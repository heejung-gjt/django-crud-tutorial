## Function-Based-View Tutorial

<br>

## 목차
- #### 가상환경 세팅     
- #### 회원가입,로그인,로그아웃 페이지 구현   
- #### 글 작성 페이지 구현    
- #### 댓글 구현   
- #### 댓글 좋아요 구현   
- #### 팔로우, 팔로잉 구현    
- #### 해시태그 구현    

<br>

## 가상환경 세팅

1. venv를 만들어 실행시킨 후 필요한 패키지를 설치한다               
```bash
virtualenv venv
source venv/bin/activate
pip install django
```
<br>

2. 프로젝트와 앱을 설치한다       
```bash
django-admin startproject config .
django-admin startapp crudapp
```
<br>

3. 설치한 앱을 settings.py의 INSTALLED_APPS에 넣어준다      
<br> 

4. 이제 프로젝트를 만들 최소한의 준비는 끝이 났다. ```python manage.py runserver```를 실행시켜 장고 페이지가 제대로 나오는지 확인해주자   
<br>

__(github에 commit할 계획이라면 .gitignore를 만들어 필수로 넣어주어야 할 파일들을 넣어주자)__     

<br>

## 회원가입,로그인,로그아웃 페이지 구현 

__1. django.contrib.auth를 이용한 회원가입 구현__        
회원가입시 유저의 프로필도 함께 만들어주었다. models.py에서 user와 profile를 1:1로 묶어준다. user가 생성될때 해당 user와 1:1 매핑되는 profile도 생성된다. 자세한 코드는 파일에서 확인해보자

```python
# models.py
from django.contrib.auth.models import User

class Profile(models.Model):
user = models.OneToOneField(User, on_delete=CASCADE, related_name='profile')
```
<br>

__2. 회원가입 링크를 만들어 회원가입 페이지로 이동할 수 있게 해준다__   
```html
<a href="{% url 'register' %}">회원가입하기</a>
```
<br>

__3. register로 매핑되는 url를 찾은 후 해당되는 view로 요청을 보낸다__    
```python
#urls.py

path('register/',views.register, name='register')
```
<br>

__4. view에서 POST로 받은 데이터를 가공해준다. 여기선 아이디존재여부, 비밀번호 체크, 닉네임존재여부 등을 조건으로 걸어주었다__     조건 성립이 된 경우 create_user로 user를 생성해주고 동시에 profile를 생성해준다. __이때 profile의 user는 auth user와 1:1로 연결되어 있기 때문에 auth user의 인스턴스가 와야함을 주의하자.__ 이후 auth.login기능을 이용해 현재 생성된 user로 로그인 해준다

```python
# views.py
# 자세한 내용은 코드 참조 

user = User.objects.create_user(
    username = userid,
    password = password
  )
Profile.objects.create(
    user = user,
    nickname = nickname,
    intro = intro
  )
auth.login(request, user)
```
<br>

__5. home 템플릿에서 로그인 된 경우와 그렇지 않은 경우에 보여지는 화면을 제어하기 위해 ```is_authenticated```을 이용한 장고 템플릿을 사용하였다__

```python
{% if user.is_authenticated %}
{{user.profile.nickname}}님 환영합니다 !
```