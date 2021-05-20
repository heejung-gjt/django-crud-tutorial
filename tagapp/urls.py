from django.contrib import admin
from django.urls import path
from tagapp import views

app_name = 'tag'

urlpatterns = [
    
    # tag
    path('tag/<int:article_pk>', views.tag, name='tag'),

]
