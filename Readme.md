# Django Project Notes

## Level 1

### Creating virtual environments
You can create a virtual environment by doing the following in the cmd prompt

`conda create --name <environment name> <package name>`

`conda create --name mydjangoenv django`

You can then start using your package by typing this in the cmd prompt

`conda activate <env name>`

You can stop the environment by using this prompt

`conda deactivate`

You can view all envs by doing this

`conda info --envs`

### New project creation
Create a new project by doing this command in an empty folder

`django-admin startproject <project_name>`

### When you create a new project, the following files get created : 
Folder : project name
1. `__init__.py` : blank file, lets python know that the directory can be treated as a package
2. `asgi.py` : application server gateway interface. No notes on this one, probably same as wsgi 
3. `settings.py` : Where you will store all the project settings 
4. `urls.py` : stores all url patterns for project, all pages in your web app 
5. `wsgi.py` : script that acts as a web server gateway inferface. It helps us deploy the app to productionn
Outside folder:
1. `manage.py` : script that allows you to handle all of the core function of the django project

### When you want to start the server, you can run the following command:
`python manage.py runserver `

You can quit the server by using CTRL-BREAK in the cmd 

From here, you can paste the localhost url to see the web app live

`http://127.0.0.1:8000/`

### The difference between a project and an app
1. Django project : collection of applications and configurations that when combined together make up the full web application
2. Django application: performs a particular functionality for your entire web application. For example you could have a registration app, polling app, comments app, etc. 
** Django apps can be plugged into other django projects so you can reuse them, or other peoples apps**

### Creating a new app 
When you want to create a new app, you need to write the following command 

`python manage.py startapp <app_name>`

When this happens, a new folder will be generated with the following structure
1. migrations folder : stores database specific information as it relates to the models 
2. __init__.py : blank file, lets python know that the directory can be treated as a package
3. admin.py : register your models to allow django to use them with the admin interface
4. apps.py : place application specific configuration
5. models.py : store applications data models and entity relationships
6. tests.py : store test functions
7. views.py : store functions that handle requests and return responses

** Whenever you make a new app, you must add it to the list `installed apps` in the project folder under the settings.py file. **

### Making a new view
In your app, open the views.py file and make a new function

**If you want to link your views directly to your project from an app, you gotta do these things**

1. navigate to urls.py in the project folder and import your app using the template `from <app folder name> import views`. Views is the py file and <app folder name> is the name of the folder the views.py file lives in.
2. while in the urls.py file, modify the url_patterns list and add the function you made in there using the template `path("",views.<function name>, name = <name of your view you want>)`

**If you want to link your views by the app, you gotta do this. RECOMMENDED**

1. in your app folder, make a new file called urls.py
2. in your app folder urls.py file, import these packages `from django.urls import path` for using the path function and `from <app name> import views` to connect this py file to the views.py file in your <app name> folder
3. create the url patterns list and add this entry `path("",views.index,name="index"),` to the list. 
4. in your project folder, open up the urls.py file and import this package `from django.conf.urls import include`

### Using Templates
Templates are the best way to organize your HTML so that is modular. Unfortunately, django does not come this way out of the box so we gotta do some manipulations to include templates. 
1. Create a new folder in the project directory called `templates`
2. Create a new folder in the templates directory of the name of the app we are making this template for
3. Create an html file in that folder
4. In the project directory, open up the settings.py file and make these changes 
    1. Get the OS package installed `import os`
    2. Make a new variable `TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")`
    3. Add the TEMPLATE_DIR variable to the DIRS section of the Templates list like this `"DIRS": [TEMPLATE_DIR,],`

### Using django html tags 
A Django HTML tag is a piece of django code that allows you to incorporate python logic into your html code. In order to do that, you need these things
1. In the app directory, open the views.py file and import render `from django.shortcuts import render`
2. At the end of your function return the output like this `return render(<function parameter name>, '<app name>/<html file name>.html', context = <info you want to display>)`
3. Navigate to the project directory and go to the templates folder and your app folder and open the html file and here you can insert what you want using double curly braces `{{<whatever>}}`


