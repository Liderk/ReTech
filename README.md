# ReTech Labs Task

##Установка:
Для выполнить установку всех зависимостей:
```commandline
pip install -r requirements.txt
```
Создать миграции
```commandline
python manage.py makemigrations
python manage.py migrate
```
Создать администратора 
```commandline
python manage.py createsuperuser
```
Запустить сервер:
```commandline
python manage.py runserver
```
Создать пользователей и организации через панель администратора
```text
http://127.0.0.1:8000/admin/
```


Добавить в таблице Accounts разрешения к каким компаниям может подключаться пользователь

## Работа с api:

###Авторизация пользователя: 

отправить POST-запрос
```json
{
    "email": "your@email.ru", 
    "company":"company_name", 
    "password":"your_pass"
}
```
на
```text
http://127.0.0.1:8000/api/v1/signin/
```
###Получить все todo листы компании:
```text
http://127.0.0.1:8000/api/v1/task/
```

###Для создания ToDo листа отправить POST-запрос
```json
{
    "name": "Your task name",
    "task": "your task"
}
```
на
```text
http://127.0.0.1:8000/api/v1/task/
```
###Редактирование ToDo листа
Отправить PUT/PATCH запрос
```json
{
    "name": "some change in task name",
    "task": "some change in your task"
}
```
на 
```text
http://127.0.0.1:8000/api/v1/task/<int:id>/
```
где вместо < int:id> подставить номер ToDo листа

###Удаление ToDo листа
для удаления отправить DELETE - запрос на
```text
http://127.0.0.1:8000/api/v1/task/<int:id>/
```
где вместо < int:id> подставить номер ToDo листа
###Выход из системы:
```text
http://127.0.0.1:8000/api/v1/signout/
```