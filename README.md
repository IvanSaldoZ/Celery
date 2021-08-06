## Celery Youtbe Tutorial

https://www.youtube.com/watch?v=s1vmVWCKefM

Task - задача (таск) (файл tasks.py)
Workers - ворекеры, внутри которых выполняются таски
Consumers - Потребители результатов ворекеров

Файл celery.py содержит инстанс объекта Celery. А в tasks.py хранятся все возможные Таски, которые 
можно запустить через Celery.

Для запуска Воркера используйте команду:
https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#first-steps
`celery -A send_email worker --loglevel=INFO`


Официальная документация:
https://docs.celeryproject.org/en/stable/getting-started/introduction.html

Свой SMTP-сервер:
https://www.hostinger.com.ua/rukovodstva/kak-ispolzovat-smtp-server

Celery Periodic Tasks
https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules


## Развертывание приложения
1. Устанавливаем все зависимости:
`pip install -r requirements.txt`
2. Выполняем миграции:
`python manage.py makemigrations`
`python manage.py migrate`
3. Определяем необходимые настройки CELERY и REDIS в файле settings.py
4. Определяем нужную функцию на выполнение в очереди в файле tasks.py
5. Дорабатываем файл __init__.py в главной папке проекта (send_email в нашем случае)
6. Создаем файл celery.py
7. Запускам redis-сервер в качестве Брокера
`docker run -d -p 6379:6379 redis`
8. Запускаем celery на прослушивание сервера
`celery -A send_email worker --loglevel=INFO`
9. Готово! Можно пользоваться, вызывая какие-то функции из приложения (см. views.py).