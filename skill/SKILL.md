# meme skill

Render meme images by overlaying text onto templates.

Templates (YAML) are stored in [awesome-meme](https://github.com/edwinjhlee/awesome-meme). The skill downloads template data on demand.

## Quick Start

```bash
# By meme ID (auto-downloads template from GitHub)
python3 skill/meme_render.py distracted-boyfriend ZIG ME RUST

# By local template file
python3 skill/meme_render.py /path/to/distracted_boyfriend.yml ZIG ME RUST

# ImageMagick backend
python3 skill/meme_render.py distracted-boyfriend ZIG ME RUST --backend magick

# Pure shell (local template only)
bash skill/meme_render.sh distracted_boyfriend.yml "ZIG" "ME" "RUST"
```

## Options

- `--layout` — chest-label (default), above-head, bottom-label
- `--backend` — pillow (default), magick
- `--output` — output file path (default: meme_output.jpg)

## Docs

- [INSTALL.md](INSTALL.md) — Dependency installation (Pillow, ImageMagick, fonts)
- [PILLOW.md](PILLOW.md) — Pillow backend usage and coordinate system
- [IMAGE_MAGICK.md](IMAGE_MAGICK.md) — ImageMagick backend usage and coordinate conversion
