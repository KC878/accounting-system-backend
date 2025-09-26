from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounting.models import Users
from . serializers import UserSerializer

@api_view(['GET'])
def getData(request):
  users = Users.objects.all()

  serializer = UserSerializer(users, many=True) #many=True: serialize multiple items

  return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
  serializer = UserSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)