---
name: meme
description: |
  Generate meme images by overlaying text onto templates.
  Supports Pillow (Python) and ImageMagick backends.
  Templates are fetched on demand from the awesome-meme data repo.
  Use for "meme", "meme generator", "text overlay", "distracted boyfriend", "image macro".

metadata:
  version: "0.1.0"
  category: image
  tags: [meme, image, text-overlay, pillow, imagemagick]
  repository: https://github.com/edwinjhlee/awesome-meme
---

# meme skill

Generate meme images by overlaying text onto templates.

Templates are stored in [awesome-meme](https://github.com/edwinjhlee/awesome-meme) and fetched on demand.

---

## Not installed? → [INSTALL.md](INSTALL.md)

---

## Quick Start

```bash
# By meme ID (auto-downloads spec from GitHub)
python3 meme_render.py distracted-boyfriend ZIG ME RUST

# By local spec file
python3 meme_render.py /path/to/distracted_boyfriend.yml ZIG ME RUST
```

---

## Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--backend` | pillow, magick | pillow | Rendering backend |
| `--layout` | chest-label, above-head, bottom-label | chest-label | Text placement preset |
| `--output` | file path | meme_output.jpg | Output file path |

---

## Two backends

**Pillow** (recommended) — Python, precise center-anchor coordinates:

```bash
pip install pillow pyyaml
python3 meme_render.py distracted-boyfriend ZIG ME RUST
```

→ See [PILLOW.md](PILLOW.md) for programmatic usage and coordinate system.

**ImageMagick** — Shell, no Python needed:

```bash
python3 meme_render.py distracted-boyfriend ZIG ME RUST --backend magick
# Or pure shell
bash meme_render.sh distracted_boyfriend.yml "ZIG" "ME" "RUST"
```

→ See [IMAGE_MAGICK.md](IMAGE_MAGICK.md) for direct magick commands and coordinate conversion.

---

## Get the skill

```bash
# Option 1: Clone
git clone https://github.com/edwinjhlee/awesome-meme.git
cd awesome-meme/skill

# Option 2: Single file (no git)
curl -O https://raw.githubusercontent.com/edwinjhlee/awesome-meme/main/skill/meme_render.py

# Option 3: x-cmd
eval "$(curl https://get.x-cmd.com)"
# See https://www.x-cmd.com/llms.txt
```

---

## How it works

1. **skill/** = renderer code, stable and rarely changes
2. **data/spec/** = per-meme render specs (layouts, slots, positions), updated independently
3. When you pass a meme ID, the renderer fetches the spec YAML from GitHub automatically

---

## Docs

- [INSTALL.md](INSTALL.md) — Dependency installation (Pillow, ImageMagick, fonts, x-cmd)
- [PILLOW.md](PILLOW.md) — Pillow backend: programmatic usage, coordinates, font notes
- [IMAGE_MAGICK.md](IMAGE_MAGICK.md) — ImageMagick backend: commands, coordinate conversion, formats
