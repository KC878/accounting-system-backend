from rest_framework import serializers 
from accounting.models import Users, Account, Transaction, TransactionLine, BalanceSheet, MonthlyBalance

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users # model to serialize
    #fields = '__all__' # all the fields 

    fields = ["password", "username", "first_name", "last_name", "email", "sex"]
    extra_kwargs = {
      "password": {"write_only": True} # don't expose in response  
    }

    
# validation for email
  def validate_email(self, value):
    if Users.objects.filter(email=value).exists():
      raise serializers.ValidationError("Email already exists.")
    return value
  
  # user with hashed password
  def create(self, validated_data):
    user = Users(
      username=validated_data["username"],
      email=validated_data["email"],
      first_name=validated_data.get("first_name"),
      last_name=validated_data.get("last_name"),
      sex=validated_data.get("sex"),
    )

    user.set_password(validated_data["password"]) # hash password
    user.save()

    return user

  
  def update(self, instance, validated_data):
    if "password" in validated_data:
      instance.set_password(validated_data.pop("password"))
    return super().update(instance, validated_data)


class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField(write_only=True)




#AccountSerializer (read-only)
class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = ['id', 'account_name', 'account_type', 'normal_balance']  # accept this defined text 



#TransactionLineSerializer (nested inside transaction)
class TransactionLineSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(write_only=True)  # input only --> receive 
    account = AccountSerializer(read_only=True)  # output only --> output

    class Meta:
        model = TransactionLine
        fields = ['account', 'account_name', 'debit_amount', 'credit_amount', 'notes']


#TransactionSerializer (main parent)
class TransactionSerializer(serializers.ModelSerializer):
  created_by = serializers.SlugRelatedField( # syntax to look for related field 
    slug_field='username',  # lookup by username
    queryset=Users.objects.all() 
  )
  transaction_lines = TransactionLineSerializer(many=True)

  class Meta:
    model = Transaction
    fields = ['id', 'created_by', 'transaction_date', 'description', 'transaction_lines']

  def create(self, validated_data):
    lines_data = validated_data.pop('transaction_lines')
    transaction = Transaction.objects.create(**validated_data)

    for line_data in lines_data:
        account_name = line_data.pop('account_name')
        account, _ = Account.objects.get_or_create(account_name=account_name)
        TransactionLine.objects.create(transaction=transaction, account=account, **line_data)

    return transaction


