from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from accounting.models import Users
from . serializers import UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getData(request):
  users = Users.objects.all()

  serializer = UserSerializer(users, many=True) #many=True: serialize multiple items

  return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def addUser(request):
  serializer = UserSerializer(data=request.data)

  try:
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except Exception as err:
    return Response({"detail": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  