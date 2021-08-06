from django.core.mail import send_mail

def send(user_email):
    """
    Функция для отправки email-а
    :return:
    """
    send_mail('Вы подписались на рассылку!',
              'Мы будем присылать вам много спама!',
              "saldoz@ya.ru",
              [user_email],
              fail_silently=False,
              )