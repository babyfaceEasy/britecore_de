from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Insurer(AbstractUser):
    companyName = models.CharField(max_length=100)
    companyAddress = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
