#!/usr/bin/env python3
"""
Shared configuration for the EU AI Act Transparency Labeling Toolkit.
All constants, defaults, and configuration dataclasses live here so they
can be imported by the labeler, CLI, and helper scripts.

Prototype to test concepts, do not use it for compliance
Seek formal legal advice before using it for compliance with the EU AI Act

Software designed by Roberto Lofaro, developed with Kimi and Grok
CC-BY-SA-4.0 2026-08-09 https://linkedin.com/in/robertolofaro
"""

from dataclasses import dataclass, field
from typing import Literal, Optional, List
from pathlib import Path
import json
import os

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SUPPORTED_EXTENSIONS: List[str] = [".png", ".jpg", ".jpeg", ".webp"]

ICON_TYPES = ("basic", "fully_generated", "partially_modified")
VARIATIONS = ("black", "white", "black_50", "white_50")
POSITIONS = ("top_left", "top_right", "bottom_left", "bottom_right", "center")
CONTENT_TYPES = ("image", "audio", "video", "text")

DEFAULT_SCALE: float = 0.15
DEFAULT_MARGIN: int = 20
DEFAULT_WATERMARK_STRENGTH: float = 0.01
DEFAULT_CONFIDENCE: float = 1.0

# EXIF tag IDs used by the labeler
EXIF_IMAGE_DESCRIPTION = 0x010E
EXIF_COPYRIGHT = 0x8298
EXIF_SOFTWARE = 0x0131
EXIF_DATE_TIME = 0x0132
EXIF_DATE_TIME_ORIGINAL = 0x9003
EXIF_USER_COMMENT = 0x9286

# Regulation identifiers
REGULATION_ID = "EU AI Act 2024/1689"
REGULATION_ARTICLE = "50"
DIGITAL_SOURCE_TYPE = "trainedAlgorithmicMedia"

# IPTC / C2PA digital source type URIs
DST_TRAINED_ALGORITHMIC_MEDIA = (
    "http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia"
)
DST_COMPOSITE_WITH_TRAINED_ALGORITHMIC_MEDIA = (
    "http://cv.iptc.org/newscodes/digitalsourcetype/compositeWithTrainedAlgorithmicMedia"
)
DST_ALGORITHMICALLY_ENHANCED = (
    "http://cv.iptc.org/newscodes/digitalsourcetype/algorithmicallyEnhanced"
)

# Map EU AI Act icon levels → C2PA digitalSourceType
ICON_TYPE_TO_DST = {
    "basic": DST_TRAINED_ALGORITHMIC_MEDIA,
    "fully_generated": DST_TRAINED_ALGORITHMIC_MEDIA,
    "partially_modified": DST_COMPOSITE_WITH_TRAINED_ALGORITHMIC_MEDIA,
}

# Map EU AI Act icon levels → machine-readable disclosure strings
# (used in PNG text, XMP, EXIF JSON, and human Description fields)
ICON_TYPE_TO_DISCLOSURE = {
    "basic": "ai-labeled",
    "fully_generated": "fully-ai-generated",
    "partially_modified": "partially-ai-modified",
}
ICON_TYPE_TO_DISCLOSURE_SNAKE = {
    "basic": "ai_labeled",
    "fully_generated": "fully_ai_generated",
    "partially_modified": "partially_ai_modified",
}
# Short digital-source token for simple PNG text keys (non-URI form)
ICON_TYPE_TO_DIGITAL_SOURCE = {
    "basic": "trainedAlgorithmicMedia",
    "fully_generated": "trainedAlgorithmicMedia",
    "partially_modified": "compositeWithTrainedAlgorithmicMedia",
}

# Default paths for development/test signing certificates
DEFAULT_C2PA_CERT_PATH = str(Path(__file__).resolve().parent / "certs" / "es256.pub")
DEFAULT_C2PA_KEY_PATH = str(Path(__file__).resolve().parent / "certs" / "es256.pem")
DEFAULT_C2PA_TSA_URL = "http://timestamp.digicert.com"

CLAIM_GENERATOR_NAME = "EU-AI-Act-Labeler"
CLAIM_GENERATOR_VERSION = "1.1.0"

# Font search paths (first existing wins)
FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "C:/Windows/Fonts/arial.ttf",
]


# ---------------------------------------------------------------------------
# Configuration dataclasses
# ---------------------------------------------------------------------------

@dataclass
class LabelConfig:
    """Configuration for the visible label overlay.

    icon_type is compulsory – callers must explicitly choose the disclosure level.
    """
    icon_type: Literal["basic", "fully_generated", "partially_modified"]
    variation: Literal["black", "white", "black_50", "white_50"] = "black_50"
    position: Literal["top_left", "top_right", "bottom_left", "bottom_right", "center"] = "bottom_right"
    scale: float = DEFAULT_SCALE
    margin: int = DEFAULT_MARGIN

    def __post_init__(self):
        if self.icon_type not in ICON_TYPES:
            raise ValueError(
                f"icon_type must be one of {ICON_TYPES}, got '{self.icon_type}'"
            )
        if self.variation not in VARIATIONS:
            raise ValueError(
                f"variation must be one of {VARIATIONS}, got '{self.variation}'"
            )
        if self.position not in POSITIONS:
            raise ValueError(
                f"position must be one of {POSITIONS}, got '{self.position}'"
            )
        if not (0.01 <= self.scale <= 0.5):
            raise ValueError(f"scale should be between 0.01 and 0.5, got {self.scale}")
        if self.margin < 0:
            raise ValueError(f"margin must be >= 0, got {self.margin}")


