# Онлайн-сервис для вычисления координат по IP-адресу

Для начала работы с программным кодом онлайн-сервиса необходимо
установить Django версии 3.2.8:

### Инструкция по установке и первому запуску 

Установить сторонние библиотеки:

```
pip install -r requirements.txt
```

Провести миграцию:

```bash
python manage.py makemigrations
python manage.py migrate
```

Запустить веб-сервер проекта:

```bash
python manage.py runserver
```