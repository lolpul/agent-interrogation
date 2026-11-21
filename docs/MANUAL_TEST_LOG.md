# Manual validation log — Interrogation Mode

This is a **tracking log**, not a claim that any scenario passed. Automated checks validate
metadata, packaging and file consistency; only a real agent session can confirm
interview behavior, question quality or compliance with the approval gate.

## Execution metadata

For each run, record the date (UTC), the **exact commit SHA**, agent/client version,
OS, activation prompt, read-only/Plan mode, expected and observed behavior, verdict
(`PASS`, `FAIL`, or `BLOCKED`), and a link to sanitized evidence if available.

Do not publish private project contents, personal data, API credentials, or unredacted logs.
Use disposable example projects when verifying that no files are changed.

## Release-critical Codex checks

| ID | Scenario | Acceptance criterion | Last run | Result | Evidence |
| --- | --- | --- | --- | --- | --- |
| M01 | Light: local UI preference | Asks only material questions; produces short spec | — | NOT RUN | — |
| M02 | Standard: orders-to-notifications API | Clarifies contracts, errors, acceptance checks | — | NOT RUN | — |
| M03 | Deep: architecture migration | Records alternatives, risks, test plan | — | NOT RUN | — |
| M04 | Approval gate | No code/files changed before explicit approval; asks for confirmation | — | NOT RUN | — |
| M05 | Opt-in activation | Regular tasks do not implicitly trigger the interview | — | NOT RUN | — |
| M06 | Fresh installation and update | Correct installation path; customized copy not overwritten silently | — | NOT RUN | — |

### Run record template

```text
Test ID:
Date (UTC):
Commit SHA:
Agent/client + version:
Model / effort (if applicable):
OS:
Read-only / Plan mode enabled:
Start repository state (git status):
Prompt:
Expected:
Observed:
End repository state (git status):
Verdict: PASS / FAIL / BLOCKED
Redacted evidence link:
Notes / follow-up issue:
```

See [TEST_SCENARIOS.md](../TEST_SCENARIOS.md) for more adversarial and multi-agent
manual scenarios. For other agents, maintain a separate record; do not infer
support or compliance from Codex results.
