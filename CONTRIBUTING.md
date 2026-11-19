# Участие в проекте / Contributing

Спасибо за интерес к улучшению `$interrogation`.

## Что полезно присылать

- Воспроизводимые случаи, когда skill начал реализацию без утверждения.
- Сценарии, где `auto` неверно выбрал глубину, или вопросы оказались избыточными.
- Улучшения русскоязычных инструкций, примеров или установки.
- Небольшие правки без излишнего усложнения SKILL.md.

## Перед pull request

1. Опишите проблему и ожидаемое поведение.
2. Убедитесь, что `interrogation/SKILL.md` по-прежнему требует явного утверждения ТЗ, не выдаёт `mode=` за CLI-флаг и не обещает техническую блокировку изменений.
3. Проверьте соответствующие сценарии из [TEST_SCENARIOS.md](TEST_SCENARIOS.md) вручную в Codex, если есть доступ; не отмечайте сценарий как проверенный без реального прогона.
4. Не публикуйте исходники чужих проектов, секреты, токены, конфиденциальные логи или персональные данные.

## English

Please submit reproducible reports or narrowly scoped PRs. Include the Codex version/client, trigger prompt, expected and actual behavior, and test evidence where available. Never include secrets or proprietary code. This skill is instruction-only and must not claim to enforce filesystem access controls.