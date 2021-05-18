from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import time
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=CASCADE, related_name='profile')
  nickname = models.CharField(max_length=64)
  intro = models.TextField()

  def __str__(self):
    return self.user.username


class Follow(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='follow')
  followers = models.ManyToManyField(User, blank=True, related_name='following')


class Category(models.Model):
  name = models.CharField(max_length=32)

  def __str__(self):
    return self.name

class Article(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, related_name='article')
  writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
  title = models.CharField(max_length=64)
  content = models.TextField()
  create_at = models.TextField(default=time.time())
  modify_at = models.DateTimeField(auto_now_add=True)
  is_deleted = models.BooleanField(default=False)
  

class Tag(models.Model):
  name = models.CharField(max_length=64, unique=True)
  articles = models.ManyToManyField(Article, blank=True, related_name='tag')