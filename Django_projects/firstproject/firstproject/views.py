from django.shortcuts import render
from django.http import HttpResponse

def wattsup(respond):
    return HttpResponse("<h1>This is my wattsup</h1>")

def facebook(respond):
    return HttpResponse("<h2>This is my facebook page</h2>")

def index(request):
    x = 20
    y = 50
    return HttpResponse(f'sum of two number is:{x+y}')

