#!/usr/bin/env python3
"""
EU AI Act Transparency Labeling Toolkit
========================================
A self-contained Python routine to apply EU AI Act compliant labels to images.

Features:
- Generates the three official EU AI Act icons programmatically (no external assets needed)
- Overlays visible labels on images with configurable position, size, and style
- Embeds machine-readable metadata (EXIF, XMP) marking content as AI-generated
- Adds an imperceptible LSB watermark for detection resilience
- Supports single-file or directory (batch) processing via a unified API

Shared constants and dataclasses live in config.py.

Requirements: Pillow, numpy
Install: pip install Pillow numpy

Prototype to test concepts, do not use it for compliance
Seek formal legal advice before using it for compliance with the EU AI Act

Software designed by Roberto Lofaro, developed with Kimi and Grok
CC-BY-SA-4.0 2026-08-09 https://linkedin.com/in/robertolofaro
"""

from PIL import Image, ImageDraw, ImageFont, PngImagePlugin
import numpy as np
import json
import os
from datetime import datetime, timezone
from typing import Literal, Tuple, Optional, List, Union
from pathlib import Path

from config import (
    LabelConfig,
    MetadataConfig,
    ProcessConfig,
    C2PAConfig,
    SUPPORTED_EXTENSIONS,
    FONT_CANDIDATES,
    EXIF_IMAGE_DESCRIPTION,
    EXIF_COPYRIGHT,
    EXIF_SOFTWARE,
    EXIF_DATE_TIME,
    EXIF_DATE_TIME_ORIGINAL,
    EXIF_USER_COMMENT,
    REGULATION_ID,
    REGULATION_ARTICLE,
    DIGITAL_SOURCE_TYPE,
    ICON_TYPE_TO_DISCLOSURE,
    ICON_TYPE_TO_DISCLOSURE_SNAKE,
    ICON_TYPE_TO_DIGITAL_SOURCE,
    ICON_TYPE_TO_DST,
)
from c2pa_provenance import embed_c2pa_manifest, is_c2pa_available, verify_c2pa


