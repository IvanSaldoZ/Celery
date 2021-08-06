from django.shortcuts import render
from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm
from .services import send
from .tasks import send_spam_email


# Create your views here.
class ContactView(CreateView):
    """
    Отображение формы подписки по email
    """
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        # Следующая строка запускает задачу в Celery (delay - отложить задачу и не ждать)
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)