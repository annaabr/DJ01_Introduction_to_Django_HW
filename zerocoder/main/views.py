from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Главная страница сайта на Django</h1>")

def index_data(request):
    return HttpResponse("<h1>Это страница DATA</h1>")

def index_test(request):
    return HttpResponse("<h1>Это страница TEST</h1>")