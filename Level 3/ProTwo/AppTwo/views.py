from django.shortcuts import render
from AppTwo.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html')

def help(request):
    dict = {"text":"THIS IS A TEXT HELP PAGE"}
    return render(request,'AppTwo/help.html', context = dict)

def users(request):
    form = NewUserForm()

    # If the submission brings back information and it's valid
    # we will save the form and send you back to the home page
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'AppTwo/users.html',{'form':form})