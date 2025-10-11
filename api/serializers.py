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
