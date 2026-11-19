# Установка Codex Interrogation Mode

[← README](README.md) · [English](README.en.md)

## Требования

- Установленный OpenAI Codex с поддержкой пользовательских skills.
- Доступ на чтение/копирование файлов в каталоге skills.
- Никаких пакетов Python/Node.js и внешнего сервера не требуется.

## Шаг 1. Получить файлы

```bash
git clone https://github.com/lolpul/codex-interrogation.git
cd codex-interrogation
```

Или скачайте ZIP репозитория в GitHub → **Code → Download ZIP**, затем распакуйте его и откройте полученную папку.

**Нужно скопировать папку `interrogation` целиком**, а не весь репозиторий.

## Шаг 2. Выбрать папку назначения

| Область действия | Windows | Linux/macOS |
| --- | --- | --- |
| Глобально, рекомендованный путь | `%USERPROFILE%\.agents\skills\interrogation` | `~/.agents/skills/interrogation` |
| Глобально, ранее используемый Codex | `%USERPROFILE%\.codex\skills\interrogation` | `~/.codex/skills/interrogation` |
| Только для проекта | `<project>\.agents\skills\interrogation` | `<project>/.agents/skills/interrogation` |

Путь `.codex/skills` включён для совместимости с установками, где Codex уже обнаруживает skills в этом каталоге. При расхождении ориентируйтесь на документацию и проверенное поведение вашей версии Codex. Не устанавливайте одинаковые копии одновременно без необходимости.

## Шаг 3. Скопировать каталог

### Windows PowerShell

Из корня распакованного/клонированного репозитория:

```powershell
# Рекомендуемая глобальная установка
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\interrogation" "$HOME\.agents\skills\"
```

Если ваш Codex уже работает с `%USERPROFILE%\.codex\skills`, используйте:

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\interrogation" "$HOME\.codex\skills\"
```

Либо перенесите каталог через Проводник.

### Linux/macOS

```bash
mkdir -p ~/.agents/skills
cp -R ./interrogation ~/.agents/skills/
```

### Установка только в проект

Создайте в нужном репозитории `.agents/skills/` и поместите в него папку `interrogation`.

## Шаг 4. Проверить структуру

```text
<skills-directory>/
└── interrogation/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

Частая ошибка — лишний уровень `interrogation/interrogation/SKILL.md`: Codex может не распознать skill.

## Шаг 5. Запуск

1. Перезапустите Codex или откройте новую сессию, чтобы он перечитал список skills.
2. При работе над рискованной задачей включите штатный `/plan` (и при необходимости `Read Only`).
3. Запустите:

```text
$interrogation mode=auto Спроектируй новую функцию, задай все важные вопросы до реализации.
```

Другие варианты:

```text
$interrogation mode=light Добавь локальную настройку интерфейса.
$interrogation mode=standard Согласуй API между двумя модулями.
$interrogation mode=deep Проработай критичную интеграцию и отказные сценарии.
```

В текущем чате можно попросить «Переключи на Deep, сохрани предыдущие решения».

**`mode=...` — текстовая директива, предусмотренная skill. Она не является штатным параметром CLI Codex.**

## Обновление

1. Сделайте резервную копию изменённого локального `SKILL.md`, если вы его редактировали.
2. Замените каталог `interrogation` более новой версией.
3. Перезапустите Codex или начните новый чат.

## Удаление

Удалите папку `<skills-directory>/interrogation` и перезапустите Codex. Другие skills не затрагиваются.

## Безопасность

Инструкция запрещает записи до согласования ТЗ, **но сама по себе не может технически запретить файловые операции**. Для задач с важными данными используйте ограничения прав, обычные резервные копии/коммиты и проверяйте команды агента. `/plan` не следует трактовать как универсальную гарантию отсутствия любых побочных эффектов от произвольных внешних инструментов.

## Если не работает

См. [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) и [TEST_SCENARIOS.md](TEST_SCENARIOS.md).