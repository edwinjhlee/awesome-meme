# Contributing to awesome-meme

Help us grow the meme collection! This repo stores YAML metadata and a renderer — no images.

## Quick Add (3 steps)

### Step 1: Add to the index

Edit `data/index.yml`, append an entry:

```yaml
  - id: your-meme-id
    name: Your Meme Name
    name_zh: 中文名
    lang: en|zh
    category: programmer|general
    meaning: One-line description of the meme's meaning
    meaning_zh: 一句话描述这个梗的含义
    triggers_en: keyword1|keyword2|keyword3
    triggers_zh: 关键词1|关键词2
    url_wikipedia: https://upload.wikimedia.org/...
    safety: P1
    alt: Description of the meme image for accessibility
```

**Field reference:**

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | kebab-case identifier, must match spec filename |
| `name` | yes | English name |
| `name_zh` | no | Chinese name |
| `lang` | yes | `en`, `zh`, or `en\|zh` |
| `category` | yes | `programmer`, `general`, or both (`\|` separated) |
| `meaning` | yes | What the meme expresses |
| `meaning_zh` | if lang has zh | Chinese meaning |
| `triggers_en` | if lang has en | Pipe-separated trigger words for matching |
| `triggers_zh` | if lang has zh | Chinese trigger words |
| `url_wikipedia` | preferred | Wikipedia/Wikimedia image URL |
| `url_imgflip` | optional | imgflip template URL as fallback |
| `url_moegirl` | optional | Chinese wiki source |
| `safety` | yes | P0 (text), P1 (image links), P2 (celebrity ≤20%) |
| `alt` | yes | Accessibility description of the image |

### Step 2: Create a render spec

Create `data/spec/your-meme-id.yml`:

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

**Layout types:**

- `top-bottom` — classic meme, text above and below image
- `reject-accept` — two-panel (like Drake), reject on top, accept on bottom
- `four-panel` — progressive (like Expanding Brain), 4 slots
- `chest-label` — labels on characters (like Distracted Boyfriend)
- `text-only` — no image needed, ASCII art or pure text

**Coordinate tips:**
- Positions are center coordinates (`anchor: mm`)
- Origin is top-left (0, 0), Y increases downward
- Top text: ~10-15% from top edge
- Bottom text: ~85-90% from top edge
- Use `identify image.jpg` or `sips -g pixelWidth -g pixelHeight image.jpg` to get dimensions

### Step 3: Test and submit

```bash
# Test locally
python3 skill/meme_render.py your-meme-id "TEXT1" "TEXT2"

# Verify the output looks good, then submit a PR
```

## Safety Guidelines

| Level | Description | Examples |
|-------|-------------|---------|
| **P0** | Text/ASCII only, no image | Table Flip, Shrug, LGTM |
| **P1** | External image links | Drake, This is Fine, Success Kid |
| **P2** | Celebrity or media content | 真香, 葛优躺 |

- P2 entries must stay ≤20% of total
- No NSFW content
- No hateful or discriminatory memes

## URL Guidelines

- **Wikipedia/Wikimedia preferred** — stable, legally clear
- Provide **multiple URLs** when possible (fallback against dead links)
- imgflip URLs are acceptable but may be rate-limited
- Never upload images to this repo

## PR Checklist

- [ ] `data/index.yml` updated with new entry
- [ ] `data/spec/<meme-id>.yml` created with valid YAML
- [ ] `example.texts` produces a funny/relevant test meme
- [ ] Tested with `python3 skill/meme_render.py <meme-id> ...`
- [ ] No images committed to repo
- [ ] Safety level correctly assigned

## Reporting Issues

- **Dead image link** — report the meme ID and suggest a replacement URL
- **Wrong coordinates** — include a screenshot showing the text placement issue
- **Missing meme** — open an issue with the meme name and a source URL