### Handling static files
When we want to handle static files, we have to do a lot of connections and create more folders
1. Make a folder on the root called `static`
2. Connect the static files variable in the settings.py file of the project folder: `STATIC_DIR = os.path.join(BASE_DIR,"static")`
3. Create a static file directories list `STATICFILES_DIRS` in the `settings.py` file and add the `STATIC_DIR` variable to that list 
4. Here's what to do if you want to add images:
    1. Add image to images folder 
    2. In html page you want to display the image, you have to have the following code on top `{% load static %}`
    3. Add the image you want with the template tag `<img src="{%static 'images/<image>.jpg' %}" alt = "<whatever you want">`
5. Here's what to do if you want to add files like css
    1. Add the following in your head `<link rel="stylesheet" href="{% static 'css/mystyle.css'%}"/>`


### Building models
Models help django handle data. Models are just database tables.. 
1. Inside of the app folder, open the models.py file and create classes, these represent the architecture of a database table. 
`class <Class Name>(models.Model):`
    `<field name>= models.<datatype>(<datatype parameters>)`
    `def __str__(self): //string representation, not too sure what that is...`
        `return self.top_name`
2. After you make your classes and save the file go into the console and run the migration `python manage.py migrate`
3. After it's done, you gotta migrate the app, the first one was migrating the project `python manage.py makemigrations <app name>`
4. Finally, concrete the migrations in the project level again `python manage.py migrate`

### Interacting with your project
You can interact with your project using the shell. 

- You can access the shell by using the command in CMD `python manage.py shell`
- Query a model `print(<model_name>.objects.all())`
- On top of `.all`, you can do these :
    1. `.get`
    2. `.filter`
    3. `.exclude`
- You can specify specific parameters with how you want to find things using these methods:
    1. `exact` / `iexact` (case sensitive/insensitive) 
    2. `contains` / `icontains`
    3. `startswith` / `istartswith`
    4. `endswith` / `iendswith`
- Some examples on how to find items 
    1. `<model>.<field_name>`
    2. `<model>.objects.get(pk=<key number>).<field_name>`
    3. `<model>.objects.filter(<field_name>__icontains==<content>).exclude(<field_name2>__icontains=<content>)[0].<field_name>`
- Add a new entry to a model `<Model_name>(<field_name> = <content>).save`
    - alternatively, you can do it this way: `<model_name>.objects.create(<field name> = <content>, <other field> = <content>)`
- Quit the shell:    `quit()`

### The admin interface
An easier way to interface with your models is by using the django admin interface. 

In order to do this though, there's some setup that needs to happen. 
1. In your app folder, open up the `admin.py` file 
2. Import your models `from <app_name>.models import <model1>,<model2>`
3. Register your models `admin.site.register(<model1>)`
4. Create a superuser. From the console: `python manage.py createsuperuser` and fill out the username and password

### Working with forms 
When working with forms, you can use django's built in form functionality. 

You first need a `forms.py` file created in the app directory and import these packages `from django import forms`

Then you need to create a new form class `class <form name>(forms.Form):`

and inside of the class, put all the form components you want `<component name> = forms.<field component type>()`

After that, you can input this form inside the `<body>` of your HTML page by doing this : 

```html
<form method = 'post'>

{{form.as_p}}

{% csrf_token %}
```

and then some sort of button to ingest it : `<input type="submit" class = "btn btn-primary" name = '' value = 'Submit'>`

### Validating forms
You can validate form fields to prevent unwanted input. You can do many things like stop bots, enforce formatting, etc
Inside of your forms.py file, import this package `from django.core import validators`

Bot Prevention
: One way to prevent bots is to hide a form component `botcatcher = forms.CharField(required=False, widget = forms.HiddenInput)`
: Inside your botcatcher form component, you can add the specific validation `validators = [validators.MaxLengthValidator(0)]`. The logic behind it is that if it's hidden, only a bot would try to fill out the form. Therefore, it won't successfully submit and process the form fillout because the bot filled out the form with a validation of "invalid if the field has more than 0 characters inside"

Custom Validation
: You can even validate things yourself. First thing you need to do is make a new function outside of the form class 
``` python
    def <validation function name>(value):
        if <validation logic>:
            raise forms.ValidationError("<validation message>")
```

: You can do better validation through the clean function. First you create a clean data object using `cleaner = super().clean()` and then clean each field `field = cleaner['field']` once that's clean you can validate whatever rules you want. Finally you can raise errors 
``` python 
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("emails don't match")
```

