
# from crudapp.models import Article,Tag
from django.shortcuts import redirect
from .service import create_article_tag 

def tag(request, article_pk):
  create_article_tag(request, article_pk) # service.py에서 tag 테이블 생성해준다
  
  return redirect('blog:article_detail',article_pk)