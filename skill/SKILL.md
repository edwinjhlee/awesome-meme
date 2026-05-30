# meme skill

Generate meme images by overlaying text onto templates.

## Quick Start

```bash
# Pillow backend (recommended)
python3 skill/meme_render.py templates/distracted_boyfriend.yml ZIG ME RUST

# ImageMagick backend
python3 skill/meme_render.py templates/distracted_boyfriend.yml ZIG ME RUST --backend magick

# Pure shell
bash skill/meme_render.sh templates/distracted_boyfriend.yml "ZIG" "ME" "RUST"
```

## Options

- `--layout` — chest-label (default), above-head, bottom-label
- `--backend` — pillow (default), magick
- `--output` — output file path

See [doc/INSTALL.md](doc/INSTALL.md) for dependency installation.
