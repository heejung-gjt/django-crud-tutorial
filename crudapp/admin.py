from django.contrib import admin
from .models import Profile, Follow, Article, Category, Tag
# Register your models here


admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
