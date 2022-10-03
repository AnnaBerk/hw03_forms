# backend_community_homework

Яндекс Практикум. Спринт 4. Итоговый проект. Расширение проекта [Yatube v1](https://github.com/AnnaBerk/hw02_community)

### Описание
Yatube - это социальная сеть с авторизацией, персональными лентами, комментариями и подписками на авторов статей.

### Функционал
- регистрация пользователя,
- вход/выход пользователя,
- восстановления пароля,
- создания записей сообщества,
- подробная информация, редактирование только своей записи,
- отображение постов пользователя,
- пагинация, раздел Об авторе, Технологии, отображения профиля пользователя.

### Установка
Клонировать репозиторий:
```bash
git clone git@github.com:AnnaBerk/hw02_community.git
```
Перейти в папку с проектом:
```bash
cd hw03_forms/
```
Установить виртуальное окружение для проекта:
```bash
python -m venv venv
```
Активировать виртуальное окружение для проекта:

для OS Lunix и MacOS
```bash
source venv/bin/activate
```
для OS Windows
```bash
source venv/Scripts/activate
```
Установить зависимости:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции на уровне проекта:
```bash
cd yatube
python3 manage.py makemigrations
python3 manage.py migrate
```
Запустить проект локально:
```bash
python3 manage.py runserver
```
адрес запущенного проекта
http://127.0.0.1:8000
Зарегистирировать суперпользователя Django:
```bash
python3 manage.py createsuperuser
```
адрес панели администратора
http://127.0.0.1:8000/admin
