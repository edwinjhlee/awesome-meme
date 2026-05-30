# Install Dependencies

## Pillow (Python)

```bash
pip install pillow pyyaml
```

Or via x-cmd:

```bash
x env use python   # ensure Python available
pip install pillow pyyaml
```

## ImageMagick

### macOS

```bash
brew install imagemagick
```

Or via x-cmd:

```bash
x pixi use imagemagick
```

### Linux

```bash
apt install imagemagick    # Debian/Ubuntu
dnf install imagemagick    # Fedora
```

## Font

Impact is recommended (classic meme font).

- macOS: `/System/Library/Fonts/Supplemental/Impact.ttf` (pre-installed)
- Linux: Install `ttf-mscorefonts-installer` or use Google Fonts Anton/Bangers as free alternatives
- Windows: `C:\Windows\Fonts\impact.ttf` (pre-installed)
