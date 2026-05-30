#!/usr/bin/env bash
# meme_render.sh — ImageMagick-based meme renderer
# Usage: ./meme_render.sh <template.yml> "TEXT1" "TEXT2" "TEXT3" [--layout chest-label] [--output out.jpg]

set -euo pipefail

TEMPLATE="${1:?Usage: meme_render.sh <template.yml> TEXT1 TEXT2 TEXT3 [--layout id] [--output path]}"
shift

TEXTS=()
LAYOUT=""
OUTPUT="meme_output.jpg"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --layout) LAYOUT="$2"; shift 2 ;;
        --output) OUTPUT="$2"; shift 2 ;;
        *) TEXTS+=("$1"); shift ;;
    esac
done

# Parse YAML (simple grep-based, no python dependency)
get_yaml_val() {
    local key="$1" file="$2"
    grep -A100 "^${key}:" "$file" | head -1 | sed "s/^${key}: *//" | tr -d '"' | tr -d "'"
}

FONT_FAMILY=$(get_yaml_val "family" "$TEMPLATE" || echo "Impact")
FONT_SIZE=$(get_yaml_val "size" "$TEMPLATE" || echo "48")
STROKE_W=$(get_yaml_val "stroke_width" "$TEMPLATE" || echo "4")
FILL=$(get_yaml_val "color" "$TEMPLATE" || echo "white")
STROKE=$(get_yaml_val "stroke_color" "$TEMPLATE" || echo "black")

# Find the first URL
URL=$(grep "url:" "$TEMPLATE" | head -1 | sed 's/.*url: *//' | tr -d '"' | tr -d "'")
BASE_IMG="/tmp/_meme_base_$$.jpg"
curl -sL -o "$BASE_IMG" "$URL" 2>/dev/null || { echo "Failed to download image"; exit 1; }

# Build magick command
CMD=("magick" "$BASE_IMG" "-colorspace" "sRGB")

# Get slot positions from template (simplified: read first 3 slots)
SLOT_POS=()
for i in 0 1 2; do
    POS=$(grep "- pos:" "$TEMPLATE" | sed -n "$((i+1))p" | sed 's/.*pos: *\[//' | sed 's/\].*//')
    [[ -z "$POS" ]] && break
    SLOT_POS+=("$POS")
done

for i in "${!TEXTS[@]}"; do
    [[ -z "${SLOT_POS[$i]:-}" ]] && break
    IFS=',' read -r CX CY <<< "${SLOT_POS[$i]}"
    # Convert center coords to left-baseline for ImageMagick
    IM_X=$((CX - ${#TEXTS[$i]} * FONT_SIZE / 4))
    IM_Y=$((CY + FONT_SIZE * 35 / 100))

    CMD+=(
        "-font" "$FONT_FAMILY"
        "-pointsize" "$FONT_SIZE"
        "-fill" "$FILL"
        "-stroke" "$STROKE"
        "-strokewidth" "$STROKE_W"
        "-draw" "text ${IM_X},${IM_Y} '${TEXTS[$i]}'"
    )
done

CMD+=("$OUTPUT")
"${CMD[@]}"
rm -f "$BASE_IMG"
echo "Saved: $OUTPUT"
