from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null = True, blank=True)
    role = models.CharField(max_length=20, choices=(
        ('admin', 'Admin'),
        ('user', 'User'),
    ), default='user')

    def __str__(self):
        return self.username
    