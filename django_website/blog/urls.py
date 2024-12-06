from django.urls import path
from . import views # . means current directory

urlpatterns = [
    path('', views.home, name='blog-home'), # '' - home page, views.home will let the home function handle this route
    path('about/', views.about, name='blog-about'), # this route doesn't needs to be added to django website urls module, as whenever someone goes to blog, the request will reach here in this urls module and then this url module would take the user to the about page from here
]
