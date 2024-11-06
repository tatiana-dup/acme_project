## Описание проекта:
Учебный проект сервиса, на котором размещается информация о днях рождениях людей, а пользователи могут оставить комментарий с поздравлением.

В рамках проекта были отработаны:
- реализация проекта на Django;
- использование шаблонизатора Django для создания HTML-шаблонов;
- подключение базы данных, выполнение CRUD-операций с Django ORM и настройка Django Forms;
- настройка и кастомизация админ-панели Django.

Стек проекта: Python 3.9, Django, Bootstrap.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:tatiana-dup/acme_project.git
```

```
cd acme_project/
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

После локального запуска проект будет доступен по ссылке: http://127.0.0.1:8000
