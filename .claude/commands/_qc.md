---
name: _qc
description: Quick commit - analyze staged changes and commit with subject + optional body using Haiku
model: haiku
---

Analyze the git staged changes and create a commit message following the conventional 50/72 format:

1. Run `git diff --cached` to see staged changes
2. Generate a commit message with:

   **Subject line (required):**
   - ~50 characters (max 72)
   - Starts with imperative verb (e.g., "Add", "Fix", "Update", "Remove")
   - Summarizes WHAT changed
   - No period at the end

   **Body (optional - use only when needed):**
   - Blank line after subject
   - Wrap at 72 characters per line
   - Explains WHY or HOW
   - Provides context for complex changes
   - Use bullet points with `-` or `*` for lists

3. Run git commit using heredoc format:
   ```bash
   git commit -m "$(cat <<'EOF'
   Subject line here

   Optional body here if needed.
   Can span multiple lines.
   EOF
   )"
   ```

**Examples:**

Simple change (subject only):
```
Add user authentication endpoint
```

Complex change (subject + body):
```
Fix null pointer in quote generator

The generator was accessing customer.name without checking
if customer exists. Added null check and fallback to handle
cases where customer data is incomplete.
```

**Decision criteria for body:**
- Simple/obvious changes: subject only
- Bug fixes with non-obvious cause: add body
- New features with context: add body
- Refactoring with reasoning: add body

DO NOT:
- Use past tense (use "Add" not "Added")
- End subject with period
- Exceed 72 chars in subject
- Add body for trivial changes
- Add any references to Claude or Antropic

