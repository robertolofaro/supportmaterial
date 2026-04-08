#!/usr/bin/env bash

set -e

DATE=$(date +"%Y-%m-%d")
DATE_FILE=$(date +"%Y%m%d")
MODEL="claude-3-opus"   # change if needed

OUTPUT_FILE="output/MorningNews_${DATE_FILE}_${MODEL}.md"

PROMPT=$(sed "s/{{DATE}}/${DATE}/g" prompts/morning_brief_prompt.md)

echo "Running Morning Brief for $DATE..."

# Example using Claude CLI (adjust if using API)
claude chat \
  --model $MODEL \
  --system "$PROMPT" \
  --output-format markdown \
  > "$OUTPUT_FILE"

echo "Saved to $OUTPUT_FILE"
