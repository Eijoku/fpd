from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет мир!Вы на главной странице опроса.")

