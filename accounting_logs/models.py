from django.db import models
from accounting.models import Transaction, Users, Account
# Create your models here.


class User_Log(models.Model):
  USER_ACTION_CHOICES = [
    ('login', 'LOGIN'),
    ('logout', 'LOGOUT'),
    ('created', 'CREATED'),
    ('updated', 'UPDATED'),
    ('deleted', 'DELETED'),
    ('change_password', 'CHANGE_PASSWORD'),
    ('role_change', 'ROLE_CHANGE')
  ]


  user_id = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='logs_as_user')
  action = models.CharField(max_length=20, choices=USER_ACTION_CHOICES)
  field_changed = models.CharField(max_length=25)
  old_value = models.CharField(max_length=255)
  new_value = models.CharField(max_length=255)
  changed_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='logs_as_changer')
  created_at = models.DateTimeField(auto_now_add=True)


class Account_Log(models.Model):
  ACCOUNT_ACTION_CHOICES = [
    ('created', 'CREATED'),
    ('updated', 'UPDATED'),
    ('deleted', 'DELETED')
  ]

  account_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
  action = models.CharField(max_length=10, choices=ACCOUNT_ACTION_CHOICES)
  field_changed = models.CharField(max_length=25)
  old_value = models.CharField(max_length=255)
  new_value = models.CharField(max_length=255)
  created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)


class Transaction_Log(models.Model):
  transaction_id = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=True)
  account_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
  debit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=True)
  credit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=True)
  description = models.CharField(max_length=255)
  reference_no = models.CharField(max_length=25, null=True)
  created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

