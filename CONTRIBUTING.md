# Участие в проекте / Contributing

Спасибо за интерес к улучшению `$interrogation`.

## Что полезно присылать

- Воспроизводимые случаи, когда skill начал реализацию без утверждения.
- Сценарии, где `auto` неверно выбрал глубину, или вопросы оказались избыточными.
- Улучшения русскоязычных инструкций, примеров или установки.
- Небольшие правки без излишнего усложнения SKILL.md.

## Обратная связь

- [Bug Report](https://github.com/lolpul/agent-interrogation/issues/new/choose) — воспроизводимые сбои установки и поведения.
- [Feature Request](https://github.com/lolpul/agent-interrogation/issues/new/choose) — улучшения на основе реальных задач.
- [Журнал ручных проверок](docs/MANUAL_TEST_LOG.md) — фиксируйте только реально выполненные тесты.
- [Критерии релиза](docs/RELEASE_CHECKLIST.md) — что нужно проверить до публикации.

## Перед pull request

1. Опишите проблему и ожидаемое поведение.
2. Убедитесь, что `interrogation/SKILL.md` по-прежнему требует явного утверждения ТЗ, не выдаёт `mode=` за CLI-флаг и не обещает техническую блокировку изменений.
3. Запустите `python -m pip install -r requirements-dev.txt`, затем `python -m unittest discover -s tests -v` и `python scripts/build_plugin.py --check`. Проверьте соответствующие сценарии из [TEST_SCENARIOS.md](TEST_SCENARIOS.md) вручную в Codex, если есть доступ; не отмечайте сценарий как проверенный без реального прогона.
4. Не публикуйте исходники чужих проектов, секреты, токены, конфиденциальные логи или персональные данные.

## English

Please submit reproducible reports or narrowly scoped PRs. Include the Codex version/client, trigger prompt, expected and actual behavior, and test evidence where available. Never include secrets or proprietary code. This skill is instruction-only and must not claim to enforce filesystem access controls.