from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.Prefetch)
    company_name = models.CharField(max_length=100)
    full_address = models.CharField(max_length=255)

    def __str__(self):
        return f"Client: {self.company_name}"
