from django.db import models

# Create your models here.

class Users(models.Model):
  ROLE_ADMIN = 'admin'
  ROLE_ACCOUNTANT = 'accountant'
  ROLE_CHOICES = [
    (ROLE_ADMIN, "Admin"),
    (ROLE_ACCOUNTANT, 'Accountant')
  ]
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=255)
  role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=ROLE_ACCOUNTANT)
  email = models.EmailField(max_length=255, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  