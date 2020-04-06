from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def hello_word(request):
    return HttpResponse("hello word")
