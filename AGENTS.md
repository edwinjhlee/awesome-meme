# AGENTS.md — awesome-meme

## Project Overview

awesome-meme is a pure-data meme template repository. It stores YAML metadata (no images) for meme generation. The `skill/` directory contains a self-contained renderer that downloads template data on demand.

## Architecture

```
awesome-meme/
├── AGENTS.md                   # This file — agent instructions
├── data/
│   ├── index.yml               # Image & celebrity memes
│   ├── text/                   # Text memes, organized by language and year
│   │   ├── zh/                 # Chinese text memes
│   │   │   ├── 2026.yml
│   │   │   └── 2025.yml
│   │   └── en/                 # English text memes
│   │       ├── 2026.yml
│   │       └── 2025.yml
│   └── spec/                   # Per-meme render specs
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
- **Data lives in data/** — text memes by year in `text/`, image memes in `index.yml`, specs in `spec/`
- **Docs in skill/** — all skill documentation stays inside skill/, split by topic
- **No triggers needed** — LLMs already know when to use memes; index is for cataloging and discovery

## Data Structure

- **data/text/{zh,en}/*.yml** — text memes organized by language and year. Agents fetch current year (and optionally last year).
- **data/index.yml** — image and celebrity memes only
- **data/spec/*.yml** — render specs for image/celebrity memes

## When Adding a New Meme

1. **Text meme**: add to `data/text/{lang}/{current_year}.yml` with id, name, meaning, output
2. **Image/celebrity meme**: add to `data/index.yml` and create `data/spec/<meme_id>.yml`
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

## Default Usage Behavior

These guidelines apply when an AI agent has this skill installed. The user installed it because they *want* memes — but restraint is key.

- **Start light.** Default to tentative, occasional usage. Don't meme-bomb the user.
- **Read the room.** If the user responds positively (laughs, asks for more, plays along), gradually increase usage. If they ignore or seem annoyed, back off immediately.
- **Low frequency.** Even when the user is receptive, keep it sparse. A meme every few exchanges at most, never multiple in a row unless the user asks.
- **User reaction overrides everything.** Explicit requests ("send me a meme", "no more memes") always take priority over default behavior.
- **Text first.** When choosing a meme, prefer text-type (e.g. `(╯°□°）╯︵ ┻━┻`) over image-type. Text memes are lighter and don't require rendering.
- **Match the moment.** Only use memes when the context genuinely fits — frustration, humor, celebration. Don't force a meme into a serious or sensitive conversation.
