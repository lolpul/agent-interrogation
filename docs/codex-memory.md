# Контекст проекта для Codex

- [agent-interrogation](https://github.com/lolpul/agent-interrogation) публикует скилл для интервью по требованиям перед реализацией. В Codex вызывается через `$interrogation`.
- Источник для [прямой установки](../AGENT_INSTALL.md) — `interrogation/`. Плагин берёт идентичные по байтам `SKILL.md` и `agents/openai.yaml` из `skills/interrogation/`. Версии двух JSON-манифестов должны совпадать.
- [CI](https://github.com/lolpul/agent-interrogation/actions/workflows/ci.yml) проверяет Windows и Linux с Python 3.14 и сохраняет ZIP. Команды для локальных тестов описаны в [CONTRIBUTING.md](../CONTRIBUTING.md). PyYAML нужен тестам, сборщик и установка обходятся стандартными средствами.
- При подготовке первого стабильного релиза семь тестов и сборка ZIP проверены на Windows и Ubuntu через WSL. Ручные прогоны Codex ожидаются. Их сценарии, журнал и условия публикации описаны в [критериях релиза](RELEASE_CRITERIA.md).
- Публикация релиза требует явного подтверждения владельца. Детали изменений и локальной проверки приведены в [записи о подготовке релиза](patches/2026-11-21-0256-release-readiness.md). Результаты hosted CI сохраняются в GitHub Actions.
