from crudapp.models import Article,Tag
from django.shortcuts import redirect


def create_article_tag(request, article_pk):
  name = request.POST['tag']
  article = Article.objects.filter(pk = article_pk).first()
  tag = Tag.objects.filter(name = name).first()
  if tag:
    tag.articles.add(article)
    return redirect('blog:article_detail',article_pk)
  new_tag = Tag.objects.create(
    name = name
  )
  new_tag.articles.add(article)