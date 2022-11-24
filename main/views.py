from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1>hello guys</h1> ")

# Create your views here.
