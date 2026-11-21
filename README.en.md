# Interrogation Mode — Universal Agent Skill

[Русский](README.md) · [Installation](INSTALL.md) · [Test scenarios](TEST_SCENARIOS.md)

**A requirements-first interview skill for OpenAI Codex.** Codex should inspect the relevant repository context, ask blocking questions, reconcile conflicting requirements, prepare an acceptance-testable specification, and wait for explicit approval **before implementing**.

This is a **community-maintained, unofficial Codex skill**, not a built-in Codex mode or security boundary.


## Install by sending one prompt to your coding agent

Paste this into **Codex, Claude Code, Cursor, Gemini CLI, or OpenCode**:

```text
Install the interrogation skill from https://github.com/lolpul/agent-interrogation. Read AGENT_INSTALL.md, detect your agent, install globally, preserve existing skills, verify installation, and tell me how to use it.
```

The agent will use [AGENT_INSTALL.md](AGENT_INSTALL.md) for the platform-specific destination, safe update and verification steps. A bare URL without an installation request is ambiguous. File-system and network permissions may require approval.

| Agent | Typical invocation |
| --- | --- |
| Codex | `$interrogation` |
| Claude Code | `/interrogation` |
| Cursor | `/interrogation` in Agent chat |
| Gemini CLI | Ask it to activate the `interrogation` skill |
| OpenCode | `@interrogation` |

The skill uses the open `SKILL.md` format. Agent-specific installation details live in the installer guide. This is a behaviour guideline rather than a technical read-only guarantee.

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
git clone https://github.com/lolpul/agent-interrogation.git
cd agent-interrogation
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

The skill guides the model through an interview. The client's permissions govern access to files and tools. The skill is written in Russian and instructs agents to respond in the user's language.

[GitHub Actions](https://github.com/lolpul/agent-interrogation/actions/workflows/ci.yml) runs Python unit tests, parses the skill's YAML frontmatter, compares both skill copies, and builds and validates the plugin ZIP on Windows and Linux. Run the same checks locally with the commands in [CONTRIBUTING.md](CONTRIBUTING.md).

Use the [manual scenarios](TEST_SCENARIOS.md) to verify Codex behavior. Record the tested commit and client version in the [manual test log](docs/MANUAL_TEST_LOG.md). See the [release criteria](docs/RELEASE_CRITERIA.md) for publication requirements.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under the [MIT License](LICENSE).

[All Issues](https://github.com/lolpul/agent-interrogation/issues) · [Report a bug](https://github.com/lolpul/agent-interrogation/issues/new?template=bug_report.md) · [Request a feature](https://github.com/lolpul/agent-interrogation/issues/new?template=feature_request.md)

Resources: [Codex skills](https://developers.openai.com/codex/skills) · [Skill evals](https://developers.openai.com/blog/eval-skills) · [Plan mode](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex).

## OpenAI Skills-only Plugin distribution

This repository also provides a portable `plugin.json`, a Codex compatibility manifest, an identical skill copy at `skills/interrogation/`, and an icon. This is a distribution format for the **same** skill, not a new built-in Codex mode or a replacement for `/plan`.

Validate using `python scripts/build_plugin.py --check`; package with `python scripts/build_plugin.py` (output in `dist/`). Legacy/direct installations from `interrogation/` are unchanged. See [the submission guide](docs/PLUGIN_SUBMISSION.md). **Not yet published or endorsed by OpenAI.**
