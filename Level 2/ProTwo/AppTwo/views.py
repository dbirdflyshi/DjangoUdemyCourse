from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(response):
    return render(response,'AppTwo/index.html')

def help(response):
    dict = {"text":"THIS IS A TEXT HELP PAGE"}
    return render(response,'AppTwo/help.html', context = dict)

def users(response):
    user_list = User.objects.order_by('FirstName')
    user_dict = {'Users':user_list}
    # print(user_dict)
    return render(response,'AppTwo/users.html',context = user_dict)