#!/usr/bin/env python3
"""
C2PA Content Credentials integration for the EU AI Act Labeler.

Embeds cryptographically signed C2PA manifests that declare:
  - digitalSourceType (trainedAlgorithmicMedia / compositeWithTrainedAlgorithmicMedia)
  - c2pa.actions.v2 with c2pa.created
  - CAWG training-mining restrictions (do-not-train)
  - software agent / model provenance
  - optional generation prompt as an inputTo ingredient

Requires: pip install c2pa-python
Signing needs a cert + private key (development certs ship under certs/).

Prototype to test concepts, do not use it for compliance
Seek formal legal advice before using it for compliance with the EU AI Act

Software designed by Roberto Lofaro, developed with Kimi and Grok
CC-BY-SA-4.0 2026-08-09 https://linkedin.com/in/robertolofaro
"""

from __future__ import annotations

import json
import mimetypes
import os
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from config import (
    C2PAConfig,
    MetadataConfig,
    CLAIM_GENERATOR_NAME,
    CLAIM_GENERATOR_VERSION,
    REGULATION_ID,
    REGULATION_ARTICLE,
    ICON_TYPE_TO_DST,
    DST_TRAINED_ALGORITHMIC_MEDIA,
)

# Optional hard dependency – import is deferred so the rest of the toolkit
# still works when c2pa-python is not installed.
_C2PA_AVAILABLE = False
try:
    from c2pa import (
        Builder,
        Reader,
        Signer,
        C2paSigningAlg,
        C2paSignerInfo,
        Context,
        C2paBuilderIntent,
        C2paDigitalSourceType,
    )

    _C2PA_AVAILABLE = True
except ImportError:
    pass


def is_c2pa_available() -> bool:
    return _C2PA_AVAILABLE


# Map icon_type → C2paDigitalSourceType enum when available
_ICON_TO_ENUM = {
    "basic": "TRAINED_ALGORITHMIC_MEDIA",
    "fully_generated": "TRAINED_ALGORITHMIC_MEDIA",
    "partially_modified": "COMPOSITE_WITH_TRAINED_ALGORITHMIC_MEDIA",
}


def _mime_for_path(path: str) -> str:
    mime, _ = mimetypes.guess_type(path)
    if mime:
        return mime
    ext = Path(path).suffix.lower()
    return {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".tif": "image/tiff",
        ".tiff": "image/tiff",
    }.get(ext, "application/octet-stream")


def _load_signer(cfg: C2PAConfig) -> "Signer":
    if not _C2PA_AVAILABLE:
        raise RuntimeError(
            "c2pa-python is not installed. Run: pip install c2pa-python"
        )

    cert_path = Path(cfg.cert_path)
    key_path = Path(cfg.key_path)
    if not cert_path.is_file():
        raise FileNotFoundError(f"C2PA certificate not found: {cert_path}")
    if not key_path.is_file():
        raise FileNotFoundError(f"C2PA private key not found: {key_path}")

    cert = cert_path.read_bytes()
    key = key_path.read_bytes()
    ta = (cfg.tsa_url or "").encode("utf-8")

    signer_info = C2paSignerInfo(
        alg=C2paSigningAlg.ES256,
        sign_cert=cert,
        private_key=key,
        ta_url=ta,
    )
    return Signer.from_info(signer_info)


