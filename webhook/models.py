# models.py
from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    what_date = models.CharField(max_length=255)
    other_specific_date = models.JSONField()
    what_services = models.CharField(max_length=255)

    def __str__(self):
        return f"Application for {self.user.email}"
