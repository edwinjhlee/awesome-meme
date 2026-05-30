# awesome-meme

Meme template index for AI agents. YAML-only, no images.

## What is this

A curated collection of meme templates stored as structured YAML data. Each meme has:

- Metadata (name, category, triggers, safety level)
- Multiple image source URLs (fallback support)
- Render specs with text slot positions, layouts, and font configuration

The `skill/` directory provides a self-contained renderer that downloads specs on demand.

## Structure

```
awesome-meme/
├── data/
│   ├── meme_index.yml          # Master index (27 memes)
│   └── spec/                   # Per-meme render specifications
│       └── distracted_boyfriend.yml
├── skill/                      # Self-contained renderer
│   ├── SKILL.md                # Skill entry point
│   ├── meme_render.py          # Python renderer (Pillow + ImageMagick)
│   ├── meme_render.sh          # Shell renderer (ImageMagick)
│   ├── INSTALL.md              # Dependency installation
│   ├── PILLOW.md               # Pillow backend guide
│   └── IMAGE_MAGICK.md         # ImageMagick backend guide
├── AGENTS.md                   # Agent instructions
├── CONTRIBUTING.md             # How to contribute
├── .x-cmd/rule/                # Quality rules
└── README.md
```

## Quick Start

```bash
# Install dependencies
pip install pillow pyyaml

# Generate a meme (auto-downloads spec from GitHub)
python3 skill/meme_render.py distracted-boyfriend ZIG ME RUST
```

See [skill/SKILL.md](skill/SKILL.md) for full documentation.

## Design Principles

- **Pure data** — only YAML files and URLs, no images stored in repo
- **Skill/data separation** — renderer is stable, specs update independently
- **Multiple backends** — Pillow (Python) and ImageMagick (shell)
- **Fallback URLs** — each meme provides multiple image sources
- **MIT licensed** — free to use and contribute

## Safety

Meme entries are classified by safety level:

| Level | Description | Ratio target |
|-------|-------------|-------------|
| P0 | Text/ASCII only | — |
| P1 | External image links | majority |
| P2 | Celebrity/media | ≤20% |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add new memes.

## License

[MIT](LICENSE)
