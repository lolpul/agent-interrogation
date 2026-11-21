# Release readiness checklist

This checklist defines a **candidate quality gate**, not a release announcement.
Do not tag or create a GitHub Release until every release-critical item is verified.

## Automated checks

- [ ] GitHub Actions CI passes on `ubuntu-latest` and `windows-latest`.
- [ ] Python unit tests pass on the supported Python versions in CI.
- [ ] Both skill frontmatters and Codex metadata parse as valid YAML.
- [ ] Canonical and packaged `SKILL.md` / `agents/openai.yaml` remain identical.
- [ ] The minimal ZIP builds and passes its archive and metadata checks.
- [ ] CI reports no blocking failures on the final PR commit.

## Manual acceptance checks

- [ ] Run and record M01 Light, M02 Standard, and M03 Deep in a real Codex client.
- [ ] Run M04 approval gate in a **disposable test repository** with a clean `git status`.
- [ ] Run M05 opt-in activation and M06 clean install/update, with evidence recorded.
- [ ] Confirm that the skill's instruction-only write restriction is described accurately.

Record each verified run in [MANUAL_TEST_LOG.md](MANUAL_TEST_LOG.md).
Mark `NOT RUN` or `BLOCKED` instead of claiming a pass without evidence.

## Public release and distribution

- [ ] Verify English/Russian README installation commands and troubleshooting.
- [ ] Check that examples, screenshots and test artifacts contain no internal project
      details, private data, or secrets.
- [ ] MIT license remains unchanged and both installation methods still work.
- [ ] Changelog/release notes describe only changes actually shipped.
- [ ] Select a version number and tag only after the PR is reviewed and merged.
- [ ] Publish a GitHub Release and attach a verified ZIP **only after approval**.

## Current decision

**Release status: NOT READY / PENDING manual checks and review.**

A PR and green CI do not themselves authorize publishing or claiming
an OpenAI-endorsed distribution.
