from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content': "hello i am from firstapp"}
    return render(request,'first_app/index.html', context = my_dict)