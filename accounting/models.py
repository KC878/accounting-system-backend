from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError

MONEY_MAX_DIGITS = 15
MONEY_DECIMAL_PLACES = 2

class Users(AbstractUser):
  ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('accountant', 'Accountant'),
  ]
  SEX_CHOICES = [
    ('male', 'male'),
    ('female', 'female'),
  ]

  role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='accountant')
  sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='')


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

  def __str__(self):
    return self.account_name


class MonthlyBalance(models.Model):
  month_end = models.DateField(auto_now=False, null=False, blank=False)
  total_assets = models.DecimalField(max_digits=MONEY_MAX_DIGITS, decimal_places=MONEY_DECIMAL_PLACES)
  total_liabilities = models.DecimalField(max_digits=MONEY_MAX_DIGITS, decimal_places=MONEY_DECIMAL_PLACES)
  total_equity = models.DecimalField(max_digits=MONEY_MAX_DIGITS, decimal_places=MONEY_DECIMAL_PLACES)
  created_at = models.DateTimeField(auto_now_add=True)

  @property
  def total_liabilities_and_equity(self):
    return self.total_liabilities + self.total_equity

  def clean(self):
    if self.total_assets != self.total_liabilities + self.total_equity:
      raise ValidationError("Assets must equal Liabilities + Equity")

  
class BalanceSheet(models.Model):
  account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='balance_sheets')
  balance_date = models.DateTimeField(auto_now_add=True)
  debit_balance = models.DecimalField(max_digits=MONEY_MAX_DIGITS, decimal_places=MONEY_DECIMAL_PLACES, null=True, default=0)
  credit_balance = models.DecimalField(max_digits=MONEY_MAX_DIGITS, decimal_places=MONEY_DECIMAL_PLACES, null=True, default=0)

  def total_balance(self):
    return (self.debit_balance or 0) - (self.credit_balance or 0)


class Transaction(models.Model):
  created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='transactions')
  transaction_date = models.DateField(default=timezone.now)
  description = models.CharField(max_length=255, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  #soft delete 
  #when transaction is null = is_active set to false
  is_active = models.BooleanField(default=True) 

  class Meta: 
    ordering = ['-transaction_date']
    indexes = [
      models.Index(fields=['transaction_date']),
      models.Index(fields=['created_by']),
    ]
  
  def __str__(self):
    return self.description

class TransactionLine(models.Model):
  transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=True, related_name='transaction_lines')
  account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='transaction_lines')
  debit_amount = models.DecimalField(max_digits=MONEY_MAX_DIGITS, decimal_places=MONEY_DECIMAL_PLACES, null=True, default=0)
  credit_amount = models.DecimalField(max_digits=MONEY_MAX_DIGITS, decimal_places=MONEY_DECIMAL_PLACES, null=True, default=0)
  notes = models.CharField(max_length=255, blank=True)

  # rejects if entered at database debit and credit are 0 both
  class Meta:
    constraints = [
        models.CheckConstraint(
            check=~(models.Q(debit_amount=0) & models.Q(credit_amount=0)),
            name='debit_or_credit_nonzero',
        )
    ]



