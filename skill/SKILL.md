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

Generate meme images by overlaying text onto templates from [awesome-meme](https://github.com/edwinjhlee/awesome-meme). Pass a meme ID and the renderer fetches the spec YAML from GitHub automatically.

## Not installed? → [INSTALL.md](references/INSTALL.md)

## Quick Start

```bash
python3 scripts/meme_render.py distracted-boyfriend ZIG ME RUST
```

## Options

**Python** (`meme_render.py`):

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--backend` | pillow, magick | pillow | Rendering backend |
| `--layout` | chest-label, above-head, bottom-label | (spec default) | Text placement preset |
| `--output` | file path | meme_output.jpg | Output file path |

**Shell** (`meme_render.sh`):

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--output` | file path | meme_output.jpg | Output file path |

## Font selection

| Text language | Font used | Source |
|---|---|---|
| English / Latin | Impact (default) or Anton | macOS/Windows pre-installed; Linux needs install |
| Chinese / CJK | PingFang (macOS) / Noto Sans CJK (Linux) | System font |
| Mixed | Each slot auto-detected independently | — |

**Impact has no CJK glyphs** — Chinese text will be invisible (no error, just blank). The renderer auto-detects CJK characters and falls back to system CJK fonts. To override, set `font.path` in the spec YAML. On Linux, install CJK fonts: `apt install fonts-noto-cjk`.

## Backends

**Pillow** (default) — precise center-anchor coordinates → [PILLOW.md](references/PILLOW.md)
**ImageMagick** — no Python needed → [IMAGE_MAGICK.md](references/IMAGE_MAGICK.md)

```bash
python3 scripts/meme_render.py distracted-boyfriend ZIG ME RUST --backend magick
# Or pure shell (also supports meme IDs):
bash scripts/meme_render.sh distracted-boyfriend "ZIG" "ME" "RUST"
```

## Get the skill

```bash
git clone https://github.com/edwinjhlee/awesome-meme.git && cd awesome-meme/skill
# Or: curl -O https://raw.githubusercontent.com/edwinjhlee/awesome-meme/main/skill/scripts/meme_render.py
# Or via x-cmd: eval "$(curl https://get.x-cmd.com)"
```

## Docs

- [references/INSTALL.md](references/INSTALL.md) — Dependencies (Pillow, ImageMagick, fonts)
- [references/PILLOW.md](references/PILLOW.md) — Pillow backend: coordinates, programmatic usage
- [references/IMAGE_MAGICK.md](references/IMAGE_MAGICK.md) — ImageMagick backend: commands, coordinates
- [references/GUIDELINES.md](references/GUIDELINES.md) — AI agent usage, font selection, data structure