### Storing form values to a model
This is a little different than the notes above. What you have to do is make the model first and the form will populate all the model fields automatically. 

1. Open up the `forms.py` file or make it first if you haven't yet and import the model(s) `from <app name>.models import <model>`
    1. Create a new class naming it whatever you want the form name to be with the parameter `forms.ModelForm` so it looks like this `class <form name>(forms.ModelForm):`
        1. Create a subclass called `Meta`
        2. Inside add `model = <model name>`
        3. Also, add `fields = [<field list>]` 
            - if you want to include all fields from the model, replace the `[<field list>]` with `'__all__'`
2. Open the `views.py` file
    1. Import the name of the form you made in the `forms.py` file `from <app name>.forms import <form name>`
    2. Create a new function of the page you want this form to live in `def <view name>(request)`
    3. Make an `if` statement to catch if the form was submitted
        - `form = <form name>(request.POST)`
        - Then create a form object using the form you imported earlier `form = <form name>()`
    4. Inside the `if` statement, make a second `if` statement to check if that submitted form is valid
        - `if form.is_valid():`
    5. If the submitted form is valid, save the form to the model `form.save(commit = True)` and go back to the pain page `return index(request)` 
    6. If the form is invalid, you can do whatever you want, for this example, we just printed 'Invalid form' `print('form invalid')`
    7. Finally, we'll return the page with the form.
        - `return render(request,'<app name>/<page with form>.html',{'form':form})`
3. Open the html page where you want the form to be
    1. Create the form in html and set the method to 'POST' so we can track submission 
        - `<form method = 'POST'>`
    2. Inside the form tag, include the django template tag to call the form and make the components vertical rather than horizontal 
        - `{{ form.as_p }}`
    3. Inside the form tag, Include the token 
        - `{% csrf_token %}`
    4. Inside the form tag, Create a submit button 
        - `<input type="submit", value = "Submit">`
4. Now everything should be already good to go and connected, go ahead and test it is working.

### Relative URLs
Relative URLs are good for when you want to set up a second level and interchange your apps between projects. With it, you have your urls living inside of your app which then that url file connects to the urls file in the project. 

In order to do that, you must do the following:
1. In your app folder, create a `urls.py` file
    1. Import your views `from <app_name> import views`
    2. Import the path and include functions from the django package `from django.urls import path,include`
    3. Set the namespace by creating a variable called `APP_NAME` and tie it to the name of the app `app_name = '<name of your app>'`
    4. Create your url list `urlpatterns = []` like in the project folder version and include the views you made in the views file and of those, which ones you want to live in the app directory
2. In the project folder, modify the `urls.py` file 
    1. Add the relative path linking both urls files to your urlpatterns list `path("<app name>/", include('<app name>.urls'))`
3. When referencing this in your html, you gotta do these
    1. Instead of a link in your html, you gotta use this `{% url '<variable from the APP_NAME designation>:<view_name>' %}`. Full example for an anchor tag is here: `<a href="{% url 'basic_app:other' %}">The other page</a>`

### Template inheritance/extension 
You can create html components and call them in other html files for ultimate reusability. 

In order to do this, you have to set your code up with the following:
1. In your templates folder, create a new html file that houses your inheritable html code, like a nav bar, or your entire webpage structure.. 
2. Inside of the newly created html file, build out everything you want to be inherited across your other html files
3. Where you want the other code from other html files to populate, write the following template tag: `{% block <block_name> %}`
    - for `<block_name>`, you can put whatever you want, just know that it is what will be reused elsewhere
4. Close it out with the endblock template tag `{% endblock %}`
5. In your other html files, include only the `<!DOCTYPE html>`
6. While still in the other html file, add the template tag that calls your inheritable code `{% extends "<app_name>/<inheritable html file name>.html" %}`
7. Under that, put this `{% block <block_name> %}`
8. Insert all the html you want for this page
9. To close out the inheritable html, add `{% endblock %}`


### Template filters
You can use template filters to make modifications and changes to context dictionaries right inside of the html. 

There are many preset functions inside django also with the ability to make your own. 

To use a prebuilt function
: You can view all the functions here : https://docs.djangoproject.com/en/4.1/ref/templates/builtins/
: A prerequisite to use template filters is that you must pull in a context dictionary.
: Assuming your view has a context dictionary, you can put the following code to make a filter `{{ <dictionary_key>|<function>:<argument>}} `. A full example is like this : `{{ text|cut:'world' }}`

