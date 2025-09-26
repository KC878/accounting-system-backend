from django.db import models
from accounting.models import Transaction, Users, Account
# Create your models here.


class UserLog(models.Model):
  USER_ACTION_CHOICES = [
    ('login', 'LOGIN'),
    ('logout', 'LOGOUT'),
    ('created', 'CREATED'),
    ('updated', 'UPDATED'),
    ('deleted', 'DELETED'),
    ('change_password', 'CHANGE_PASSWORD'),
    ('role_change', 'ROLE_CHANGE')
  ]

  user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='logs_as_user')
  action = models.CharField(max_length=20, choices=USER_ACTION_CHOICES)
  field_changed = models.CharField(max_length=25)
  old_value = models.CharField(max_length=255, blank=True)
  new_value = models.CharField(max_length=255, blank=True)
  changed_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='logs_as_changer')
  created_at = models.DateTimeField(auto_now_add=True)
  ip_address = models.GenericIPAddressField(null=True, blank=True)
  is_active = models.BooleanField(default=True) #soft delete

  def __str__(self):
    return f"{self.action} by {self.created_by} on {self.created_at}"
  
  class Meta:
    indexes = [
      models.Index(fields=['user']),
      models.Index(fields=['changed_by']),
      models.Index(fields=['created_at']),
    ]


class AccountLog(models.Model):
  ACCOUNT_ACTION_CHOICES = [
    ('created', 'CREATED'),
    ('updated', 'UPDATED'),
    ('deleted', 'DELETED')
  ]

  account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='account_logs')
  action = models.CharField(max_length=10, choices=ACCOUNT_ACTION_CHOICES)
  field_changed = models.CharField(max_length=25)
  old_value = models.CharField(max_length=255, blank=True)
  new_value = models.CharField(max_length=255, blank=True)
  created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='account_logs_created')
  created_at = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=True)
  
  def __str__(self):
    return f"{self.action} by {self.created_by} on {self.created_at}"
  
  class Meta:
    indexes = [
      models.Index(fields=['account']),
      models.Index(fields=['created_by']),
      models.Index(fields=['created_at'])
    ]

class TransactionLog(models.Model):
  transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=True, related_name='transaction_logs')
  account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='transaction_logs')
  debit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=True)
  credit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=True)
  description = models.CharField(max_length=255, null=True, blank=True)
  reference_no = models.CharField(max_length=25, null=True)
  created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='transaction_logs_created')
  created_at = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=True)
  class Meta:
    indexes = [
      models.Index(fields=['transaction']),
      models.Index(fields=['account']),
      models.Index(fields=['created_by']),
      models.Index(fields=['created_at']),
    ]

