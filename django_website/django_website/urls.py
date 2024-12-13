"""
URL configuration for django_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls")), # the include function chops off the part that has been matched with the user input in the url section of the browser which is blog in this case and sends the remaining part from the string. So here blog will be removed and only an empty string will be sent to the urls module of the blog which represents the home page
    # if you want to change the route of the blog app, you can just change it here once (from blog/ to blog_dev/ or something and then all the routes of the blogs app will be accessible via blog_dev)
    # if we put the forward slash after the route name, it will redirect the user to the route whether the user puts the forward slash after the route name or not (always put the forward slash after the route name)
    # if we want that the user doesn't even have to put blog to reach the blog app then we can just keep the route name an empty string and it will get matched with the empty string in the urls module of the blog app, this will make the blog home the entire app's home page
]

# whenever we enter a url, first it comes here to check if the entered url matches any url pattern mentioned here, if it does then it goes to the urls.py file of our blog project, looks for the url pattern, then it goes to the views module and runs the function associated with the url that has matched with the entered url