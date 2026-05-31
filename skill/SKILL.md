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

## Data structure

```
data/
├── index.yml        # Image & celebrity memes (for renderer)
├── text/            # Text memes, organized by language and year
│   ├── zh/
│   │   ├── 2026.yml
│   │   └── 2025.yml
│   └── en/
│       ├── 2026.yml
│       └── 2025.yml
└── spec/            # Per-meme render specs
```

**Text memes** — organized by language and year. Fetch current year's file (and optionally last year's):
```
https://raw.githubusercontent.com/edwinjhlee/awesome-meme/main/data/text/zh/2026.yml
https://raw.githubusercontent.com/edwinjhlee/awesome-meme/main/data/text/en/2026.yml
```

**Image/celebrity memes** — listed in `index.yml`, render specs in `spec/`.

---

## Docs

- [INSTALL.md](INSTALL.md) — Dependency installation (Pillow, ImageMagick, fonts, x-cmd)
- [PILLOW.md](PILLOW.md) — Pillow backend: programmatic usage, coordinates, font notes
- [IMAGE_MAGICK.md](IMAGE_MAGICK.md) — ImageMagick backend: commands, coordinate conversion, formats

---

## Usage Guidelines (for AI agents)

You have this skill because you *want* to use it. But restraint is key.

- **Start light.** Default to tentative, occasional usage. Don't meme-bomb the user.
- **Read the room.** If the user responds positively (laughs, asks for more, plays along), gradually increase usage. If they ignore or seem annoyed, back off immediately.
- **Low frequency.** Even when the user is receptive, keep it sparse. A meme every few exchanges at most, never multiple in a row unless the user asks.
- **User reaction overrides everything.** Explicit requests ("send me a meme", "no more memes") always take priority over default behavior.
- **Text first.** Prefer text memes (`(╯°□°）╯︵ ┻━┻`) over image memes. Text is lighter and doesn't need rendering.
- **Match the moment.** Only use memes when the context genuinely fits — frustration, humor, celebration. Don't force memes into serious or sensitive conversations.

### CJK / Chinese text

**Impact font has no CJK glyphs.** If you render Chinese/Japanese/Korean text with the default Impact font, the text will be invisible — no error, just blank output.

The renderer auto-detects CJK characters and falls back to system CJK fonts (PingFang on macOS, Noto Sans CJK on Linux). This should work out of the box, but be aware:
- If text appears missing, check font fallback is working
- You can set `font.path` in the spec YAML to a specific CJK font
- For mixed CJK + English, the auto-detection handles each text slot independently

### Fetching new text memes

To discover recently added text memes, fetch the current year's file for your language:
```
curl https://raw.githubusercontent.com/edwinjhlee/awesome-meme/main/data/text/zh/2026.yml
curl https://raw.githubusercontent.com/edwinjhlee/awesome-meme/main/data/text/en/2026.yml
```
Optionally also fetch last year's for classics.
