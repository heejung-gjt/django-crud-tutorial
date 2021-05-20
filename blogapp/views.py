from crudapp.models import Category,Article,Tag
from django.shortcuts import get_object_or_404, redirect, render


def category(request):
  category = Category.objects.all()
  context = {
    'categories':category
  }
  return render(request, 'category.html',context)


def article_list(request, category_pk):
  article = Article.objects.filter(category__pk = category_pk).all()
  category_pk = Category.objects.filter(pk = category_pk).first().pk
  # Article category__pk.pk로 하면 Article이 없는 카테고리를 들어갈때 에러 발생함
  context = {
    'articles':article,
    'category_pk':category_pk
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
      return redirect('blog:category')
  return render(request, 'writer.html',context)


def article_detail(request, article_pk):
  article = get_object_or_404(Article, pk = article_pk)
  tag = Tag.objects.filter(articles__pk = article_pk).all()

  context = {
    'article':article,
    'tags':tag
  }
  return render(request, 'article_detail.html',context)


def article_writer(request, category_pk):
  category = Category.objects.filter(pk = category_pk).first()
  if request.method == 'POST':
    title = request.POST['title']
    content = request.POST['content']
    Article.objects.create(
      title = title,
      content = content,
      category = category,
      writer = request.user
    )
    return redirect('blog:article_list',category_pk)
  context = {
    'category':category
  }
  return render(request, 'article_writer.html',context)
