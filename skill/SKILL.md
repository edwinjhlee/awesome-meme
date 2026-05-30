# meme skill

Generate meme images by overlaying text onto meme templates.

## Dependencies

- Pillow backend: `pip install pillow pyyaml`
- ImageMagick backend: `magick` command available in PATH

## Usage

### Python (Pillow)

```bash
python3 skill/meme_render.py templates/distracted_boyfriend.yml ZIG ME RUST
python3 skill/meme_render.py templates/distracted_boyfriend.yml ZIG ME RUST --layout above-head
python3 skill/meme_render.py templates/distracted_boyfriend.yml ZIG ME RUST --backend magick
python3 skill/meme_render.py templates/distracted_boyfriend.yml ZIG ME RUST --output my_meme.webp
```

### Shell (ImageMagick only)

```bash
bash skill/meme_render.sh templates/distracted_boyfriend.yml "ZIG" "ME" "RUST" --output meme.jpg
```

## Options

- `--layout` — Layout preset: chest-label (default), above-head, bottom-label
- `--backend` — Renderer: pillow (default), magick
- `--output` — Output file path (default: meme_output.jpg)

## Adding Templates

Create `templates/<meme_id>.yml` following the existing format. Required fields:
- `id`, `name`, `image_size`, `urls`, `font`, `layouts` with `slots`
