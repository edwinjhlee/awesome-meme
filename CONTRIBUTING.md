# Contributing

Contributions welcome! This repo stores YAML data only — no images.

## Adding a New Meme

### 1. Add to index

Edit `data/meme_index.yml`, append an entry:

```yaml
- id: your-meme-id
  name: Your Meme Name
  category: reaction
  triggers: ["keyword1", "keyword2"]
  safety: P1
  urls:
    - src: wikipedia
      url: https://upload.wikimedia.org/...
```

### 2. Create render spec

Create `data/spec/your-meme-id.yml`:

```yaml
id: your-meme-id
image_size: [800, 600]
urls:
  - src: wikipedia
    url: https://...
font:
  family: Impact
  size: 48
  color: white
  stroke_color: black
  stroke_width: 4
  anchor: mm
layouts:
  - id: chest-label
    default: true
    desc: "Description of this layout"
    slots:
      - id: slot1
        role: "what this slot represents"
        pos: [400, 300]
```

### 3. Test

```bash
python3 skill/meme_render.py your-meme-id TEXT1 TEXT2
```

### 4. Submit

Open a pull request with both files changed.

## Safety Levels

- **P0** — Text/ASCII only, safest
- **P1** — External image links, moderate
- **P2** — Celebrity/media content (keep ≤20% of total entries)

## Guidelines

- **No images in repo** — only YAML metadata and URLs
- **Multiple URLs per meme** — provide fallback sources to avoid dead links
- **Test coordinates** — verify text placement with the renderer before submitting
- **One meme per PR** — easier to review

## Reporting Issues

- Dead image links — report the meme ID and suggest a replacement URL
- Wrong coordinates — include a screenshot showing the issue
