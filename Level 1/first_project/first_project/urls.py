"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app import views # for this course, this is only here to link it to the index of the site
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index, name = 'index'), # this links to the `from first_app import views` code
    path("home/",include('first_app.urls')), # if we wanted to link urls from a project to an app, we can do that here, it's cleaner to do it this way
]
