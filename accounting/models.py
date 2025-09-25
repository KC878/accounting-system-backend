from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
  ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('accountant', 'Accountant'),
  ]

  role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='accountant')




class Accounts(models.Model):
  ACCOUNT_TYPE_CHOICES = [
    ('asset', 'Asset'),
    ('liability', 'Liability'),
    ('equity', 'Equity'),
    ('revenue', 'Revenue'),
    ('expenses', 'Expenses'),
  ]

  NORMAL_BALANCE_CHOICES = [
    ('debit', 'Debit'),
    ('credit', 'Credit'),
  ]

  account_name = models.CharField(max_length=50)
  account_type = models.CharField(max_length=15, choices=ACCOUNT_TYPE_CHOICES)
  normal_balance = models.CharField(max_length=10, choices=NORMAL_BALANCE_CHOICES)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  
