from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')


def say(request):
    return HttpResponse('Say Hi')


def sayhello(request):
    return HttpResponse('Say Hello')
