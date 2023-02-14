from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<em>My Second App</em>")

def help(response):
    dict = {"text":"THIS IS A TEXT HELP PAGE"}
    return render(response,'AppTwo/help.html', context = dict)