# awesome-meme

> Make your AI agent tell memes. A curated collection of 27 meme render specs, growing with community contributions.

## Why

AI agents can generate text, but they can't *meme*. awesome-meme gives any AI agent the ability to create and share meme images — from classic programmer jokes to Chinese internet culture.

**One line to meme:**

```bash
python3 meme_render.py distracted-boyfriend ZIG ME RUST
```

## What's inside

- `data/meme_index.yml` — searchable index with triggers, categories, safety levels
- `data/spec/` — per-meme render specs: image source, text slots, coordinates, layouts
- `skill/` — self-contained renderer (Pillow + ImageMagick), stable and independent of data

## Quick Start

```bash
# Install
pip install pillow pyyaml

# Generate a meme by ID (auto-downloads spec + image)
python3 meme_render.py drake-hotline-bling "Debugging with print" "Debugging with debugger"

# List available memes
grep 'id:' data/meme_index.yml
```

See [skill/SKILL.md](skill/SKILL.md) for full docs.

## Memes

| Meme | Category | Safety |
|------|----------|--------|
| Distracted Boyfriend | programmer, general | P1 |
| Drake Hotline Bling | programmer, general | P1 |
| This is Fine | programmer | P1 |
| Success Kid | programmer, general | P1 |
| Roll Safe | programmer, general | P1 |
| Expanding Brain | programmer, general | P1 |
| Woman Yelling at Cat | programmer, general | P1 |
| Hide the Pain Harold | programmer, general | P1 |
| Doge | programmer, general | P1 |
| Nyan Cat | general | P1 |
| How to Exit Vim | programmer | P0 |
| Table Flip (╯°□°）╯︵ ┻━┻ | programmer | P0 |
| Shrug ¯\\_(ツ)_/¯ | programmer, general | P0 |
| LGTM | programmer | P0 |
| Bug → Feature | programmer | P1 |
| Monday Deploy | programmer | P1 |
| Stack Overflow Copy | programmer | P1 |
| WTFs Per Minute | programmer | P1 |
| Code Review Guy | programmer | P1 |
| It Works Why | programmer | P1 |
| Panda Head Cry | programmer | P0 |
| Panda Head Doge | programmer | P0 |
| Panda Head Overtime | programmer | P0 |
| Programmer Tea | programmer | P0 |
| 真香 (Zhen Xiang) | general | P2 |
| 葛优躺 (Ge You Tang) | general | P2 |
| 鸭屎啦你 (Ya Shi La Nei) | general | P2 |

**27 memes now. Goal: 1000 with community help.**

## Vision

1. **skill** — a stable renderer that any agent can download and use
2. **1000 meme specs** — crowdsourced from the community, one YAML per meme
3. **Every AI agent can meme** — OpenClaw, Claude Code, Codex, Cursor, any tool

## Design Principles

- **Pure data** — only YAML, no images in repo
- **Skill/data separation** — renderer rarely changes, specs grow independently
- **Fallback URLs** — multiple image sources per meme to avoid dead links
- **MIT licensed** — free to use and contribute

## Safety

| Level | Description | Ratio |
|-------|-------------|-------|
| P0 | Text/ASCII only, no images | unlimited |
| P1 | External image links | majority |
| P2 | Celebrity/media | ≤20% |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — add a meme in 3 steps.

## License

[MIT](LICENSE)
