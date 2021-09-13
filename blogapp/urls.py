from django.contrib import admin
from django.urls import path
from blogapp import views

app_name = 'blog'

urlpatterns = [
 # blog
    # path('',views.home, name='home'),
    path('category/',views.category, name='category'),
    path('article_list/<int:category_pk>', views.article_list, name='article_list'),
    path('writer/',views.writer, name='writer'),
    path('article_detail/<int:article_pk>', views.article_detail, name='article_detail'),
    path('article_writer/<int:category_pk>', views.article_writer, name='article_writer'),
    path('article/edit/<int:article_pk>', views.article_edit,name='article_edit'),
]