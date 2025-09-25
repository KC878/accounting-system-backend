from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
  ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('accountant', 'Accountant'),
  ]

  role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='accountant')