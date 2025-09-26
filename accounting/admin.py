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
  list_display = all_fields(TransactionLine)
  list_select_related = ['transaction_id', 'account_id']

@admin.register(BalanceSheet)
class BalanceSheetAdmin(admin.ModelAdmin):
  list_display = all_fields(BalanceSheet)
  list_select_related = ['account_id']

@admin.register(MonthlyBalance)
class MonthlyBalanceAdmin(admin.ModelAdmin):
  list_display = all_fields(MonthlyBalance)