# Pillow Backend

## Usage

```bash
python3 skill/meme_render.py distracted-boyfriend ZIG ME RUST
```

## Programmatic Usage

```python
from PIL import Image, ImageDraw, ImageFont

img = Image.open("base_image.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Impact.ttf", 48)

draw.text(
    (170, 323), "ZIG",
    font=font, fill="white",
    stroke_width=4, stroke_fill="black",
    anchor="mm"
)

img.save("output.jpg", quality=95)
img.save("output.webp", "WEBP", quality=90)
```

## Coordinates

Pillow uses **center coordinates** with `anchor="mm"` (middle-middle):
- `pos: [170, 323]` = text center at pixel (170, 323)
- Origin: top-left = (0, 0), Y increases downward

## Font Notes

- Impact: classic meme font, macOS pre-installed
- Free alternatives: Google Fonts Anton, Bangers
- Chinese: Noto Sans CJK (思源黑体)
