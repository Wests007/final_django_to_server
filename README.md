# TravelTube

## Описание
Социальная сеть блогеров о путешествиях.

## Технологии
Python 3
Django 2.2

### Проект доступен в сети по адресу:
[https://wests007.pythonanywhere.com/](https://wests007.pythonanywhere.com/)

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Wests007/final_django_to_server.git
```
```
cd final_django_to_server
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/scripts/activate
```
Обновить менеджер пакетов и установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Перейти в папку с файлом manage.py и выполнить миграции:
```
cd yatube
```
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```

### В разработке:
Изменение шаблонов. Добавление анимации.

## Автор
[Ромашков Александр](https://github.com/Wests007)
