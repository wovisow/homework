# Проект по предоставлению информации о продуктах на складах.

#### Poetry
- При первом запуске команды в каталоге проекта Poetry создаёт виртуальную среду Python, которая будет связана с проектом.
```bash
poetry shell
```
- Устанавливает зависимости, указанные в pyproject.toml.
```bash
poetry install
```

#### Migrations
- Создание миграции.
```bash
python manage.py makemigrations
``` 

- Применение миграций.
```bash
python manage.py migrate
```

#### Database dump
- Создание копии базы данных.
```bash
python manage.py dumpdata > db.json
``` 
- Восстановление по резервной копии.
```bash
python manage.py loaddata db.json
```

ps: ya ne pomnu, kak pisat na django, silno ne beite 🙏
