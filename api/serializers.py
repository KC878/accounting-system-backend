from rest_framework import serializers 
from accounting.models import Users, Account, Transaction, TransactionLine, BalanceSheet, MonthlyBalance


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users # model to serialize
    fields = '__all__' # all the fields 