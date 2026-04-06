# MY REQUEST

could you kindly produce a downlodable manual containing:
1. Claude Skills suggested best practices
2. usage of npx skills agent-skill-creator ?

thanks

# GEMINI ANSWER


This manual provides the 2026 standard for developing and deploying **Claude Skills** (also known as Agent Skills). It covers the architectural best practices recognized by Anthropic and the usage of the official scaffolding utility.

---

# 📘 Claude Skills: Professional Authoring Manual (2026)

## 1. Suggested Best Practices
Claude Skills are modular "playbooks" that provide Claude with just-in-time expertise. To ensure your skills are efficient and reliable, follow these industry-standard patterns.

### A. Naming and Metadata Strategy
* **The Gerund Rule:** Use the gerund form (verb + -ing) for skill names (e.g., `optimizing-sql-queries`, `reviewing-pr-compliance`). This clearly signals the skill's purpose to the model.
* **Lowercase Kebab-Case:** Skill names must be lowercase, numbers, and hyphens only (e.g., `deploy-helper` ✅, `Deploy_Helper` ❌).
* **Third-Person Descriptions:** Write descriptions in the third person. 
    * *Good:* "Validates React components against the internal design system."
    * *Avoid:* "I can help you validate components..." or "Use this to validate..."

### B. The "Progressive Disclosure" Architecture
To prevent "context bloat" and save tokens, structure your skill into three distinct layers:



1.  **Level 1 (YAML Frontmatter):** Always loaded. Contains the name and a high-level description used for discovery.
2.  **Level 2 (SKILL.md Body):** Loaded only when Claude identifies the skill is relevant. Contains core instructions and the "golden path" for the task.
3.  **Level 3 (Linked Files/Scripts):** Accessed only as needed. Store deep technical specs, large code examples, or logic scripts in subdirectories like `scripts/` or `_examples/`.

### C. Instruction Design: "Narrow Bridge vs. Open Field"
* **Narrow Bridge (High Precision):** For tasks where there is only one correct way (e.g., database migrations), use strict, numbered steps and explicit guardrails.
* **Open Field (Creative/Heuristic):** For tasks like "code reviews," provide general heuristics and principles, allowing Claude to adapt to the context of the specific file.

### D. The "Never Guess" Mandate
If your skill involves external data (like library versions), **always** include a script.
* **Practice:** Instead of telling Claude to "find the latest version," provide a `latest.js` script in the `scripts/` folder that it must execute.

---

## 2. Usage of `npx skills agent-skill-creator`
The `agent-skill-creator` is the official CLI utility for scaffolding new skills. It ensures your `SKILL.md` adheres to the 2026 universal format.

### Command Execution
To start the interactive wizard, run:
```bash
npx skills agent-skill-creator
```
*Note: You do not need to install it globally; npx fetches the latest version automatically.*

### Workflow Steps
1.  **The Prompting Phase:** The tool will ask: *"What should this skill do?"* Describe the goal in plain English (e.g., "A skill to audit AWS IAM policies for least privilege").
2.  **Refining Instructions:** The creator will generate a draft `SKILL.md`. It will ask you to confirm:
    * **Triggers:** What keywords or tasks should activate this?
    * **Rules:** What are the hard constraints?
    * **Tools:** Does it need shell scripts or API calls?
3.  **Directory Scaffolding:** Once confirmed, it generates the following structure:

```text
my-new-skill/
├── SKILL.md       # Frontmatter + Instructions
├── scripts/       # Any automation logic (JS/Python/Bash)
└── _examples/     # Sample inputs and outputs for few-shot learning
```

### Pro-Tip: Iterative Refinement
Skills are rarely perfect on the first run. The best way to use the creator is to generate a **v0.1**, test it in Claude Code or VS Code, and then pipe the feedback back:
```bash
npx skills agent-skill-creator --refine ./my-new-skill
```

---

## Quick Reference Table: Skill Limits
| Attribute | Limit / Standard | Why? |
| :--- | :--- | :--- |
| **Name Length** | Max 64 chars | For fast discovery indexing. |
| **Description** | Max 1024 chars | Efficiency in the system prompt. |
| **Body Size** | < 500 lines | Prevents context fragmentation. |
| **Scripts** | Idempotent | Scripts may be retried on failure. |

---

[Claude Code Skills & skills.sh - Crash Course](https://www.youtube.com/watch?v=rcRS8-7OgBo)

This video provides a practical walkthrough of the skills ecosystem and demonstrates how to create and share custom skills using the command-line tools discussed.


http://googleusercontent.com/youtube_content/0
