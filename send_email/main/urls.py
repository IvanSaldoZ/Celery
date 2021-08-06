from django.urls import path
from .views import ContactView, ContactListView

urlpatterns = [
    path('', ContactView.as_view(), name="contact"),
    path('contacts', ContactListView.as_view(), name="contact_list")
]