@dataclass
class MetadataConfig:
    """Configuration for machine-readable metadata and watermark payload."""
    ai_system_name: str = "Generative AI System"
    ai_provider: str = "Unknown Provider"
    generation_prompt: str = ""
    generation_date: Optional[str] = None
    confidence_score: float = DEFAULT_CONFIDENCE
    content_type: Literal["image", "audio", "video", "text"] = "image"
    watermark_strength: float = DEFAULT_WATERMARK_STRENGTH

    def __post_init__(self):
        if self.content_type not in CONTENT_TYPES:
            raise ValueError(
                f"content_type must be one of {CONTENT_TYPES}, got '{self.content_type}'"
            )
        if not (0.0 <= self.confidence_score <= 1.0):
            raise ValueError(
                f"confidence_score must be between 0.0 and 1.0, got {self.confidence_score}"
            )


@dataclass
class C2PAConfig:
    """Configuration for C2PA Content Credentials (cryptographic provenance).

    Requires the optional dependency: pip install c2pa-python
    Signing needs a certificate + private key. Development certs ship in certs/.
    """
    enabled: bool = True
    cert_path: str = DEFAULT_C2PA_CERT_PATH
    key_path: str = DEFAULT_C2PA_KEY_PATH
    tsa_url: str = DEFAULT_C2PA_TSA_URL
    # If True, refuse generative training / inference / data-mining by default
    do_not_train: bool = True
    include_prompt_as_ingredient: bool = True
    # Optional override of digitalSourceType URI; None → derived from icon_type
    digital_source_type: Optional[str] = None

    def resolve_digital_source_type(self, icon_type: str) -> str:
        if self.digital_source_type:
            return self.digital_source_type
        return ICON_TYPE_TO_DST.get(icon_type, DST_TRAINED_ALGORITHMIC_MEDIA)


@dataclass
class ProcessConfig:
    """Top-level configuration for a labeling run.

    input_path  – path to a single image file OR a directory of images
    output_dir  – directory where labeled files are written (created if missing)
    icon_type   – compulsory disclosure level
    """
    input_path: str
    output_dir: str
    icon_type: Literal["basic", "fully_generated", "partially_modified"]
    variation: Literal["black", "white", "black_50", "white_50"] = "black_50"
    position: Literal["top_left", "top_right", "bottom_left", "bottom_right", "center"] = "bottom_right"
    scale: float = DEFAULT_SCALE
    margin: int = DEFAULT_MARGIN
    ai_system_name: str = "Generative AI System"
    ai_provider: str = "Unknown Provider"
    generation_prompt: str = ""
    generation_date: Optional[str] = None
    confidence_score: float = DEFAULT_CONFIDENCE
    content_type: Literal["image", "audio", "video", "text"] = "image"
    add_visible: bool = True
    add_machine_readable: bool = True
    add_watermark: bool = True
    add_c2pa: bool = True
    output_format: Optional[str] = None  # None = keep original
    c2pa: Optional[C2PAConfig] = None

    def __post_init__(self):
        if self.c2pa is None:
            self.c2pa = C2PAConfig(enabled=self.add_c2pa)
        elif not self.add_c2pa:
            self.c2pa.enabled = False

    def to_label_config(self) -> LabelConfig:
        return LabelConfig(
            icon_type=self.icon_type,
            variation=self.variation,
            position=self.position,
            scale=self.scale,
            margin=self.margin,
        )

    def to_metadata_config(self) -> MetadataConfig:
        return MetadataConfig(
            ai_system_name=self.ai_system_name,
            ai_provider=self.ai_provider,
            generation_prompt=self.generation_prompt,
            generation_date=self.generation_date,
            confidence_score=self.confidence_score,
            content_type=self.content_type,
        )

    def ensure_output_dir(self) -> Path:
        out = Path(self.output_dir)
        out.mkdir(parents=True, exist_ok=True)
        return out

    def resolve_input_files(self) -> List[Path]:
        """Return list of image files to process (single file or directory scan)."""
        p = Path(self.input_path)
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
            files = []
            for ext in SUPPORTED_EXTENSIONS:
                files.extend(sorted(p.glob(f"*{ext}")))
                files.extend(sorted(p.glob(f"*{ext.upper()}")))
            # de-duplicate while preserving order
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


def load_config_from_json(path: str) -> ProcessConfig:
    """Load a ProcessConfig from a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    required = {"input_path", "output_dir", "icon_type"}
    missing = required - set(data.keys())
    if missing:
        raise ValueError(f"Config file missing required keys: {missing}")
    return ProcessConfig(**data)


def save_example_config(path: str = "example_config.json") -> None:
    """Write an example JSON config file for documentation / bootstrapping."""
    example = {
        "input_path": "./raw_images",
        "output_dir": "./labeled_images",
        "icon_type": "fully_generated",
        "variation": "black_50",
        "position": "bottom_right",
        "scale": 0.12,
        "margin": 20,
        "ai_system_name": "Stable Diffusion XL",
        "ai_provider": "Stability AI",
        "generation_prompt": "A cute fictional UHF hamster",
        "content_type": "image",
        "add_visible": True,
        "add_machine_readable": True,
        "add_watermark": True
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(example, f, indent=2)
    print(f"Example config written to {path}")
