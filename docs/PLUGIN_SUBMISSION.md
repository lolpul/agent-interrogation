# Skills-only plugin package for OpenAI / Codex

This repository can be installed in **two independent ways**:

1. **Direct Agent Skill install:** follow [AGENT_INSTALL.md](../AGENT_INSTALL.md) or [INSTALL.md](../INSTALL.md). This keeps using `interrogation/SKILL.md` exactly as before.
2. **Skills-only Plugin:** the portable root `plugin.json` and `skills/interrogation/` are a *distribution copy* of the same skill. The optional `.codex-plugin/plugin.json` provides compatibility with older Codex plugin installations.

No MCP server, credential, remote execution service, or API key is included. Both distribution copies must remain byte-for-byte synchronized.

## Validate and build

Requires Python 3.9+; no third-party Python packages.

```sh
python scripts/build_plugin.py --check
python scripts/build_plugin.py
```

The output is `dist/agent-interrogation-2.1.0.zip`. The ZIP contains only:

- portable `plugin.json`
- compatibility `.codex-plugin/plugin.json`
- `skills/interrogation/SKILL.md` and `agents/openai.yaml`
- the SVG icon and MIT LICENSE

Do **not** submit the GitHub repository source ZIP in place of this plugin ZIP. The repository contains separate installation guides and developer files not needed by the plugin.

## Manual behavioral checks (not comparative benchmarks)

Run the plugin in a clean supported client and verify:

1. **Light / local change:** identifies relevant context, asks only material questions and drafts a concise spec.
2. **Standard / feature integration:** identifies contracts, failure cases and acceptance criteria before proposing implementation.
3. **Deep / architecture:** compares material alternatives and records decisions, risks and verification strategy.
4. **Approval gate:** after writing the specification, it does not write or apply code before explicit user approval; if the client lacks enforceable read-only permissions, it makes the limitation clear.
5. **Non-activation:** ordinary coding requests do not activate this skill implicitly.

Detailed existing test prompts are in [TEST_SCENARIOS.md](../TEST_SCENARIOS.md).

These are manual behavior checks. Passing the structural validator **does not prove** correct runtime behavior, a technical write lock, or measurable savings in time/tokens. There is no requirement to prove that the skill outperforms Codex Plan Mode, which serves a different workflow.

## Submit

1. Review [OpenAI package documentation](https://developers.openai.com/plugins/build/plugins) and [submission instructions](https://developers.openai.com/plugins/deploy/submission).
2. Build and test the ZIP locally; do not add secrets or private repository contents.
3. In the OpenAI Plugins submission portal, choose **Skills only** and upload the generated ZIP under your verified developer identity.
4. Resolve blocking metadata and skill findings, submit for review, then publish if approved. This repository is **not** an official or already-approved plugin.

For a skills-only package, the MCP-specific five positive / three negative reviewer cases and video walkthrough are **not required**. Platform validation, skill scans and public review still apply.

The current official examples live in [openai/plugins](https://github.com/openai/plugins); [openai/skills](https://github.com/openai/skills) is marked deprecated.
