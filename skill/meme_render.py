# meme_render.py
# Meme text overlay tool — supports Pillow and ImageMagick backends
# Usage: python3 meme_render.py <template.yml> TEXT1 TEXT2 TEXT3 [--layout chest-label] [--backend pillow|magick] [--output out.jpg]

import argparse
import os
import subprocess
import sys
import tempfile

import yaml
from PIL import Image, ImageDraw, ImageFont

GITHUB_RAW = "https://raw.githubusercontent.com/edwinjhlee/awesome-meme/main"


def _resolve_template(template_arg):
    """Accept a local path or meme ID (e.g. 'distracted-boyfriend')."""
    if os.path.isfile(template_arg):
        with open(template_arg) as f:
            return yaml.safe_load(f)
    # Treat as meme ID, download from GitHub
    meme_id = template_arg.replace("_", "-")
    url = f"{GITHUB_RAW}/templates/{meme_id}.yml"
    print(f"Downloading template: {url}")
    r = subprocess.run(["curl", "-sL", url], capture_output=True, text=True, timeout=10)
    if r.returncode != 0 or not r.stdout.strip():
        print(f"Error: template '{meme_id}' not found", file=sys.stderr)
        sys.exit(1)
    return yaml.safe_load(r.stdout)


def download_image(urls, dest):
    for entry in urls:
        url = entry.get("url") or entry.get("path")
        if not url:
            continue
        if entry.get("path") and os.path.exists(url):
            return url
        try:
            r = subprocess.run(["curl", "-sL", "-o", dest, url], timeout=15)
            if r.returncode == 0 and os.path.exists(dest):
                return dest
        except Exception:
            continue
    return None


def render_pillow(template, image_path, texts, layout_id, output):
    img = Image.open(image_path)
    if tuple(img.size) != tuple(template["image_size"]):
        img = img.resize(tuple(template["image_size"]))
    draw = ImageDraw.Draw(img)

    font_cfg = template["font"]
    font_size = font_cfg["size"]
    font_path = font_cfg.get("path")
    try:
        font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default(font_size)
    except Exception:
        font = ImageFont.load_default(font_size)

    layout = _get_layout(template, layout_id)
    slots = layout["slots"]

    for i, slot in enumerate(slots):
        if i >= len(texts):
            break
        pos = tuple(slot["pos"])
        draw.text(
            pos, texts[i], font=font,
            fill=font_cfg.get("color", "white"),
            stroke_width=font_cfg.get("stroke_width", 4),
            stroke_fill=font_cfg.get("stroke_color", "black"),
            anchor=font_cfg.get("anchor", "mm"),
        )

    img.save(output, quality=95)
    return output


def render_magick(template, image_path, texts, layout_id, output):
    font_cfg = template["font"]
    font_family = font_cfg.get("family", "Impact")
    font_size = font_cfg["size"]
    stroke_w = font_cfg.get("stroke_width", 4)
    anchor = font_cfg.get("anchor", "mm")

    # Convert center coords to ImageMagick left-baseline
    # For anchor="mm": im_x = center_x - text_width/2, im_y = center_y + font_size*0.35
    ascent_offset = int(font_size * 0.35)

    layout = _get_layout(template, layout_id)
    slots = layout["slots"]

    cmd = ["magick", image_path, "-colorspace", "sRGB"]

    for i, slot in enumerate(slots):
        if i >= len(texts):
            break
        cx, cy = slot["pos"]
        # Approximate: use center coords directly with -annotate +gravity
        # Simpler: use -draw text with calculated offset
        im_x = cx - len(texts[i]) * font_size // 4  # rough estimate
        im_y = cy + ascent_offset

        cmd.extend([
            "-font", font_family,
            "-pointsize", str(font_size),
            "-fill", font_cfg.get("color", "white"),
            "-stroke", font_cfg.get("stroke_color", "black"),
            "-strokewidth", str(stroke_w),
            "-draw", f"text {im_x},{im_y} '{texts[i]}'",
        ])

    cmd.append(output)
    subprocess.run(cmd, check=True)
    return output


def _get_layout(template, layout_id):
    layouts = template["layouts"]
    if layout_id:
        for l in layouts:
            if l["id"] == layout_id:
                return l
    # default
    for l in layouts:
        if l.get("default"):
            return l
    return layouts[0]


def main():
    parser = argparse.ArgumentParser(description="Meme text overlay renderer")
    parser.add_argument("template", help="Meme ID (e.g. distracted-boyfriend) or path to template YAML")
    parser.add_argument("texts", nargs="+", help="Text for each slot")
    parser.add_argument("--layout", default=None, help="Layout preset (e.g. chest-label)")
    parser.add_argument("--backend", choices=["pillow", "magick"], default="pillow")
    parser.add_argument("--output", default="meme_output.jpg", help="Output file path")
    args = parser.parse_args()

    tmpl = _resolve_template(args.template)

    # Download image
    dest = tempfile.mktemp(suffix=".jpg", prefix="_meme_base_")
    img_path = download_image(tmpl["urls"], dest)
    if not img_path:
        print("Error: could not download image", file=sys.stderr)
        sys.exit(1)

    if args.backend == "pillow":
        render_pillow(tmpl, img_path, args.texts, args.layout, args.output)
    else:
        render_magick(tmpl, img_path, args.texts, args.layout, args.output)

    print(f"Saved: {args.output}")


if __name__ == "__main__":
    main()
