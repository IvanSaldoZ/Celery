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

## Внедрение в Django и запуск Celery на отслеживание тасков
1. Определяем необходимые настройки CELERY и REDIS в файле settings.py
2. Определяем нужную функцию на выполнение в очереди в файле tasks.py
3. Дорабатываем файл __init__.py в главной папке проекта (send_email в нашем случае)
4. Создаем файл celery.py
5. Запускаем Django: `python manage.py runserver`
6. Запускам redis-сервер в качестве Брокера
`docker run -d -p 6379:6379 redis`
7. Запускаем celery на прослушивание сервера
`celery -A send_email worker --loglevel=INFO`
8. Готово! Можно пользоваться, вызывая какие-то функции из приложения (см. views.py).


## Запуск периодических задач
1. Указываем настройки периодического запуска в файле `celery.py`
2. Делаем шаги 5-7 с предыдущего раздела запуска задачи в очереди
3. Для запуска периодических задач необходимо использовать флаг beat.
4. `celery -A send_email beat -l info`