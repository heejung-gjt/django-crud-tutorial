    
from django.contrib import admin
from django.urls import path
from followapp import views

app_name = 'follow'

urlpatterns = [
  
  # follow
    path('follow/<int:user_pk>', views.follow, name='follow'),
]