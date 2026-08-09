#!/usr/bin/env python3
"""
Command-line interface for the EU AI Act Transparency Labeler.

Examples
--------
# Single file
python cli.py --input photo.png --output-dir ./out --icon-type fully_generated

# Whole directory
python cli.py --input ./raw_hamsters --output-dir ./labeled --icon-type basic

# From JSON config
python cli.py --config example_config.json

Prototype to test concepts, do not use it for compliance
Seek formal legal advice before using it for compliance with the EU AI Act

Software designed by Roberto Lofaro, developed with Kimi and Grok
CC-BY-SA-4.0 2026-08-09 https://linkedin.com/in/robertolofaro
"""

import argparse
import sys
from pathlib import Path

from eu_ai_act_labeler import EUAILabeler
from config import ProcessConfig, load_config_from_json, ICON_TYPES, VARIATIONS, POSITIONS


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="EU AI Act transparency labeler – visible icon + machine-readable metadata + LSB watermark",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument(
        "--input", "-i",
        help="Path to a single image file OR a directory of images",
    )
    src.add_argument(
        "--config", "-c",
        help="Path to a JSON config file (see example_config.json)",
    )

    p.add_argument(
        "--output-dir", "-o",
        help="Output directory (created if missing). Required when not using --config.",
    )
    p.add_argument(
        "--icon-type",
        choices=ICON_TYPES,
        help="Compulsory disclosure level. Required when not using --config.",
    )
    p.add_argument("--variation", choices=VARIATIONS, default="black_50")
    p.add_argument("--position", choices=POSITIONS, default="bottom_right")
    p.add_argument("--scale", type=float, default=0.15)
    p.add_argument("--margin", type=int, default=20)
    p.add_argument("--ai-system-name", default="Generative AI System")
    p.add_argument("--ai-provider", default="Unknown Provider")
    p.add_argument("--generation-prompt", default="")
    p.add_argument("--no-visible", action="store_true", help="Skip visible label")
    p.add_argument("--no-metadata", action="store_true", help="Skip machine-readable metadata")
    p.add_argument("--no-watermark", action="store_true", help="Skip LSB watermark")

    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.config:
        cfg = load_config_from_json(args.config)
    else:
        if not args.output_dir:
            parser.error("--output-dir is required when not using --config")
        if not args.icon_type:
            parser.error("--icon-type is required when not using --config")

        cfg = ProcessConfig(
            input_path=args.input,
            output_dir=args.output_dir,
            icon_type=args.icon_type,
            variation=args.variation,
            position=args.position,
            scale=args.scale,
            margin=args.margin,
            ai_system_name=args.ai_system_name,
            ai_provider=args.ai_provider,
            generation_prompt=args.generation_prompt,
            add_visible=not args.no_visible,
            add_machine_readable=not args.no_metadata,
            add_watermark=not args.no_watermark,
        )

    labeler = EUAILabeler()
    reports = labeler.process_with_config(cfg)

    print(f"Processed {len(reports)} image(s) → {cfg.output_dir}")
    for r in reports:
        print(f"  {Path(r['input']).name} → {Path(r['output']).name}  [{', '.join(r['operations'])}]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
