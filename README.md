## Function-Based-View Tutorial

## 목차
- ### 가상환경 세팅     
- ### 회원가입,로그인 페이지 구현   
- ### 글 작성 페이지 구현    
- ### 댓글 구현   
- ### 댓글 좋아요 구현   
- ### 팔로우, 팔로잉 구현    
- ### 해시태그 구현    

## 가상환경 세팅

__1. venv를 실행시킨후 필요한 패키지를 설치한다__            
```bash
virtualenv venv
source venv/bin/activate
pip install django
```
<br>

__2. 프로젝트와 앱을 설치한다__    
```bash
django-admin startproject config .
django-admin startapp crudapp
```
<br>

__3. 설치한 앱을 settings.py의 INSTALLED_APPS에 넣어준다__   
<br> 

__4. 이제 프로젝트를 만들 최소한의 준비는 끝이 났다. ```python manage.py runserver```를 실행시켜 장고 페이지가 제대로 나오는지 확인해주자__
<br>

__(github에 commit할 계획이라면 .gitignore를 만들어 필수로 넣어주어야 할 파일들을 넣어주자)__     

<br>

## 회원가입,로그인 페이지 구현 
