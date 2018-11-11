from django.shortcuts import render
from django.http import HttpResponse

def myView(reauest):
    return HttpResponse('Hello, World!')
