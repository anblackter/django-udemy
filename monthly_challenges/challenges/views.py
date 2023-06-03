from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This Works!")

def january(request):
    return HttpResponse("This is January!")

def february(request):
    return HttpResponse("This is February")
