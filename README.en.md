# Codex Interrogation Mode

[Русский](README.md) · [Installation](INSTALL.md) · [Test scenarios](TEST_SCENARIOS.md)

**A requirements-first interview skill for OpenAI Codex.** Codex should inspect the relevant repository context, ask blocking questions, reconcile conflicting requirements, prepare an acceptance-testable specification, and wait for explicit approval **before implementing**.

This is a **community-maintained, unofficial Codex skill**, not a built-in Codex mode or security boundary.

## Why use it?

When tasks are underspecified, a coding agent may implement the wrong API, miss an important failure path, or make an architectural assumption that requires costly rework. This skill adds an explicit discovery and approval phase. It can reduce unnecessary revisions on complex tasks, but it also adds overhead; no time or token savings are guaranteed.

## Modes

| Mode | Typical use | Interview scope | Deliverable |
| --- | --- | --- | --- |
| **Auto** | Default | Assess scope, uncertainty, risk, integrations (S/U/R/I), then adapt | Specification proportional to risk |
| **Light** | Small local change | Typically 2–5 meaningful questions, fewer when unnecessary | Short specification and acceptance checks |
| **Standard** | Feature or cross-module change | Contracts, errors, integration constraints, verification | Full feature specification |
| **Deep** | Architecture, reliability, critical integrations | Alternatives, invariants, failures, migration, security as relevant | Detailed design, verification and risk plan |

Question counts are guidance, not hard limits. **Unresolved blocking questions must not be ignored in any mode.** For explicitly selected modes, the skill recommends a mode change rather than silently overriding the user.

## Installation

Clone this repository:

```bash
git clone https://github.com/lolpul/codex-interrogation.git
cd codex-interrogation
```

Copy the **`interrogation` directory** (not the entire repository) to the user-level skills folder:

**Windows PowerShell:**

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\interrogation" "$HOME\.agents\skills\"
```

**Linux/macOS:**

```bash
mkdir -p ~/.agents/skills
cp -R ./interrogation ~/.agents/skills/
```

An existing legacy-style `%USERPROFILE%\.codex\skills` / `~/.codex/skills` installation can also be used when supported by your Codex version. For repository-local installation, copy the folder into `<repo>/.agents/skills/`. See [INSTALL.md](INSTALL.md) for more details (Russian).

Expected layout:

```text
<skills-root>/interrogation/SKILL.md
<skills-root>/interrogation/agents/openai.yaml
```

Restart or start a new Codex session after installation.

## Usage

```text
$interrogation Design a small UI preference.
$interrogation mode=light Clarify a local change.
$interrogation mode=standard Define the API between two services.
$interrogation mode=deep Design a high-risk integration with recovery behavior.
```

`mode=...` is **plain text interpreted by this skill**, not an official Codex CLI option. You can change the mode mid-interview: “Switch to Deep and retain all previous decisions.”

**Recommended:** enable built-in `/plan` first. `$interrogation` defines how requirements should be gathered; `/plan` is Codex's built-in planning mode. The skill does not itself enforce read-only permissions or prevent tool-side effects. Use an available Read Only setting where appropriate and review tool calls.

## Workflow

1. Read only the relevant code and project instructions.
2. Determine or accept the interview depth.
3. Ask questions with options and trade-offs, track agreed/delegated/open items.
4. Reconcile contradictions and adapt depth when appropriate.
5. Produce a specification with observable acceptance criteria.
6. Wait for explicit approval before proceeding to implementation.

Decisions are held in the **current conversation context**, not a persistent database; bring the specification to a new session if needed.

## Limitations and testing

This is an instruction-based workflow, not a technical write lock. The model can make mistakes and may still need supervision. Test coverage currently consists of [nine manual scenarios](TEST_SCENARIOS.md); behavior is not certified across all Codex clients and versions. The skill itself is written in Russian; Codex is instructed to respond in the user's language.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under the [MIT License](LICENSE).

Resources: [Codex skills](https://developers.openai.com/codex/skills) · [Skill evals](https://developers.openai.com/blog/eval-skills) · [Plan mode](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex).