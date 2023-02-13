from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): #putting request in the parameter is meaningless, you can put anything in here really.
    my_dict = {"insert_me":"Now i am coming from first_app/index.html!"}
    return render(request,'first_app/index.html',context = my_dict)