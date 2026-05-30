# AGENTS.md — awesome-meme

## Project Overview

awesome-meme is a pure-data meme template repository. It stores YAML metadata (no images) for meme generation. The `skill/` directory contains a self-contained renderer that downloads template data on demand.

## Architecture

```
awesome-meme/
├── AGENTS.md                   # This file — agent instructions
├── meme_index.yml              # Master index of all memes
├── templates/                  # Per-meme YAML with layouts, slots, coords
│   └── distracted_boyfriend.yml
├── skill/                      # Self-contained renderer (stable, no data)
│   ├── SKILL.md                # Entry point — usage, download, docs
│   ├── meme_render.py          # Python renderer (Pillow + ImageMagick)
│   ├── meme_render.sh          # Shell renderer (ImageMagick only)
│   ├── INSTALL.md              # Dependency installation
│   ├── PILLOW.md               # Pillow backend guide
│   └── IMAGE_MAGICK.md         # ImageMagick backend guide
├── .x-cmd/rule/                # Quality rules for skill/
└── README.md
```

## Key Principles

- **skill/ is stable** — renderer code changes rarely; template data updates independently
- **No images in repo** — only YAML metadata + URLs pointing to external image sources
- **Data lives in root** — meme_index.yml and templates/ are data the skill fetches at runtime
- **Docs in skill/** — all skill documentation stays inside skill/, split by topic

## When Adding a New Meme

1. Add entry to `meme_index.yml` with metadata, triggers, safety level, URLs
2. Create `templates/<meme_id>.yml` with layouts, slots, positions, font config
3. Test with `python3 skill/meme_render.py <meme-id> TEXT1 TEXT2`

## When Modifying the Skill

1. Run `x rule scan skill/` to check quality
2. Ensure both Pillow and ImageMagick backends still work
3. Keep SKILL.md concise — detailed docs go in INSTALL.md / PILLOW.md / IMAGE_MAGICK.md

## Quality Rules

Rules are in `.x-cmd/rule/`. Check with:

```bash
x rule scan skill/     # quick scan
x rule check skill/    # full compliance check
```
