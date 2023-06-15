📁 tg_bot_template
 |_ .env
 |_ .env.example
 |_ .gitignore
 |_ bot.py
 |_ requirements.txt
 |_ 📁 config_data
 |   |_ __init__.py
 |   |_ config.py
 |_ 📁 errors
 |   |_ __init__.py
 |   |_ errors.py
 |_ 📁 external_services
 |   |_ __init__.py
 |_ 📁 filters
 |   |_ __init__.py
 |   |_ is_admin.py
 |   |_ language_filter.py
 |_ 📁 handlers
 |   |_ __init__.py
 |   |_ admin_handlers.py
 |   |_ private_user_handlers.py
 |   |_ user_handlers.py
 |_ 📁 keyboards
 |   |_ __init__.py
 |   |_ keyboard_utils.py
 |   |_ set_menu.py
 |_ 📁 lexicon
 |   |_ __init__.py
 |   |_ lexicon_ru.py
 |   |_ lexicon_en.py
 |_ 📁 middlewares
 |   |_ __init__.py
 |   |_ throttling.py
 |_ 📁 models
 |   |_ __init__.py
 |   |_ methods.py
 |   |_ models.py
 |_ 📁 services
 |   |_ __init__.py
 |   |_ services.py
 |_ 📁 states
 |   |_ __init__.py
 |   |_ states.py
 |_ 📁 tests
 |   |_ __init__.py
 |_ 📁 utils
     |_ __init__.py
     |_ utils.py


## 📁 tg_bot_template

Это директория, в которой хранится проект. Сюда мы также устанавливаем виртуальное окружение, git, здесь IDE хранит свой
кэш и т.п. Ее обычно называют по имени проекта.

## .env.example

Пример файла с секретами, где реальные секреты заменены на неработающие, но похожие по структуре, примеры. Этот файл
можно и нужно хранить на гитхабе, чтобы другие разработчики понимали как должен выглядеть реальный .env-файл. Нужно не
забывать его обновлять, при изменениях структуры реального .env-файла.

## .gitignore

Файл для системы контроля версий, в котором прописаны файлы и директории проекта, которые не следует отслеживать.

## bot.py

Основной файл проекта - точка входа в проект. Запуск бота - это, по сути, запуск файла bot.py.

## requirements.txt

Файл с зависимостями - версиями библиотек, используемыми в проекте. При развертывании бота на сервере, сервер читает из
этого файла требуемые зависимости и устанавливает их. Про него поговорим отдельно, когда дойдем до деплоя бота.

## 📁 config_data

Пакет для хранения файлов с конфигурационными данными.

## config.py

Файл с конфигурационными данными для бота, базы данных, сторонних сервисов и т.п.

## 📁 errors

Пакет с модулями для обработки исключений, возникающих в процессе работы бота.

## errors.py

Модуль с обработчиками исключений.

## 📁 external_services

Пакет с модулями для работы с API внешних сервисов.

## 📁 filters

Пакет с кастомными фильтрами, если не хватает встроенных фильтров самого aiogram, или если анонимная функция, при
регистрации хэндлеров в диспетчере, получается слишком громоздкой и ее лучше убрать из регистратора.

## is_admin.py

Модуль с функцией-фильтром, проверяющей пользователя, является ли он администратором бота.

## language_filter.py

Языковой фильтр. Актуален для мультиязычных ботов. Если бот работает только на одном языке - такой фильтр не требуется.

## 📁 handlers

Пакет, в котором хранятся обработчики апдейтов.

## admin_handlers.py

Модуль с хэндлерами, срабатывающими на действия пользователя, если он является администратором бота.

## private_user_handlers.py

Модуль с хэндлерами, срабатывающими на действия пользователей с каким-то другим статусом, например, если они заплатили
за дополнительный функционал бота.

## user_handlers.py

Модуль с хэндлерами для пользователей с обычным статусом, например, для тех, кто первый раз запустил бота.

## 📁 keyboards

Пакет с модулями, в которых хранятся и/или динамически формируются клавиатуры, отправляемые пользователям ботом, в
процессе взаимодействия.

## keyboard_utils.py

Вспомогательные функции/методы, помогающие формировать клавиатуры.

## set_menu.py

Модуль для установки команд в нативную кнопку "Menu" вашего бота.

## 📁 lexicon

Пакет для хранения текстов - ответов бота.

## lexicon_ru.py

Модуль со словарем соответствий данных текстам на русском языке.

## lexicon_en.py

Модуль со словарем соответствий данных текстам на английском языке.

## 📁 middlewares

Пакет, в котором хранятся мидлвари, то есть программы, которые работают с апдейтамм до того момента, как они попадут в
хэндлер.

## throttling.py

Модуль с "удушающей миддлварью", то есть с функциями/методами, которые отсекают от хэндлеров апдейты, распознанные как
флуд. Например, если пользователь слишком часто жмет одну и ту же кнопку или отправляет много коротких сообщений в
короткий промежуток времени.

## 📁 models

Пакет с модулями для взаимодействия с базой данных.

## methods.py

Модуль с методами для работы с БД.

## models.py

Модуль с ORM-моделями базы данных, то есть отображением базы данных в виде объекта с атрибутами, часто совпадающими с
полями базы данных. Через такие объекты можно обращаться к базе данных и как-то взаимодействовать с ней, обращаясь к
атрибутам и методам объектов.

## 📁 services

Пакет с модулями для реализации какой-то бизнес-логики бота.

services.py Соответственно, модуль с реализацией бизнес-логики.

## 📁 states

Пакет с модулями, в которых описаны классы, отражающими возможные состояния пользователей, в процессе взаимодействия с
ботом, для реализации машины состояний.

## states.py

Соответственно, модуль с классами, отражающими возможные состояния пользователя, в процессе взаимодействия с ботом.

## 📁 tests

Пакет с тестами для тестирования работы бота перед тем, как развернуть и запустить его в продакшн.

## 📁 utils

Пакет для хранения вспомогательных модулей, которые нужны в процессе работы бота, но по смыслу не попали ни в одну из
предыдущих категорий.

## utils.py

Модуль с утилитами - вспомогательными скриптами для работы бота.
