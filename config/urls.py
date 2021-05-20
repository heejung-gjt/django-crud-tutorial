from django.contrib import admin
from django.urls import path, include
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('userapp.urls')),
    path('blog/',include('blogapp.urls')),
    path('follow/',include('followapp.urls')),  
    path('tag/',include('tagapp.urls')),
]


