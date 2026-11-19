# Публикация репозитория на GitHub

Файлы готовы к публикации в `https://github.com/lolpul/codex-interrogation`. Репозиторий создан. Этот документ описывает подготовку чистого репозитория или публикацию форка.

## Вариант А — через GitHub (без GitHub CLI)

1. Откройте https://github.com/new.
2. В **Repository name** укажите `codex-interrogation`.
3. Выберите **Public**.
4. Не добавляйте README, .gitignore или лицензию при создании: они уже есть в пакете.
5. Нажмите **Create repository**.
6. Передайте ссылку на созданный пустой репозиторий в чат с подключённым GitHub — можно загрузить файлы в него через коннектор или сделать `git push` локально.

## Вариант Б — одной командой через GitHub CLI

Установите `gh` при необходимости: https://cli.github.com/ . Авторизуйтесь через `gh auth login`.

Из папки, в которой находятся README.md и `interrogation/`:

```bash
git init -b main
git add .
git commit -m "Initial release: Codex Interrogation Mode v2"
gh repo create lolpul/codex-interrogation --public --source . --remote origin --push
```

Если имя уже занято, GitHub сообщит об ошибке. Не перезаписывайте чужой/существующий репозиторий автоматически.

## Рекомендуемые GitHub Topics

`openai-codex`, `codex`, `agent-skills`, `prompt-engineering`, `requirements-engineering`, `developer-tools`, `planning`

Рекомендуемое описание:

> Adaptive requirements interview skill for OpenAI Codex. Light/Standard/Deep modes, no implementation before explicit spec approval.

## Проверка после публикации

Проверьте открытие `README.md`, наличие `interrogation/SKILL.md`, статус **Public** и успешность копирования в каталог Codex skills.