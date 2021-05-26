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

>__회원가입 페이지 구현__   
<br>

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

<br>

>__로그인 페이지 구현__    

__1. 입력받은 id,pwd 데이터를 post 요청으로 view에 전송한다__    

<br>

__2. login은 post,get 요청을 받기때문에 post인 경우와 get인 경우를 나눠서 로직을 작성한다. autheniticate를 사용하여 username과 password가 auth user에 존재하는지를 확인해준다. 존재한다면 ```auth.login```를 사용해 로그인해준다__ 

```python
#views.py

if request.method == 'POST':
    userid = request.POST['id']
    pwd = request.POST['password']

    user = authenticate(username = userid, password = pwd)
    if user is  None:
      context['error']['state'] = True
      context['error']['msg'] = '아이디와 비밀번호를 확인해주세요'

    auth.login(request, user)
    return redirect('home') # post요청일때의 반환값

return render(request, 'login.html',context) # get요청일때의 반환값

```
<br>

>__로그아웃 구현__   

__1. ```auth.logout(request)```를 사용해 현재 로그인되어 있는 user를 로그아웃 해준다__   
```python
def logout(request):
  auth.logout(request)
  return redirect('home')
``` 

<br>

>__글 작성 페이지 구현__     

__1. 카테고리와 카테고리 각각의 글을 볼 수 있는 페이지를 나누어 구현한다__   

![template](https://user-images.githubusercontent.com/64240637/119611858-30225580-be36-11eb-8763-ff92562403c4.png)

- category.html : 만들어 놓은 카테고리를 화면에 보여준다     
- writer.html : 카테고리를 직접 선택해 글을 작성할 수 있다   
- article_list.html : 카테고리를 누르면 카테고리에 해당하는 글의 목록을 화면에 보여준다     
- article_writer.html : 작성하기를 누르면 해당 카테고리에 글을 작성할 수 있다        
- article_detail.html : 글을 선택하면 글의 세부 내용을 볼 수 있다     

<br>

__2. 카테고리를 작성하기 위해 model을 작성한 후 admin에 직접 카테고리 내용을 추가해준다__      
Category와 Article 두개의 모델을 작성한다. Article은 글을 작성할때 쓰이는 모델이므로 작성자를 User와 1:n으로 묶어준다. 이때 user가 생성될때 함께 생성되는 profile 모델이 있다. 작성자를 user와 묶어줄 수 있지만 profile과 묶어줄 수도 있다. __이는 선택사항이므로 선택해서 묶어준다. 단, 통일성있게 묶어야 한다는 것을 잊지말자!__ 작성되는 세부글은 카테고리를 선택해야 하기 때문에 글의 카테고리도 category와 1:n으로 묶어주어야 한다. 여기서는 user로 묶는 것으로 통일시키겠다   

![category](https://user-images.githubusercontent.com/64240637/119616286-644c4500-be3b-11eb-8a45-8246e84190bf.png) 

```python
# models.py

class Category(models.Model):
    name = models.CharField(max_length=32)
    
class Article(Timestampable):
  category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, related_name='article')
  writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
  title = models.CharField(max_length=64)
  content = models.TextField()
  is_deleted = models.BooleanField(default=False)
```
하나의 category는 여러개의 article에서 접근할 수 있으며(1:n) 현재 로그인한 user가 여러개의 article을 작성할 수 있다(1:n)    

<br>

__3. category를 all()함수를 사용해 템플릿에 그려준 뒤 각각의 category중 하나를 누르면 pk와 함께 article_list view에 데이터를 보낸다. article_list는 해당 category의 pk를 받아 category에 쓰인 article을 filter함수를 사용하여 필터하여 모든 데이터를 가져온다.__    
이때 article_list 템플릿에서 카테고리에 관련된 글을 작성하기 위해서는 어떤 카테고리인지 알아야하기 때문에 view에서 현재 들어와 있는 카테고리의 pk를 함께 템플릿에 보내준다    
```python
# views.py

def article_list(request, category_pk):
  article = Article.objects.filter(category__pk = category_pk).all()
  category_pk = Category.objects.filter(pk = category_pk).first().pk # 템플릿에서 해당하는 카테고리 찾기 위해서
  # Article category__pk.pk로 하면 Article이 없는 카테고리를 들어갈때 에러 발생함
  context = {
    'articles':article,
    'category_pk':category_pk
  }
  return render(request, 'article_list.html',context)
```
article안에 있는 글작서 버튼을 누를때 카테고리가 선택되어져 있어야 하기 때문에 category의 pk 데이터를 함께 url에 보낸다     
```html
<a href="{% url 'blog:article_writer' category_pk %}">글작성하기</a>     
```
<br>

__4. article_writer에서 작성한 데이터를 받아 article을 Create해준다__     
```python
#views.py

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

```
<br>

__5. category.html에서도 글작성하기를 추가한다__    
이때는 글 작성할때 카테고리를 직접 선택해야 하기 때문에 category로부터 get요청이 들어올 때 all함수를 사용하여 category의 모든 데이터를 함께 보내준다. 데이터를 받은 템플릿은 form안에서 select-option을 사용하여 category를 선택할 수 있게 한다    

```html
<!--  writer.html -->

<form action="{% url 'blog:writer' %}"method="POST">
  {% csrf_token %}
  <select name="category_pk">
    {% for category in categories %}
    <option value="{{category.pk}}">{{category}}</option>  <!--각각의 카테고리 중 하나 선택시 해당 Category.pk 데이터가 보내진다-->
    {% endfor %}
  </select><br><br>
.....
</form>
```
writer.html에서 사용자가 작성한 제목, 글, 선택한 카테고리 데이터가 전송되어 writer view에서 새로운 article 필드가 생성된다. create로 생성되어지며 위의 코드와 같이 생성된다    
<br>

__6. 작성된 글의 세부사항을 보기 위해서 article_list에서 각각의 글들을 누르면 해당 글의 pk 데이터가 article_detail view로 전달된다__   
article_detail은 해당 pk에 맞는 글을 필터해 템플릿에 데이터를 보내준다    
 