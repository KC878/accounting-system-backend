from django.shortcuts import render
from django.http import HttpResponse
import datetime

def test(request):

  today = datetime.datetime.now().date()
 
  return render(request, "test.html", {"today": today})
