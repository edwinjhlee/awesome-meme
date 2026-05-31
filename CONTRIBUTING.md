# Contributing to awesome-meme

> Also available: [Code of Conduct](CODE_OF_CONDUCT.md) | [Security](SECURITY.md) | [License](LICENSE) | [README](README.md)

Help us grow the meme collection! This repo stores YAML metadata and a renderer — no images.

## Quick Add (3 steps)

### Step 1: Add to the index

Edit `data/index.yml`, append an entry under `memes:`:

```yaml
  - id: your-meme-id
    name: Your Meme Name
    name_zh: 中文名
    type: image
    meaning: One-line description of the meme's meaning
    meaning_zh: 一句话描述这个梗的含义
```

**Field reference:**

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | kebab-case identifier (e.g. `distracted-boyfriend`) |
| `name` | yes | English name |
| `name_zh` | no | Chinese name |
| `type` | yes | `image` or `celebrity` |
| `meaning` | yes | What the meme expresses |
| `meaning_zh` | no | Chinese meaning |

Note: Text/ASCII memes (e.g. `(╯°□°）╯︵ ┻━┻`) go in `data/text/{zh,en}/{year}.yml`, not in index.yml.

### Step 2: Create a render spec

Create `data/spec/your_meme_id.yml` (use underscores in filename):

```yaml
id: your-meme-id
image_size: [width, height]
urls:
  - src: wikipedia
    url: https://upload.wikimedia.org/...
font:
  family: Impact
  size: 36
  color: white
  stroke_color: black
  stroke_width: 3
  anchor: mm
layouts:
  - id: top-bottom
    default: true
    desc: "Classic top/bottom text format"
    slots:
      - id: top
        role: "what goes here"
        role_zh: "中文说明"
        pos: [x_center, y_center]
      - id: bottom
        role: "what goes here"
        role_zh: "中文说明"
        pos: [x_center, y_center]
example:
  texts: ["Top text example", "Bottom text example"]
```

**Naming:** spec files use underscores (`distracted_boyfriend.yml`), index IDs use hyphens (`distracted-boyfriend`). The renderer auto-resolves both.

**Layout types:**

- `top-bottom` — classic meme, text above and below image
- `reject-accept` — two-panel (like Drake), reject on top, accept on bottom
- `four-panel` — progressive (like Expanding Brain), 4 slots
- `chest-label` — labels on characters (like Distracted Boyfriend)

**Coordinate tips:**
- Positions are center coordinates (`anchor: mm`)
- Origin is top-left (0, 0), Y increases downward
- Top text: ~10-15% from top edge
- Bottom text: ~85-90% from top edge
- Use `identify image.jpg` or `sips -g pixelWidth -g pixelHeight image.jpg` to get dimensions

**CJK text:** Impact has no CJK glyphs — Chinese text will be invisible. The renderer auto-detects CJK and falls back to system fonts (PingFang/Noto Sans CJK). See [skill/SKILL.md](skill/SKILL.md) for details.

### Step 3: Test and submit

```bash
# Test locally (renderer auto-fetches spec + image)
python3 skill/meme_render.py your-meme-id "TEXT1" "TEXT2"

# Verify the output looks good, then submit a PR
```

### Step 3b: Regenerate TSV

After editing `data/index.yml`, regenerate the TSV:

```bash
bash .x-cmd/yml2tsv
```

## URL Guidelines

- **Wikipedia/Wikimedia preferred** — stable, legally clear
- Provide **multiple URLs** when possible (fallback against dead links)
- imgflip URLs are acceptable but may be rate-limited
- Never upload images to this repo

## PR Checklist

- [ ] `data/index.yml` updated with new entry
- [ ] `data/spec/your_meme_id.yml` created with valid YAML (underscores in filename)
- [ ] `data/index.tsv` regenerated via `.x-cmd/yml2tsv`
- [ ] `example.texts` produces a funny/relevant test meme
- [ ] Tested with `python3 skill/meme_render.py <meme-id> ...`
- [ ] No images committed to repo

## Reporting Issues

- **Dead image link** — report the meme ID and suggest a replacement URL
- **Wrong coordinates** — include a screenshot showing the text placement issue
- **Missing meme** — open an issue with the meme name and a source URL
