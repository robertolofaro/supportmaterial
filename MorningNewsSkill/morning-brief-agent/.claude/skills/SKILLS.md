# Skill: Morning Brief Intelligence Agent

## Command
/morning-brief

## Purpose
Generate a daily geopolitical, economic, and technology intelligence briefing
using a structured multi-analyst model.

## Execution
When invoked:
1. Load prompt from `/prompts/morning_brief_prompt.md`
2. Inject current date
3. Execute with web access enabled
4. Output strict Markdown briefing

## Output Rules
- Must follow exact structure defined in prompt
- Must include URLs
- Must remain under ~1,200 words unless necessary
- Must not hallucinate sources

## Schedule
Intended for automated daily execution at:
08:00 CET

## Notes
- Uses multi-analyst persona system
- Requires fresh news (last 24h)
- Output is saved externally (not by skill itself)