def build_manifest_definition(
    icon_type: str,
    metadata: MetadataConfig,
    c2pa_cfg: C2PAConfig,
    title: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Build a C2PA manifest JSON definition aligned with EU AI Act Article 50
    and the C2PA AI disclosure guidance.
    """
    dst = c2pa_cfg.resolve_digital_source_type(icon_type)

    actions = [
        {
            "action": "c2pa.created",
            "digitalSourceType": dst,
            "softwareAgent": {
                "name": metadata.ai_system_name,
                "version": "1.0",
            },
        }
    ]

    # For partially-modified content, also record an edit action
    if icon_type == "partially_modified":
        actions.append(
            {
                "action": "c2pa.edited",
                "digitalSourceType": dst,
                "softwareAgent": {
                    "name": metadata.ai_system_name,
                    "version": "1.0",
                },
                "description": "AI-assisted modification / partial generation",
            }
        )

    assertions: List[Dict[str, Any]] = [
        {
            "label": "c2pa.actions.v2",
            "data": {"actions": actions},
        }
    ]

    if c2pa_cfg.do_not_train:
        assertions.append(
            {
                "label": "cawg.training-mining",
                "data": {
                    "entries": {
                        "cawg.ai_generative_training": {"use": "notAllowed"},
                        "cawg.ai_inference": {"use": "notAllowed"},
                        "cawg.ai_training": {"use": "notAllowed"},
                        "cawg.data_mining": {"use": "notAllowed"},
                    }
                },
            }
        )

    # Custom assertion carrying EU AI Act context (non-standard but useful)
    assertions.append(
        {
            "label": "com.eu-ai-act.transparency",
            "data": {
                "regulation": REGULATION_ID,
                "article": REGULATION_ARTICLE,
                "disclosure_level": icon_type,
                "ai_system": metadata.ai_system_name,
                "ai_provider": metadata.ai_provider,
                "content_type": metadata.content_type,
                "confidence": metadata.confidence_score,
            },
        }
    )

    manifest: Dict[str, Any] = {
        "title": title or "AI-generated content",
        "claim_generator_info": [
            {
                "name": CLAIM_GENERATOR_NAME,
                "version": CLAIM_GENERATOR_VERSION,
            }
        ],
        "assertions": assertions,
    }

    return manifest


def embed_c2pa_manifest(
    source_path: str,
    dest_path: str,
    icon_type: str,
    metadata: MetadataConfig,
    c2pa_cfg: Optional[C2PAConfig] = None,
) -> Dict[str, Any]:
    """
    Embed a signed C2PA Content Credential into an image.

    Parameters
    ----------
    source_path : path to the (already labeled) image to sign
    dest_path   : where to write the signed file (may be the same as source
                  if you accept in-place replacement via a temp file)
    icon_type   : "basic" | "fully_generated" | "partially_modified"
    metadata    : MetadataConfig with model / provider info
    c2pa_cfg    : signing and assertion options

    Returns
    -------
    report dict with keys: success, active_manifest, assertions, error (optional)
    """
    if c2pa_cfg is None:
        c2pa_cfg = C2PAConfig()

    if not c2pa_cfg.enabled:
        return {"success": False, "skipped": True, "reason": "C2PA disabled"}

    if not _C2PA_AVAILABLE:
        return {
            "success": False,
            "error": "c2pa-python not installed (pip install c2pa-python)",
        }

    title = Path(source_path).name
    manifest_def = build_manifest_definition(
        icon_type=icon_type,
        metadata=metadata,
        c2pa_cfg=c2pa_cfg,
        title=title,
    )
    mime = _mime_for_path(source_path)

    # Sign to a temp file then atomically replace dest, so source can == dest
    dest = Path(dest_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(
        suffix=dest.suffix or ".jpg", dir=str(dest.parent)
    )
    os.close(fd)

    try:
        with Context() as ctx:
            with _load_signer(c2pa_cfg) as signer:
                with Builder(json.dumps(manifest_def), ctx) as builder:
                    # Prefer intent API when available for correct action structure
                    try:
                        enum_name = _ICON_TO_ENUM.get(
                            icon_type, "TRAINED_ALGORITHMIC_MEDIA"
                        )
                        dst_enum = getattr(C2paDigitalSourceType, enum_name)
                        builder.set_intent(C2paBuilderIntent.CREATE, dst_enum)
                    except Exception:
                        pass  # fall back to explicit actions in the JSON

                    builder.sign_file(source_path, tmp_path, signer)

        # Move into place
        os.replace(tmp_path, dest_path)

        # Read back for the report
        with Reader(dest_path) as reader:
            store = json.loads(reader.json())
        active = store.get("active_manifest")
        assertions = []
        if active and active in store.get("manifests", {}):
            assertions = [
                a.get("label")
                for a in store["manifests"][active].get("assertions", [])
            ]

        return {
            "success": True,
            "active_manifest": active,
            "assertions": assertions,
            "digital_source_type": c2pa_cfg.resolve_digital_source_type(icon_type),
            "output": dest_path,
        }
    except Exception as exc:
        if os.path.exists(tmp_path):
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
        return {"success": False, "error": str(exc)}


def read_c2pa_manifest(path: str) -> Optional[Dict[str, Any]]:
    """
    Read and return the C2PA manifest store from a file, or None if absent / unreadable.
    """
    if not _C2PA_AVAILABLE:
        return None
    try:
        with Reader(path) as reader:
            return json.loads(reader.json())
    except Exception:
        return None


def verify_c2pa(path: str) -> Dict[str, Any]:
    """
    High-level verification summary for a file that may contain Content Credentials.
    """
    store = read_c2pa_manifest(path)
    if store is None:
        return {
            "has_c2pa": False,
            "valid": False,
            "message": "No C2PA manifest found (or c2pa-python missing)",
        }

    active_id = store.get("active_manifest")
    manifests = store.get("manifests", {})
    if not active_id or active_id not in manifests:
        return {
            "has_c2pa": True,
            "valid": False,
            "message": "Manifest store present but no active manifest",
            "store": store,
        }

    manifest = manifests[active_id]
    assertions = manifest.get("assertions", [])
    labels = [a.get("label") for a in assertions]

    # Extract digitalSourceType if present
    dst = None
    for a in assertions:
        if a.get("label") in ("c2pa.actions", "c2pa.actions.v2"):
            for act in a.get("data", {}).get("actions", []):
                if act.get("digitalSourceType"):
                    dst = act["digitalSourceType"]
                    break

    validation_status = store.get("validation_status") or manifest.get(
        "validation_status"
    )

    return {
        "has_c2pa": True,
        "valid": validation_status is None
        or (
            isinstance(validation_status, list) and len(validation_status) == 0
        ),
        "active_manifest": active_id,
        "title": manifest.get("title"),
        "assertions": labels,
        "digital_source_type": dst,
        "claim_generator": manifest.get("claim_generator")
        or manifest.get("claim_generator_info"),
        "validation_status": validation_status,
        "store": store,
    }
