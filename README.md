# awesome-meme

Meme template index for AI agents. YAML-only, no images.

## Structure

```
├── meme_index.yml              # Master index
├── templates/                  # Per-meme layout templates
│   └── distracted_boyfriend.yml
├── skill/                      # Render skill
│   ├── SKILL.md                # Full docs (install + Pillow + ImageMagick)
│   ├── meme_render.py          # Python renderer (Pillow + ImageMagick)
│   └── meme_render.sh          # Shell renderer (ImageMagick)
└── README.md
```

## Usage

Data-only repo. Use with [x-bash/meme](https://github.com/x-cmd/x-bash) module for generation.

## Adding a Meme

1. Add entry to `meme_index.yml`
2. Create `templates/<meme_id>.yml`
3. PR welcome