To make your own function
: It is best practice to make a new folder inside of your app directory called `templatetags` and put a file in there with all your template tag functions. For the udemy course that is used to make these notes, it was instructed to call the file `my_extras.py`. 
: Inside of the template tag python file, you have to do some housekeeping before making the functions. First thing to do is import the template package from django `from django import template`
: Next you have to create the registration object to register your newly created functions to the function library `register = template.Library()`
: Make your function. Here's an example 
``` python
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.astype(str).replace(arg,'')
```
: When you are done with your function, you have to register it to the registry object made in the previous step above. You can do so through decorators `@register.filter(name = '<function name>')`. A full example would look like this `@register.filter(name = 'cut')`.

### Passwords and authentication
** Some extra housekeeping **
- Add a new folder to the root directory `media`. The difference between static and media is that media is content owned by the end user and static is content owned by the admin

1. Install the package `bcrypt` and `django[argon2]`
2. Add password hashers. The order matters because if one fails or isn't installed in the server, it will default down a level
``` python 
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]
```
3. Inside of the password validators section, you can add more options if you like by adding the code inside of a specific rule you want to augment. `'OPTIONS':{'min_length':9}`

### Deployment
There are many options to deploy your projects. Python anywhere is the service we use in the course. 

In order to deploy, there are quite a few steps needed. 
1. Create an account in pythonanywhere
2. Set up your virtual environment 
    1. Open the console tab
    2. Select Bash
    3. type `mkvirtualenv --python=python<version> <name_of_environment>`
        - if you need to, you can see what packages are installed with `pip list`
3. Install all of the packages you might need. 
    - django `pip install django`
    - pillow `pip install pillow`
    - argon2 `pip install django[argon2]`
    - you can validate django is installed by running this command `which django-admin.py`
4. Get your git project `git clone <your repository>`
    - you can type `ls` to view your directory
5. Make your migrations 
    - `python manage.py migrate`
    - `python manage.py makemigrations`
    - `python manage.py migrate`
6. Create your superuser if you haven't yet
    - `python manage.py createsuperuser`
7. Set up your web app
    1. Go to dashboard > web > add a new web app and follow instructions there
    2. after clicking next, select `manual configuration` and select the python version you set in your virtual env
    3. after clicking next, it will take you to the web tab, now we will modify the settings 
    4. Go to virtualenv section and click `enter path to a virtual env` and fill out the text box
        - `/home/<username>/.virtualenvs/<virtualenv name>`
    5. go to code section and click `enter the path to your web app source code` and fill out the text box
        - `/home/<username>/<git repo name>/<project name>`
8. Modify the WSGI 
    - Click on the path under `WSGI configuration file:` and we will modify it 
    1. Delete all the hello world stuff
    2. Go to django section and uncomment these items
        - `import os`
        - `import sys`
        - `path`
        - `if path` 
    3. Modify the path variable and replace it with `/home/<username>/<git repo name>/<project name>`
    4. Add a new line under the `if path` and put `os.chdir(path)`
    5. Under that, put `os.environ.setdefault("DJANGO_SETTINGS_MODULE","<project name>.settings")`
    6. Under that, put `django.setup()`
    7. Uncomment `from django.core.wsgi import get_wsgi_application`
    8. Uncomment `application = get_wsgi_application()`
    9. Save
9. Connect your static files
    1. Go to files tab and create a new directory called `static`
    2. In the web tab, go to the static files section
    3. Create the connection to your admin panel static files
        1. url : `/static/admin`
        2. directory: `/home/<username>/.virtualenvs/<virtualenv name>/lib/python<version>/site-packages/django/contrib/admin/static/admin`
    4. Create the connection to your main static files
        1. url : `/static/`
        2. directory: `/home/<username>/<repository>/<project>/static`
10. Allow pythonanywhere to host your project
    1. Navigate to files tab and under directories click your repo, project and modify your `settings.py` file
        - in the file, go to the `ALLOWED HOSTS` portion of the code and add this entry to the list `<username>.pythonanywhere.com`
        - Save
9. Turn off debug
    1. In `settings.py` file, find `DEBUG` and change it from `True` to `False`
    2. Save
10. Reload
    1. Under web tab, click the big green button under `Reload` section