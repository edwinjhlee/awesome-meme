# Install Dependencies

## x-cmd (optional)

[x-cmd](https://www.x-cmd.com) provides portable package management without sudo.

Install:

```bash
eval "$(curl https://get.x-cmd.com)"
```

See [x-cmd.com/llms.txt](https://www.x-cmd.com/llms.txt) for details.

## Pillow (Python)

```bash
pip install pillow pyyaml
```

Or via x-cmd:

```bash
x env use python
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
- Linux: `ttf-mscorefonts-installer` or Google Fonts Anton/Bangers
- Windows: `C:\Windows\Fonts\impact.ttf` (pre-installed)
- Chinese: Noto Sans CJK (思源黑体)
