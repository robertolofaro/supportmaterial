#!/usr/bin/env python3
"""
LSB watermark verification for the EU AI Act Transparency Labeler.

Reads the imperceptible blue-channel LSB watermark from one or more
previously labeled images and reports the decoded payload.

Examples
--------
# Single file
python watermark_check.py --input ./labeled/photo_ai_labeled.png

# Whole directory
python watermark_check.py --input ./labeled_hamsters

# From JSON config
python watermark_check.py --config watermark_config.json

# Quiet mode (machine-readable JSON only)
python watermark_check.py -i photo_ai_labeled.png --json

Prototype to test concepts, do not use it for compliance
Seek formal legal advice before using it for compliance with the EU AI Act

Software designed by Roberto Lofaro, developed with Kimi and Grok
CC-BY-SA-4.0 2026-08-09 https://linkedin.com/in/robertolofaro
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from PIL import Image

from config import SUPPORTED_EXTENSIONS
from eu_ai_act_labeler import EUAILabeler


def resolve_input_files(input_path: str) -> List[Path]:
    """Return list of image files (single file or directory scan)."""
    p = Path(input_path)
    if not p.exists():
        raise FileNotFoundError(f"Input path does not exist: {p}")

    if p.is_file():
        if p.suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type '{p.suffix}'. "
                f"Supported: {SUPPORTED_EXTENSIONS}"
            )
        return [p]

    if p.is_dir():
        files: List[Path] = []
        for ext in SUPPORTED_EXTENSIONS:
            files.extend(sorted(p.glob(f"*{ext}")))
            files.extend(sorted(p.glob(f"*{ext.upper()}")))
        seen = set()
        unique = []
        for f in files:
            if f not in seen:
                seen.add(f)
                unique.append(f)
        if not unique:
            raise FileNotFoundError(
                f"No supported image files found in directory: {p}"
            )
        return unique

    raise ValueError(f"Input path is neither a file nor a directory: {p}")


def load_config(path: str) -> Dict[str, Any]:
    """Load a simple JSON config: {\"input_path\": \"...\", ...}."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if "input_path" not in data:
        raise ValueError("Config file must contain 'input_path'")
    return data


def check_file(labeler: EUAILabeler, path: Path) -> Dict[str, Any]:
    """Decode watermark from one image; return a result dict."""
    entry: Dict[str, Any] = {
        "input": str(path),
        "found": False,
        "payload": None,
        "error": None,
    }
    try:
        img = Image.open(path)
        payload = labeler.read_watermark(img)
        if payload is None:
            entry["error"] = "No valid LSB watermark payload found"
        else:
            entry["found"] = True
            entry["payload"] = payload
    except Exception as exc:
        entry["error"] = str(exc)
    return entry


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=(
            "Verify the imperceptible LSB watermark embedded by the "
            "EU AI Act Transparency Labeler"
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument(
        "--input", "-i",
        help="Path to a single labeled image OR a directory of labeled images",
    )
    src.add_argument(
        "--config", "-c",
        help="Path to a JSON config file with at least an 'input_path' key",
    )

    p.add_argument(
        "--json",
        action="store_true",
        help="Print results as a single JSON array (machine-readable)",
    )
    p.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 2 if any file has no valid watermark",
    )

    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.config:
        cfg = load_config(args.config)
        input_path = cfg["input_path"]
    else:
        input_path = args.input

    try:
        files = resolve_input_files(input_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    labeler = EUAILabeler()
    results = [check_file(labeler, f) for f in files]

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(f"Checked {len(results)} file(s)\n")
        for r in results:
            name = Path(r["input"]).name
            if r["found"]:
                print(f"  ✓ {name}")
                payload = r["payload"] or {}
                for k, v in payload.items():
                    print(f"      {k}: {v}")
            else:
                print(f"  ✗ {name}")
                print(f"      error: {r['error']}")
            print()

        found = sum(1 for r in results if r["found"])
        print(f"Summary: {found}/{len(results)} watermark(s) detected")

    if args.strict and any(not r["found"] for r in results):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
