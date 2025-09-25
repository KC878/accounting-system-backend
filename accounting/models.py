from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Users(AbstractUser):
  ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('accountant', 'Accountant'),
  ]

  role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='accountant')




class Account(models.Model):
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


class Monthly_Balance(models.Model):
  month_end = models.DateField(auto_now=False, null=False, blank=False)
  total_assets = models.DecimalField(max_digits=15, decimal_places=2)
  total_liabilities = models.DecimalField(max_digits=15, decimal_places=2)
  total_equity = models.DecimalField(max_digits=15, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)

  
class Balance_Sheet(models.Model):
  account_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
  balance_date = models.DateTimeField(auto_now_add=True)
  debit_balance = models.DecimalField(max_digits=15, decimal_places=2, null=True, default=0)
  credit_balance = models.DecimalField(max_digits=15, decimal_places=2, null=True, default=0)


class Transaction(models.Model):
  created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
  transaction_date = models.DateField(default=timezone.now)
  description = models.CharField(max_length=255, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

class Transaction_Line(models.Model):
  transaction_id = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=True)
  account_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
  debit_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, default=0)
  credit_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, default=0)
  notes = models.CharField(max_length=255)


