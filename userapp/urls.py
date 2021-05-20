from django.contrib import admin
from django.urls import path
from userapp import views

app_name = 'user'

urlpatterns = [
    # user
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('my_page/<int:user_pk>',views.my_page, name='my_page'),
]
