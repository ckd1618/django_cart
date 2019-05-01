from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  text_var = 'my first django web page'
  return HttpResponse(text_var)


