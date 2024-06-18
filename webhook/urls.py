from django.urls import path

from . import views

urlpatterns = [
    path("webhook/", views.jotform_webhook, name="jotform_webhook"),
]
