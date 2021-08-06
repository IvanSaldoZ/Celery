import pathlib

from django.core.mail import send_mail
from send_email.celery_mod import app

from .services import send
from .models import Contact


@app.task
def send_spam_email(user_email):
    """
    Таска по отрпавке email-а
    :param user_email:
    :return:
    """
    send(user_email)


@app.task
def send_beat_email():
    """
    Периодическая таска
    :return:
    """
    for contact in Contact.objects.all():
        with open('email_sending.log', 'wt') as f:
            f.write(contact.email)
        send(contact.email)
