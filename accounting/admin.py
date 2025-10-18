from django.contrib import admin
from . models import Users, Account, Transaction, TransactionLine, BalanceSheet, MonthlyBalance
from utils.all_fields import all_fields

### 


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
  list_display = all_fields(Users)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
  list_display = all_fields(Account)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
  list_display = all_fields(Transaction)

@admin.register(TransactionLine)
class TransactionLinesAdmin(admin.ModelAdmin):
  list_display = ('id', 'transaction_id', 'account_id', 'account_display', 'transaction_display', 'debit_amount', 'credit_amount', 'notes')
  list_select_related = ['transaction', 'account']

  # show human-readable account
  def account_display(self, obj):
      return str(obj.account)
  account_display.short_description = 'Account'


  def transaction_display(self, obj):
      return str(obj.transaction)
  transaction_display.short_description = 'Transaction'


@admin.register(BalanceSheet)
class BalanceSheetAdmin(admin.ModelAdmin):
  list_display = all_fields(BalanceSheet)
  list_select_related = ['account']

@admin.register(MonthlyBalance)
class MonthlyBalanceAdmin(admin.ModelAdmin):
  list_display = all_fields(MonthlyBalance)