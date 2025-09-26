from django.contrib import admin
from . models import UserLog, AccountLog, TransactionLog
from utils.all_fields import all_fields
# Register your models here.


@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
  list_display = all_fields(UserLog)

@admin.register(AccountLog)
class AccountLogAdmin(admin.ModelAdmin):
  list_display = all_fields(AccountLog)

@admin.register(TransactionLog)
class TransactionLogAdmin(admin.ModelAdmin):
  list_display = all_fields(TransactionLog)