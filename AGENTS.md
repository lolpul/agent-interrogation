# Instructions for agents working with this repository

This is a public, instruction-only **Agent Skill** that installs from `interrogation/SKILL.md`.
For user requests to install it **from a GitHub link**, follow [AGENT_INSTALL.md](AGENT_INSTALL.md), which covers host detection, install locations, backups, verification, and invocation.

Do not assume the user wants installation if they pasted only the URL without any instruction; clarify intent.
Do not execute downloaded code or scripts during skill installation. Do not modify unrelated repositories or credentials.
When contributing to this repository, keep `interrogation/SKILL.md` host-neutral; put agent-specific installation details in `AGENT_INSTALL.md` and docs.
The skill itself is a behavioural instruction, not a sandbox permission control.
