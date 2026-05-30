# meme skill

Generate meme images by overlaying text onto templates.

## Quick Start

```bash
# Pillow backend (recommended)
python3 skill/meme_render.py templates/distracted_boyfriend.yml ZIG ME RUST

# ImageMagick backend
python3 skill/meme_render.py templates/distracted_boyfriend.yml ZIG ME RUST --backend magick

# Pure shell (ImageMagick only)
bash skill/meme_render.sh templates/distracted_boyfriend.yml "ZIG" "ME" "RUST"
```

## Options

- `--layout` — chest-label (default), above-head, bottom-label
- `--backend` — pillow (default), magick
- `--output` — output file path

## Install Dependencies

### Pillow (Python)

```bash
pip install pillow pyyaml
```

Or via x-cmd:

```bash
x env use python
pip install pillow pyyaml
```

### ImageMagick

macOS:

```bash
brew install imagemagick
```

Or via x-cmd:

```bash
x pixi use imagemagick
```

Linux:

```bash
apt install imagemagick    # Debian/Ubuntu
dnf install imagemagick    # Fedora
```

### Font

Impact is recommended (classic meme font).

- macOS: `/System/Library/Fonts/Supplemental/Impact.ttf` (pre-installed)
- Linux: `ttf-mscorefonts-installer` or Google Fonts Anton/Bangers
- Windows: `C:\Windows\Fonts\impact.ttf` (pre-installed)
- Chinese: Noto Sans CJK (思源黑体)

## Pillow Backend

### Programmatic Usage

```python
from PIL import Image, ImageDraw, ImageFont

img = Image.open("base_image.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Impact.ttf", 48)

draw.text(
    (170, 323), "ZIG",
    font=font, fill="white",
    stroke_width=4, stroke_fill="black",
    anchor="mm"  # center-center anchor
)

img.save("output.jpg", quality=95)
img.save("output.webp", "WEBP", quality=90)
```

### Coordinates

Pillow uses **center coordinates** with `anchor="mm"` (middle-middle):
- `pos: [170, 323]` = text center at pixel (170, 323)
- Origin: top-left = (0, 0), Y increases downward

## ImageMagick Backend

### Direct magick command

```bash
magick base.jpg \
  -colorspace sRGB \
  -font Impact -pointsize 48 \
  -fill white -stroke black -strokewidth 4 \
  -draw "text 140,340 'ZIG'" \
  -draw "text 400,280 'ME'" \
  -draw "text 595,370 'RUST'" \
  output.jpg
```

### Coordinates

ImageMagick `-draw "text x,y"` uses **left-baseline** anchor:
- x,y = left edge of text + baseline position
- Convert from center: `im_x = center_x - text_width/2`
- Convert from center: `im_y = center_y + font_size * 0.35`

Coordinate conversion table:

| Pillow (anchor=mm) | ImageMagick (-draw) |
|---------------------|---------------------|
| center coords       | left-baseline coords |
| `(170, 323)`       | `(140, 340)`        |
| `(427, 263)`       | `(400, 280)`        |
| `(645, 353)`       | `(595, 370)`        |

### Formats

```bash
magick input.jpg -quality 90 output.jpg      # JPEG
magick input.jpg -quality 90 output.webp     # WebP (~58% smaller)
magick input.jpg output.png                   # PNG
```
