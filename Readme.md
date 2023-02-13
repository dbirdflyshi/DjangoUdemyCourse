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
1. in your app, open the views.py file and make a new function
** If you want to link your views directly to your project from an app, you gotta do these things **
2. navigate to urls.py in the project folder and import your app using the template `from <app folder name> import views`. Views is the py file and <app folder name> is the name of the folder the views.py file lives in.
3. while in the urls.py file, modify the url_patterns list and add the function you made in there using the template `path("",views.<function name>, name = <name of your view you want>)`
** If you want to link your views by the app, you gotta do this. RECOMMENDED **
2. in your app folder, make a new file called urls.py
3. in your app folder urls.py file, import these packages `from django.urls import path` for using the path function and `from <app name> import views` to connect this py file to the views.py file in your <app name> folder
4. create the url patterns list and add this entry `path("",views.index,name="index"),` to the list. 
5. in your project folder, open up the urls.py file and import this package `from django.conf.urls import include`

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
