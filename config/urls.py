"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('my_page/<int:user_pk>',views.my_page, name='my_page'),
    path('follow/<int:user_pk>', views.follow, name='follow'),
    path('category',views.category, name='category'),
    path('article_list/<int:category_pk>', views.article_list, name='article_list'),
    path('writer/',views.writer, name='writer'),
    path('article_detail/<int:article_pk>', views.article_detail, name='article_detail'),
    path('article_writer/<int:category_pk>', views.article_writer, name='article_writer'),
    path('tag/<int:article_pk>', views.tag, name='tag'),
]
