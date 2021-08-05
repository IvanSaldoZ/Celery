from django.shortcuts import render
from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm
from .services import send

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
        # send_span_email_delay(form.instance.email)
        return super().form_valid(form)