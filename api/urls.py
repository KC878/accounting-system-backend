from django.urls import path
from . import views

urlpatterns = [
  path('', views.getData),
  path('api/users/register', views.addUser),
  path('api/users/login', views.userLogin),
  path('api/users/logout', views.userLogout),
]