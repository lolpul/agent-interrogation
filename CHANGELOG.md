# Changelog

## [Unreleased] — release-readiness work

- CI matrix for Windows/Linux with Python tests, YAML validation and plugin ZIP build.
- GitHub Issue forms, manual verification log and explicit release acceptance criteria.
- Neutral integration scenario in public tests; documentation of feedback and CI.
- **No new GitHub Release or empirical agent-behavior claims yet.**


## Plugin packaging (2026-11-21)

- Добавлены portable manifest, Codex compatibility manifest, упаковка skills-only plugin и SVG-иконка.
- Добавлены стандартная локальная структурная проверка и сборщик ZIP без внешних зависимостей.
- Обычная установка и исходный `interrogation/SKILL.md` не изменены.

## [2.1.0] — 2026-11-19

- Универсальная логика skill для Codex, Claude Code, Cursor, Gemini CLI и OpenCode.
- Инструкция установки по одной ссылке через агента: `AGENT_INSTALL.md`, без обязательных скриптов.
- Обновлены README RU/EN и пути установки; добавлены правила безопасного обновления.
- Сохранён прежний вызов `$interrogation` в Codex и уровни Auto/Light/Standard/Deep.
- Поведение в сторонних агентах пока требует ручных проверок.


## [2.0.0] — 2026-11-19

- Адаптивная оценка глубины `mode=auto` по S/U/R/I.
- Поддержка `mode=light`, `mode=standard`, `mode=deep`.
- Обновление глубины без сброса подтверждённых решений в текущем чате.
- Разная детализация итогового ТЗ, единые блокирующие условия завершения.
- Явное предупреждение: skill не является техническим read-only механизмом.
- Публичная документация на русском и английском, установка и ручные тест-сценарии.

## [1.0.0] — первоначальная версия

- Интервью до реализации; журнал решений; финальное ТЗ и явный шлюз утверждения.