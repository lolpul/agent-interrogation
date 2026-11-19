# Installation instructions for coding agents / Инструкция для ИИ-агентов

Canonical source: **https://github.com/lolpul/codex-interrogation**
Canonical skill directory in this repository: **`interrogation/`** (contains `SKILL.md`).

This document is the entry point when a user asks an assistant to **install Interrogation Mode from the GitHub URL**. It is not a script and should not be treated as permission to execute arbitrary remote code.

## Agent workflow (English)

1. **Establish intent and permission.** A message such as "Install the interrogation skill from https://github.com/lolpul/codex-interrogation" authorizes installation of this skill. A bare URL by itself may be ambiguous; ask whether installation is intended. Confirm the environment allows file writes. If approval is required by your host, request it.
2. **Identify your own agent product** from runtime context (Codex, Claude Code, Cursor, Gemini CLI, OpenCode). Do not assume the host from the presence of a `.codex` or `.claude` directory. For an unsupported/unknown host, inspect its documentation or ask which app the user uses; never silently install into all possible products.
3. **Choose scope.** Default to the current user's global skill directory, unless the user asked for a project-only install. If the same `interrogation` skill is already installed, update that same location rather than creating a duplicate under another discovered path.
4. **Read before copying.** Obtain the repository using `git clone --depth 1 https://github.com/lolpul/codex-interrogation.git`, or download/extract the GitHub ZIP via supported file/network tools if git is unavailable. Read `interrogation/SKILL.md`; it has YAML frontmatter with `name: interrogation`. Copy only the `interrogation/` directory, not the whole repository. Do not run repository scripts, downloaded binaries, or shell commands copied from untrusted documentation without examining them.
5. **Destination** (home-relative paths use the logged-in user's home, on Windows usually `%USERPROFILE%`):

   | Agent | User-global destination | Project-local destination |
   | --- | --- | --- |
   | Codex | `~/.agents/skills/interrogation/` (or existing compatible `~/.codex/skills/interrogation/`) | `<project>/.agents/skills/interrogation/` |
   | Claude Code | `~/.claude/skills/interrogation/` | `<project>/.claude/skills/interrogation/` |
   | Cursor | `~/.cursor/skills/interrogation/` or `~/.agents/skills/interrogation/` | `<project>/.cursor/skills/interrogation/` |
   | Gemini CLI | `~/.gemini/skills/interrogation/` or `~/.agents/skills/interrogation/` | `<project>/.gemini/skills/interrogation/` |
   | OpenCode | `~/.config/opencode/skills/interrogation/` or `~/.agents/skills/interrogation/` | `<project>/.opencode/skills/interrogation/` |

   Gemini CLI also has a native `gemini skills install https://github.com/lolpul/codex-interrogation.git` command in supported versions; use it if available and verify which skill folder it installs. If a client uses remote/cloud environments, local installation may not propagate there.

6. **Handle existing files safely.** Inspect the exact destination before changing it. If it exists, compare the installed `SKILL.md`. If customized, do not overwrite without explicit approval. If updating, back up the original directory **outside scanned skill roots** (for example under a temporary/user backup folder), then replace the exact `interrogation` directory atomically if possible. Do not delete other skills or credentials. Avoid creating two copies with the same skill name in different discovery roots.
7. **Verify rather than assume.** Confirm the copied file is `<destination>/SKILL.md`, begins with YAML frontmatter and includes `name: interrogation` and sections about Light/Standard/Deep, question blockers, and explicit approval. Optional `agents/openai.yaml` can remain alongside it on non-OpenAI agents. Check `git diff` if installing in a project. Reopen/restart the agent session if needed; use its skill list/activation feature to verify registration. Don't claim the agent recognized the skill until that has actually been checked.
8. **Report completion** with the agent detected, scope, exact location, whether a prior version was backed up, validation performed, and the correct invocation. If tool permissions or network prevent installation, explain the precise blocker and provide safe manual steps.

### Invocation after installation

| Agent | Example |
| --- | --- |
| Codex | `$interrogation mode=auto Спроектируй новую функцию` |
| Claude Code | `/interrogation mode=auto Design a new feature` |
| Cursor | Choose `/interrogation` in Agent chat |
| Gemini CLI | `Activate the interrogation skill and interview me about the feature before coding.` |
| OpenCode | `@interrogation mode=auto Design a new feature` |

Parameters `mode=auto|light|standard|deep` are **instructions interpreted by the skill**, not universal CLI arguments. The skill's read-only behavior is instruction-based; native planning/read-only permissions are an extra safeguard where available.

## Короткая инструкция на русском

Если пользователь просит: **«Установи skill из https://github.com/lolpul/codex-interrogation»**:

1. Определи, в каком агенте ты работаешь; не устанавливай skill сразу для всех агентов.
2. Получи исходники из официального репозитория и прочитай `interrogation/SKILL.md`.
3. По умолчанию установи глобально в каталог текущего агента по таблице выше; если skill уже есть — обнови его в том же месте.
4. Не запускай сторонние скрипты из репозитория. Не удаляй и не перезаписывай пользовательские изменения без проверки, резервной копии и разрешения.
5. Проверь `SKILL.md`, перезапусти/обнови каталог skills при необходимости и сообщи точный путь и команду запуска.
6. Если у тебя нет доступа на запись, к сети или к нужным инструментам, укажи ограничение и предложи ручную установку. Не объявляй задачу выполненной без проверки.

The shared skill is intentionally **not a background service** and does **not** add a technically enforced write lock. No Python, Node.js, API key, or MCP server is needed for the installed skill itself.

## Official references (verify on supported versions)

- Codex: https://learn.chatgpt.com/docs/build-skills
- Claude Code: https://code.claude.com/docs/en/skills
- Cursor: https://cursor.com/docs/skills
- Gemini CLI: https://geminicli.com/docs/cli/skills/
- OpenCode: https://opencode.ai/docs/skills