class EUAILabeler:
    """
    EU AI Act compliant image labeler.

    Implements both visible disclosure (Article 50.4) and machine-readable
    marking (Article 50.2) for AI-generated synthetic content.
    """

    def __init__(self):
        self._font_cache = {}
        self._icon_cache = {}

    def _get_font(self, size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
        """Load a suitable system font with fallback."""
        cache_key = (size, bold)
        if cache_key in self._font_cache:
            return self._font_cache[cache_key]

        for fn in FONT_CANDIDATES:
            if os.path.exists(fn):
                try:
                    font = ImageFont.truetype(fn, size)
                    self._font_cache[cache_key] = font
                    return font
                except Exception:
                    continue

        font = ImageFont.load_default()
        self._font_cache[cache_key] = font
        return font

    def create_icon(
        self,
        icon_type: Literal["basic", "fully_generated", "partially_modified"] = "basic",
        variation: Literal["black", "white", "black_50", "white_50"] = "black",
        base_size: int = 200
    ) -> Image.Image:
        """Generate an EU AI Act icon programmatically."""
        cache_key = (icon_type, variation, base_size)
        if cache_key in self._icon_cache:
            return self._icon_cache[cache_key].copy()

        is_black = variation.startswith("black")
        is_transparent = "50" in variation

        bg_color = (0, 0, 0, 255) if is_black else (255, 255, 255, 255)
        text_color = (255, 255, 255, 255) if is_black else (0, 0, 0, 255)

        if is_transparent:
            bg_color = (*bg_color[:3], 128)

        if icon_type == "basic":
            img = Image.new("RGBA", (base_size, base_size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            margin = 5
            draw.ellipse(
                [margin, margin, base_size - margin, base_size - margin],
                fill=bg_color,
            )

            font = self._get_font(base_size // 3, bold=True)
            text = "AI"
            bbox = draw.textbbox((0, 0), text, font=font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]
            x = (base_size - text_w) // 2
            y = (base_size - text_h) // 2 - 5
            draw.text((x, y), text, fill=text_color, font=font)

        elif icon_type in ("fully_generated", "partially_modified"):
            text = (
                "AI GENERATED"
                if icon_type == "fully_generated"
                else "AI MODIFIED"
            )

            temp_img = Image.new("RGBA", (1, 1))
            temp_draw = ImageDraw.Draw(temp_img)
            font = self._get_font(base_size // 5, bold=True)
            bbox = temp_draw.textbbox((0, 0), text, font=font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]

            padding_x = base_size // 4
            padding_y = base_size // 6
            pill_w = text_w + padding_x * 2
            pill_h = text_h + padding_y * 2

            img = Image.new("RGBA", (pill_w, pill_h), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)

            radius = pill_h // 2
            draw.rounded_rectangle(
                [0, 0, pill_w, pill_h], radius=radius, fill=bg_color
            )

            x = (pill_w - text_w) // 2
            y = (pill_h - text_h) // 2 - 3
            draw.text((x, y), text, fill=text_color, font=font)
        else:
            raise ValueError(f"Unknown icon_type: {icon_type}")

        self._icon_cache[cache_key] = img.copy()
        return img

    def _calculate_position(
        self,
        img_size: Tuple[int, int],
        icon_size: Tuple[int, int],
        position: str,
        margin: int,
    ) -> Tuple[int, int]:
        img_w, img_h = img_size
        icon_w, icon_h = icon_size

        if position == "top_left":
            return (margin, margin)
        elif position == "top_right":
            return (img_w - icon_w - margin, margin)
        elif position == "bottom_left":
            return (margin, img_h - icon_h - margin)
        elif position == "bottom_right":
            return (img_w - icon_w - margin, img_h - icon_h - margin)
        elif position == "center":
            return ((img_w - icon_w) // 2, (img_h - icon_h) // 2)
        else:
            return (img_w - icon_w - margin, img_h - icon_h - margin)

    def add_visible_label(
        self,
        image: Image.Image,
        config: LabelConfig,
    ) -> Image.Image:
        """Overlay the EU AI Act visible label on an image."""
        if image.mode != "RGBA":
            img = image.convert("RGBA")
        else:
            img = image.copy()

        img_w, img_h = img.size

        target_width = int(img_w * config.scale)
        icon = self.create_icon(
            config.icon_type, config.variation, base_size=200
        )
        orig_w, orig_h = icon.size
        scale_factor = target_width / orig_w
        target_height = int(orig_h * scale_factor)
        icon = icon.resize((target_width, target_height), Image.LANCZOS)

        x, y = self._calculate_position(
            img.size, icon.size, config.position, config.margin
        )

        img.paste(icon, (x, y), icon)
        return img

    @staticmethod
    def _disclosure_for(icon_type: str) -> Tuple[str, str, str]:
        """Return (kebab disclosure, snake disclosure, digital-source token)."""
        disclosure = ICON_TYPE_TO_DISCLOSURE.get(icon_type, "fully-ai-generated")
        disclosure_snake = ICON_TYPE_TO_DISCLOSURE_SNAKE.get(
            icon_type, "fully_ai_generated"
        )
        digital_source = ICON_TYPE_TO_DIGITAL_SOURCE.get(
            icon_type, DIGITAL_SOURCE_TYPE
        )
        return disclosure, disclosure_snake, digital_source

    @staticmethod
    def _human_description(
        icon_type: str, content_type: str, ai_system_name: str
    ) -> str:
        if icon_type == "partially_modified":
            return (
                f"AI-MODIFIED: This {content_type} was partially modified using "
                f"{ai_system_name}. EU AI Act Article 50 transparency disclosure."
            )
        if icon_type == "basic":
            return (
                f"AI-LABELED: This {content_type} is marked as AI-related "
                f"({ai_system_name}). EU AI Act Article 50 transparency disclosure."
            )
        return (
            f"AI-GENERATED: This {content_type} was created using "
            f"{ai_system_name}. EU AI Act Article 50 transparency disclosure."
        )

    def _build_xmp_metadata(
        self, config: MetadataConfig, icon_type: str = "fully_generated"
    ) -> str:
        """Build XMP packet with AI generation provenance."""
        date_str = config.generation_date or datetime.now(timezone.utc).isoformat()
        disclosure, _, digital_source = self._disclosure_for(icon_type)
        desc = self._human_description(
            icon_type, config.content_type, config.ai_system_name
        )

        lines = [
            '<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>',
            '<x:xmpmeta xmlns:x="adobe:ns:meta/">',
            ' <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">',
            '  <rdf:Description rdf:about=""',
            '    xmlns:dc="http://purl.org/dc/elements/1.1/"',
            '    xmlns:xmp="http://ns.adobe.com/xap/1.0/"',
            '    xmlns:ai="https://digital-strategy.ec.europa.eu/ai-act/ns/"',
            '    xmlns:c2pa="http://c2pa.org/">',
            "   <dc:description>",
            "    <rdf:Alt>",
            f'     <rdf:li xml:lang="x-default">{desc}</rdf:li>',
            "    </rdf:Alt>",
            "   </dc:description>",
            "   <dc:rights>",
            "    <rdf:Alt>",
            '     <rdf:li xml:lang="x-default">AI-related content - EU AI Act transparency disclosure</rdf:li>',
            "    </rdf:Alt>",
            "   </dc:rights>",
            f"   <xmp:CreatorTool>{config.ai_system_name}</xmp:CreatorTool>",
            f"   <xmp:CreateDate>{date_str}</xmp:CreateDate>",
            f"   <xmp:ModifyDate>{date_str}</xmp:ModifyDate>",
            "   <ai:generatedByAI>true</ai:generatedByAI>",
            f"   <ai:aiSystemName>{config.ai_system_name}</ai:aiSystemName>",
            f"   <ai:aiProvider>{config.ai_provider}</ai:aiProvider>",
            f"   <ai:generationDate>{date_str}</ai:generationDate>",
            f"   <ai:contentType>{config.content_type}</ai:contentType>",
            f"   <ai:transparencyLabel>{disclosure}</ai:transparencyLabel>",
            f"   <ai:digitalSourceType>{digital_source}</ai:digitalSourceType>",
            "   <c2pa:assertions>",
            "    <rdf:Seq>",
            f"     <rdf:li>{disclosure}</rdf:li>",
            "     <rdf:li>eu-ai-act-article-50</rdf:li>",
            "    </rdf:Seq>",
            "   </c2pa:assertions>",
            "  </rdf:Description>",
            " </rdf:RDF>",
            "</x:xmpmeta>",
            '<?xpacket end="w"?>',
        ]
        return "\n".join(lines)

    def _build_pnginfo(
        self, config: MetadataConfig, icon_type: str = "fully_generated"
    ) -> PngImagePlugin.PngInfo:
        """Build PngInfo with all machine-readable metadata."""
        pnginfo = PngImagePlugin.PngInfo()

        date_str = config.generation_date or datetime.now(timezone.utc).isoformat()
        disclosure, disclosure_snake, digital_source = self._disclosure_for(icon_type)

        xmp = self._build_xmp_metadata(config, icon_type=icon_type)
        pnginfo.add_text("xml:com.adobe.xmp", xmp)

        pnginfo.add_text("ai-generated", "true")
        pnginfo.add_text("ai-regulation", REGULATION_ID)
        pnginfo.add_text("ai-article", REGULATION_ARTICLE)
        pnginfo.add_text("ai-system", config.ai_system_name)
        pnginfo.add_text("ai-provider", config.ai_provider)
        pnginfo.add_text("ai-date", date_str)
        pnginfo.add_text("ai-content-type", config.content_type)
        pnginfo.add_text("ai-disclosure", disclosure)
        pnginfo.add_text("ai-digital-source", digital_source)

        metadata_json = json.dumps(
            {
                "ai_generated": True,
                "regulation": REGULATION_ID,
                "article": REGULATION_ARTICLE,
                "obligation": "transparency_synthetic_content",
                "content_type": config.content_type,
                "ai_system": config.ai_system_name,
                "ai_provider": config.ai_provider,
                "generation_date": date_str,
                "digital_source_type": digital_source,
                "confidence": config.confidence_score,
                "disclosure_type": disclosure_snake,
                "icon_type": icon_type,
                "version": "1.0",
            },
            ensure_ascii=False,
        )
        pnginfo.add_text("ai-metadata-json", metadata_json)

        pnginfo.add_text(
            "Description",
            self._human_description(
                icon_type, config.content_type, config.ai_system_name
            ),
        )

        return pnginfo

    def _build_exif_bytes(
        self, config: MetadataConfig, icon_type: str = "fully_generated"
    ) -> bytes:
        """Build EXIF bytes with AI generation markers."""
        date_str = (
            config.generation_date
            or datetime.now(timezone.utc).strftime("%Y:%m:%d %H:%M:%S")
        )
        _, disclosure_snake, digital_source = self._disclosure_for(icon_type)

        exif_dict = {}
        exif_dict[EXIF_IMAGE_DESCRIPTION] = self._human_description(
            icon_type, config.content_type, config.ai_system_name
        )
        if icon_type == "partially_modified":
            copyright_label = "AI-Modified Content"
            software_suffix = "AI-Modified"
        else:
            copyright_label = "AI-Generated Content"
            software_suffix = "AI-Generated"
        exif_dict[EXIF_COPYRIGHT] = (
            f"{copyright_label} | EU AI Act Transparency | "
            f"Synthetic media per Regulation (EU) 2024/1689"
        )
        exif_dict[EXIF_SOFTWARE] = f"{config.ai_system_name} ({software_suffix})"
        exif_dict[EXIF_DATE_TIME] = date_str
        exif_dict[EXIF_DATE_TIME_ORIGINAL] = date_str

        metadata_json = json.dumps(
            {
                "ai_generated": True,
                "regulation": REGULATION_ID,
                "article": REGULATION_ARTICLE,
                "content_type": config.content_type,
                "ai_system": config.ai_system_name,
                "generation_date": date_str,
                "disclosure_type": disclosure_snake,
                "digital_source_type": digital_source,
                "icon_type": icon_type,
            },
            ensure_ascii=False,
        )

        prefix = b"\x00" * 8
        exif_dict[EXIF_USER_COMMENT] = prefix + metadata_json.encode("utf-8")

        return self._dict_to_exif(exif_dict)

    def _dict_to_exif(self, exif_dict: dict) -> bytes:
        """Convert a dictionary of EXIF tags to raw EXIF bytes."""
        try:
            import piexif

            exif_ifd = {}
            for tag_id, value in exif_dict.items():
                if tag_id == EXIF_IMAGE_DESCRIPTION:
                    exif_ifd["0x010E"] = value.encode("utf-8")
                elif tag_id == EXIF_COPYRIGHT:
                    exif_ifd["0x8298"] = value.encode("utf-8")
                elif tag_id == EXIF_SOFTWARE:
                    exif_ifd["0x0131"] = value.encode("utf-8")
                elif tag_id == EXIF_DATE_TIME:
                    exif_ifd["0x0132"] = value.encode("ascii")
                elif tag_id == EXIF_DATE_TIME_ORIGINAL:
                    exif_ifd["0x9003"] = value.encode("ascii")
                elif tag_id == EXIF_USER_COMMENT:
                    exif_ifd["0x9286"] = value

            exif_dict_piexif = {"0th": exif_ifd}
            return piexif.dump(exif_dict_piexif)
        except ImportError:
            return b""

    def add_invisible_watermark(
        self,
        image: Image.Image,
        config: MetadataConfig,
    ) -> Image.Image:
        """Embed an imperceptible LSB watermark in the blue channel."""
        img = image.copy()
        if img.mode != "RGB":
            img = img.convert("RGB")

        arr = np.array(img, dtype=np.uint8)

        payload = json.dumps(
            {
                "ai": True,
                "reg": "EU-AI-Act",
                "art": REGULATION_ARTICLE,
                "sys": config.ai_system_name,
                "date": config.generation_date
                or datetime.now(timezone.utc).isoformat(),
                "type": config.content_type,
                "ver": "1.0",
            }
        )

        binary = "".join(format(ord(c), "08b") for c in payload)
        binary += "00000000"

        flat_blue = arr[:, :, 2].flatten()

        if len(binary) > len(flat_blue):
            raise ValueError(
                f"Image too small for watermark. Need {len(binary)} pixels, "
                f"have {len(flat_blue)}"
            )

        for i, bit in enumerate(binary):
            current_lsb = flat_blue[i] & 1
            if current_lsb != int(bit):
                if int(bit) == 1:
                    flat_blue[i] = flat_blue[i] | 1
                else:
                    flat_blue[i] = flat_blue[i] & 0xFE

        arr[:, :, 2] = flat_blue.reshape(arr.shape[:2])
        return Image.fromarray(arr)

    def read_watermark(self, image: Image.Image) -> Optional[dict]:
        """Extract and decode the LSB watermark from an image."""
        if image.mode != "RGB":
            img = image.convert("RGB")
        else:
            img = image

        arr = np.array(img, dtype=np.uint8)
        flat_blue = arr[:, :, 2].flatten()

        bits = [str(pixel & 1) for pixel in flat_blue]

        chars = []
        for i in range(0, len(bits), 8):
            byte = "".join(bits[i : i + 8])
            char_code = int(byte, 2)
            if char_code == 0:
                break
            chars.append(chr(char_code))

        payload = "".join(chars)

        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            return None

    def process_image(
        self,
        input_path: str,
        output_path: str,
        label_config: LabelConfig,
        metadata_config: Optional[MetadataConfig] = None,
        add_visible: bool = True,
        add_machine_readable: bool = True,
        add_watermark: bool = True,
        add_c2pa: bool = True,
        c2pa_config: Optional[C2PAConfig] = None,
        output_format: Optional[str] = None,
    ) -> dict:
        """
        Process a single image: visible label, metadata, watermark, and C2PA.

        label_config.icon_type is compulsory (enforced by LabelConfig).
        Returns a report dict with processing details.
        """
        if metadata_config is None:
            metadata_config = MetadataConfig()
        if c2pa_config is None:
            c2pa_config = C2PAConfig(enabled=add_c2pa)
        elif not add_c2pa:
            c2pa_config.enabled = False

        img = Image.open(input_path)
        original_mode = img.mode
        original_format = img.format or output_format or "PNG"

        report = {
            "input": input_path,
            "output": output_path,
            "original_size": img.size,
            "original_mode": original_mode,
            "operations": [],
        }

        if add_watermark:
            img = self.add_invisible_watermark(img, metadata_config)
            report["operations"].append("invisible_watermark")

        if add_visible:
            img = self.add_visible_label(img, label_config)
            report["operations"].append("visible_label")
            report["label_type"] = label_config.icon_type
            report["label_position"] = label_config.position

        if output_format is None:
            output_format = original_format

        ext = os.path.splitext(output_path)[1].lower()
        if ext in (".jpg", ".jpeg"):
            output_format = "JPEG"
        elif ext == ".png":
            output_format = "PNG"
        elif ext == ".webp":
            output_format = "WEBP"

        save_kwargs = {}

        if output_format == "PNG":
            pnginfo = self._build_pnginfo(
                metadata_config, icon_type=label_config.icon_type
            )
            save_kwargs["pnginfo"] = pnginfo
            if img.mode != "RGBA":
                img = img.convert("RGBA")
        elif output_format == "JPEG":
            if img.mode == "RGBA":
                bg = Image.new("RGB", img.size, (255, 255, 255))
                bg.paste(img, mask=img.split()[3])
                img = bg
            elif img.mode != "RGB":
                img = img.convert("RGB")

            exif_bytes = self._build_exif_bytes(
                metadata_config, icon_type=label_config.icon_type
            )
            if exif_bytes:
                save_kwargs["exif"] = exif_bytes

            save_kwargs["quality"] = 95
            save_kwargs["optimize"] = True

        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        img.save(output_path, format=output_format, **save_kwargs)
        report["output_format"] = output_format
        report["output_size"] = img.size

        if add_machine_readable:
            report["operations"].append("machine_readable_metadata")

        # C2PA Content Credentials (signed provenance) — applied last so the
        # manifest covers the final labeled bytes.
        if c2pa_config.enabled:
            if not is_c2pa_available():
                report["c2pa"] = {
                    "success": False,
                    "error": "c2pa-python not installed",
                }
            else:
                c2pa_result = embed_c2pa_manifest(
                    source_path=output_path,
                    dest_path=output_path,
                    icon_type=label_config.icon_type,
                    metadata=metadata_config,
                    c2pa_cfg=c2pa_config,
                )
                report["c2pa"] = c2pa_result
                if c2pa_result.get("success"):
                    report["operations"].append("c2pa_content_credentials")

        return report

    def process(
        self,
        input_path: Union[str, Path],
        output_dir: Union[str, Path],
        icon_type: Literal["basic", "fully_generated", "partially_modified"],
        variation: Literal["black", "white", "black_50", "white_50"] = "black_50",
        position: Literal[
            "top_left", "top_right", "bottom_left", "bottom_right", "center"
        ] = "bottom_right",
        scale: float = 0.15,
        margin: int = 20,
        metadata_config: Optional[MetadataConfig] = None,
        add_visible: bool = True,
        add_machine_readable: bool = True,
        add_watermark: bool = True,
        add_c2pa: bool = True,
        c2pa_config: Optional[C2PAConfig] = None,
        output_format: Optional[str] = None,
    ) -> List[dict]:
        """
        Unified entry point: process a single file OR an entire directory.

        Parameters
        ----------
        input_path : str or Path
            Path to one image file, or to a directory containing images.
        output_dir : str or Path
            Directory where labeled images are written. Created if it does not exist.
        icon_type : str
            Compulsory disclosure level: "basic", "fully_generated", or
            "partially_modified".
        add_c2pa : bool
            Embed a signed C2PA Content Credential (requires c2pa-python).
        c2pa_config : C2PAConfig, optional
            Certificate paths, TSA, do-not-train flags, etc.

        Returns
        -------
        list of report dicts (one per processed image)
        """
        cfg = ProcessConfig(
            input_path=str(input_path),
            output_dir=str(output_dir),
            icon_type=icon_type,
            variation=variation,
            position=position,
            scale=scale,
            margin=margin,
            add_visible=add_visible,
            add_machine_readable=add_machine_readable,
            add_watermark=add_watermark,
            add_c2pa=add_c2pa,
            output_format=output_format,
            c2pa=c2pa_config,
        )

        # Apply any extra metadata fields if a MetadataConfig was supplied
        if metadata_config is not None:
            cfg.ai_system_name = metadata_config.ai_system_name
            cfg.ai_provider = metadata_config.ai_provider
            cfg.generation_prompt = metadata_config.generation_prompt
            cfg.generation_date = metadata_config.generation_date
            cfg.confidence_score = metadata_config.confidence_score
            cfg.content_type = metadata_config.content_type

        return self.process_with_config(cfg)

    def process_with_config(self, cfg: ProcessConfig) -> List[dict]:
        """Process using a full ProcessConfig object."""
        out_dir = cfg.ensure_output_dir()
        files = cfg.resolve_input_files()
        label_cfg = cfg.to_label_config()
        meta_cfg = cfg.to_metadata_config()
        c2pa_cfg = cfg.c2pa or C2PAConfig(enabled=cfg.add_c2pa)

        reports = []
        for f in files:
            out_file = out_dir / f"{f.stem}_ai_labeled{f.suffix}"
            report = self.process_image(
                str(f),
                str(out_file),
                label_config=label_cfg,
                metadata_config=meta_cfg,
                add_visible=cfg.add_visible,
                add_machine_readable=cfg.add_machine_readable,
                add_watermark=cfg.add_watermark,
                add_c2pa=cfg.add_c2pa,
                c2pa_config=c2pa_cfg,
                output_format=cfg.output_format,
            )
            reports.append(report)

        return reports

    # Keep the old name as a thin alias for backward compatibility
    def batch_process(
        self,
        input_dir: str,
        output_dir: str,
        label_config: LabelConfig,
        metadata_config: Optional[MetadataConfig] = None,
        **kwargs,
    ) -> List[dict]:
        """
        Backward-compatible alias.

        Prefer the new process() method which accepts either a file or a directory
        and requires icon_type explicitly.
        """
        return self.process(
            input_path=input_dir,
            output_dir=output_dir,
            icon_type=label_config.icon_type,
            variation=label_config.variation,
            position=label_config.position,
            scale=label_config.scale,
            margin=label_config.margin,
            metadata_config=metadata_config,
            **kwargs,
        )


def demo():
    """Run a demonstration of the labeler on a synthetic test image."""
    labeler = EUAILabeler()

    test_img = Image.new("RGB", (800, 600), (200, 180, 160))
    draw = ImageDraw.Draw(test_img)

    draw.ellipse(
        [250, 200, 550, 500],
        fill=(210, 170, 140),
        outline=(180, 140, 110),
        width=3,
    )
    draw.ellipse(
        [300, 150, 400, 250],
        fill=(210, 170, 140),
        outline=(180, 140, 110),
        width=3,
    )
    draw.ellipse(
        [400, 150, 500, 250],
        fill=(210, 170, 140),
        outline=(180, 140, 110),
        width=3,
    )
    draw.ellipse([350, 300, 380, 330], fill=(0, 0, 0))
    draw.ellipse([420, 300, 450, 330], fill=(0, 0, 0))
    draw.ellipse([380, 350, 420, 390], fill=(255, 160, 160))

    import random

    random.seed(42)
    for _ in range(200):
        x = random.randint(260, 540)
        y = random.randint(210, 490)
        draw.point((x, y), fill=(190, 150, 120))

    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32
        )
    except Exception:
        font = ImageFont.load_default()
    draw.text((280, 520), "UHF Fictional Hamster", fill=(80, 60, 40), font=font)

    os.makedirs("/home/workdir/artifacts/demo_output", exist_ok=True)
    test_img.save("/home/workdir/artifacts/demo_output/test_hamster_original.png")

    configs = [
        ("basic", "bottom_right"),
        ("fully_generated", "top_left"),
        ("partially_modified", "bottom_left"),
    ]

    results = []
    for icon_type, position in configs:
        lc = LabelConfig(
            icon_type=icon_type,
            variation="black_50",
            position=position,
            scale=0.12,
        )
        mc = MetadataConfig(
            ai_system_name="Stable Diffusion XL",
            ai_provider="Stability AI",
            generation_prompt="A cute fictional UHF hamster, digital art",
            content_type="image",
        )

        out_path = f"/home/workdir/artifacts/demo_output/hamster_{icon_type}.png"
        report = labeler.process_image(
            "/home/workdir/artifacts/demo_output/test_hamster_original.png",
            out_path,
            label_config=lc,
            metadata_config=mc,
            add_visible=True,
            add_machine_readable=True,
            add_watermark=True,
        )
        results.append((icon_type, out_path, report))

    # Also demonstrate the unified process() API on the demo directory
    reports = labeler.process(
        input_path="/home/workdir/artifacts/demo_output/test_hamster_original.png",
        output_dir="/home/workdir/artifacts/demo_output/from_process_api",
        icon_type="fully_generated",
        variation="black_50",
        position="bottom_right",
        scale=0.12,
        metadata_config=MetadataConfig(
            ai_system_name="Stable Diffusion XL",
            ai_provider="Stability AI",
        ),
    )
    print(f"process() API produced {len(reports)} report(s)")

    wm_check = labeler.read_watermark(
        Image.open("/home/workdir/artifacts/demo_output/hamster_fully_generated.png")
    )

    print("\n" + "=" * 60)
    print("EU AI Act Labeling Demo Complete")
    print("=" * 60)
    for icon_type, out_path, report in results:
        print(f"\n{icon_type.upper()}:")
        print(f"  Output: {out_path}")
        print(f"  Operations: {', '.join(report['operations'])}")
    print(f"\nWatermark verification: {wm_check}")

    return results, wm_check


if __name__ == "__main__":
    demo()
