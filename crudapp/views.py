from crudapp.models import Follow, Profile,Category,Article
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
  users = User.objects.all()
  context = {
    'users':users
  }
  return render(request,'home.html',context)

def register(request):
  context = {
    'error':
    {
      'state':False,
      'msg':''
    }
  }
  if request.method == 'POST':
    userid = request.POST['id']
    password = request.POST['password']
    password_chk = request.POST['password_chk']
    nickname = request.POST['nickname']
    intro = request.POST['intro']
    user = User.objects.filter(username = userid)
    profile = Profile.objects.filter(nickname = nickname)
    if not userid or not password_chk or not password or not nickname or not intro:
      context['error']['state'] = True
      context['error']['msg'] = '내용을 입력해주세요'      
    if len(user) > 0:
      context['error']['state'] = True
      context['error']['msg'] = '아이디가 이미 존재합니다'
    if password != password_chk:
      context['error']['state'] = True
      context['error']['msg'] = '비밀번호가 틀립니다'     
    if len(profile) > 0:
      context['error']['state'] = True
      context['error']['msg'] = '이미 존재하는 닉네임입니다'
    
    if not context['error']['state']:
      user = User.objects.create_user(
        username = userid,
        password = password
      )
      Profile.objects.create(
        user = user,
        nickname = nickname,
        intro = intro
      )

      Follow.objects.create(
        user = user
      )
      auth.login(request, user)
      return redirect('home')

  return render(request,'register.html',context)


def login(request):
  context = {
  'error':
  {
    'state':False,
    'msg':''
  }
}
  if request.method == 'POST':
    userid = request.POST['id']
    pwd = request.POST['password']

    user = authenticate(username = userid, password = pwd)
    if user is  None:
      context['error']['state'] = True
      context['error']['msg'] = '아이디와 비밀번호를 확인해주세요'

    auth.login(request, user)
    return redirect('home')

  return render(request, 'login.html',context)


def logout(request):
  auth.logout(request)
  return redirect('home')


def my_page(request,user_pk):
  is_followed = False
  owner = User.objects.filter(pk = user_pk).first()
  follow = Follow.objects.filter(user__pk = user_pk).first()
  if request.user in follow.followers.all():
    is_followed = True
  context = {
    'owner':owner,
    'is_followed':is_followed,
    'followers':follow.followers.all()
  }
  return render(request,'my_page.html',context)


def follow(request, user_pk):
  follow = Follow.objects.filter(user__pk = user_pk).first()
  followers_list = follow.followers.all()
  if request.user in followers_list:
    follow.followers.remove(request.user)
    return redirect('my_page',user_pk)
  follow.followers.add(request.user)    
  return redirect('my_page',user_pk)


def category(request):
  category = Category.objects.all()
  context = {
    'categories':category
  }
  return render(request, 'category.html',context)


def article_list(request, category_pk):
  article = Article.objects.filter(category__pk = category_pk).all()
  context = {
    'articles':article
  }
  return render(request, 'article_list.html',context)


def writer(request):
  category = Category.objects.all()
  context = {
   'categories':category
   }
  if request.method == 'POST':
    title = request.POST['title']
    content = request.POST['content']
    category_pk = request.POST['category_pk']

    if title and content and category_pk:
      category = Category.objects.filter(pk = category_pk).first()    
      Article.objects.create(
        title = title,
        writer = request.user,
        content = content,
        category=category
      )
      return redirect('category')
  return render(request, 'writer.html',context)