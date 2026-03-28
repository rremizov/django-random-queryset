---
name: _analyze-ci
description: Fetch and analyze failing CI checks across all open PRs, identify root causes, and summarize actionable fixes
model: haiku
---

Analyze failing CI checks across all open PRs in this repository.

## Steps

1. **Fetch open PRs with CI status:**
   ```bash
   gh pr list --json number,title,headRefName,statusCheckRollup
   ```

2. **Identify failing jobs** from `statusCheckRollup`: collect unique job IDs where `conclusion == "FAILURE"`. To avoid redundancy, deduplicate by `name` — if multiple PRs fail the same check with the same error, fetching one representative job log is enough.

3. **Fetch logs for failing jobs** (limit to the 3 most recent unique failures to avoid overwhelming output):
   ```bash
   gh run view --job <job_id> --log
   ```
   Focus on the lines around `##[error]` markers and the step that failed.

4. **Analyze failures** — for each distinct failure pattern:
   - Identify the failing step (e.g., "Install dependencies", "Run linter", "Run tests")
   - Extract the actual error message
   - Determine root cause (version conflict, syntax error, missing file, etc.)
   - Note which PRs are affected

5. **Report** in this structure:

```
## CI Failure Analysis

### Affected PRs
- #<number> — <title> (<branch>)
- ...

### Failure: <step name>

**Error:**
<exact error message from log>

**Root cause:**
<concise explanation>

---
[repeat for each distinct failure pattern]

### Secondary Warnings
<non-blocking warnings worth noting, e.g. deprecated actions>
```

## Guidelines

- If no PRs are failing, output: `All open PRs are passing CI.`
- Group PRs by failure pattern rather than reporting each PR individually.
- Keep root cause and fix sections concise — one or two sentences each.
- For dependency conflicts, name both the conflicting packages and the version constraint.
- For lint/format failures, name the specific file and rule if visible in logs.
- Ignore transient infrastructure failures (network timeouts, runner provisioning errors) — note them separately if they affect all PRs.
