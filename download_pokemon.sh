#!/usr/bin/env bash

set -euo pipefail

URL="https://pokemondb.net/sprites"
OUTPUT_DIR="pokemon_gen1"

mkdir -p "$OUTPUT_DIR"

curl -L -s "$URL" |
grep -o 'https://img.pokemondb.net/sprites/scarlet-violet/icon/[a-z0-9-]*\.png' |
head -151 |
while read -r img_url; do

    filename=$(basename "$img_url")

    echo "→ Download $filename"

    curl -L -s "$img_url" \
        -o "$OUTPUT_DIR/$filename"

done

echo "Download finished."
