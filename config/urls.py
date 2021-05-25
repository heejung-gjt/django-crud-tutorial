from django.contrib import admin
from django.urls import path, include
from userapp import views

urlpatterns = [
    path('',views.home, name='home'),
    path('admin/', admin.site.urls),
    path('user/',include('userapp.urls')),
    path('blog/',include('blogapp.urls')),
    path('follow/',include('followapp.urls')),  
    path('tag/',include('tagapp.urls')),
]


