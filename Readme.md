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
