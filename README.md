# awesome-meme

A curated list of internet meme templates for AI agents and developers.

Each meme has a YAML template with metadata, image URLs, and text slot layouts for automated meme generation.

## Structure

```
├── meme_index.yml          # Master index of all memes
├── templates/              # Per-meme template files with layouts
│   └── distracted_boyfriend.yml
└── README.md
```

## Usage

This is a data-only repository. No images are stored here — only YAML metadata and external URLs.

For the meme generation tool, see [x-bash/meme](https://github.com/x-cmd/x-bash) (x-cmd module).

## Template Format

Each meme template includes:
- **Metadata**: id, name, description, category
- **URLs**: Multiple image sources (Wikipedia, imgflip, etc.) with fallback
- **Font settings**: Default font family, size, color, stroke
- **Layouts**: Multiple text placement presets (chest, above-head, bottom)
- **Slots**: Named text positions with role descriptions

## Adding a Meme

1. Add entry to `meme_index.yml`
2. Create `templates/<meme_id>.yml` with layouts and coordinates
3. Submit a PR

## License

This repository contains only metadata (YAML) and external links. No copyrighted images are stored.

Meme images linked from external sources (Wikipedia, imgflip) are subject to their respective licenses and terms of use.
