from django.contrib import admin
from . models import Users, Account, Transaction, Transaction_Line, Balance_Sheet, Monthly_Balance
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

@admin.register(Transaction_Line)
class Transaction_LinesAdmin(admin.ModelAdmin):
  list_display = all_fields(Transaction_Line)
  list_select_related = ['transaction_id', 'account_id']

@admin.register(Balance_Sheet)
class Balance_SheetAdmin(admin.ModelAdmin):
  list_display = all_fields(Balance_Sheet)
  list_select_related = ['account_id']

@admin.register(Monthly_Balance)
class Monthly_BalanceAdmin(admin.ModelAdmin):
  list_display = all_fields(Monthly_Balance)