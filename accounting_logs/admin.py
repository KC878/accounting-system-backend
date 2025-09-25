from django.contrib import admin
from . models import User_Log, Account_Log, Transaction_Log
from utils.all_fields import all_fields
# Register your models here.


@admin.register(User_Log)
class User_LogAdmin(admin.ModelAdmin):
  list_display = all_fields(User_Log)

@admin.register(Account_Log)
class Account_LogAdmin(admin.ModelAdmin):
  list_display = all_fields(Account_Log)

@admin.register(Transaction_Log)
class Transaction_LogAdmin(admin.ModelAdmin):
  list_display = all_fields(Transaction_Log)