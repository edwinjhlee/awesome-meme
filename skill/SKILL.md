# meme skill

Render meme images by overlaying text onto templates.

Templates (YAML) are stored in [awesome-meme](https://github.com/edwinjhlee/awesome-meme). The skill downloads template data on demand.

## Get the Skill

Option 1 — Download only the skill directory:

```bash
# Clone the repo and use skill/ directly
git clone https://github.com/edwinjhlee/awesome-meme.git
cd awesome-meme/skill
```

Option 2 — Download a single file (no git needed):

```bash
# Just the Python renderer
curl -O https://raw.githubusercontent.com/edwinjhlee/awesome-meme/main/skill/meme_render.py

# Or the shell renderer
curl -O https://raw.githubusercontent.com/edwinjhlee/awesome-meme/main/skill/meme_render.sh
```

Option 3 — Via x-cmd (recommended):

```bash
# Install x-cmd if not already available
eval "$(curl https://get.x-cmd.com)"
# See https://www.x-cmd.com/llms.txt for details

# Then use the meme module (coming soon)
x meme render distracted-boyfriend ZIG ME RUST
```

## Install Dependencies

See [INSTALL.md](INSTALL.md) for full details:

```bash
# Pillow (Python backend, recommended)
pip install pillow pyyaml

# Or ImageMagick
brew install imagemagick    # macOS
apt install imagemagick     # Linux
```

## Usage

```bash
# By meme ID (auto-downloads template from GitHub)
python3 meme_render.py distracted-boyfriend ZIG ME RUST

# By local template file
python3 meme_render.py /path/to/distracted_boyfriend.yml ZIG ME RUST

# ImageMagick backend
python3 meme_render.py distracted-boyfriend ZIG ME RUST --backend magick

# Pure shell (local template only)
bash meme_render.sh distracted_boyfriend.yml "ZIG" "ME" "RUST"
```

## Options

- `--layout` — chest-label (default), above-head, bottom-label
- `--backend` — pillow (default), magick
- `--output` — output file path (default: meme_output.jpg)

## How It Works

1. Skill (this directory) = renderer code only, stable
2. Template data = YAML files in [awesome-meme/templates/](https://github.com/edwinjhlee/awesome-meme/tree/main/templates), updated independently
3. When you use a meme ID (e.g. `distracted-boyfriend`), the renderer fetches the template from GitHub automatically

## Docs

- [INSTALL.md](INSTALL.md) — Dependency installation (Pillow, ImageMagick, fonts, x-cmd)
- [PILLOW.md](PILLOW.md) — Pillow backend usage and coordinate system
- [IMAGE_MAGICK.md](IMAGE_MAGICK.md) — ImageMagick backend usage and coordinate conversion
