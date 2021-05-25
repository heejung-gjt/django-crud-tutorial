from crudapp.models import User,Profile,Follow
from django.shortcuts import redirect, render



def vaild_regitser_infor(request,context):
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
    return user, context
  return render(request,'register.html',context)


def check_user_follow(request,user_pk):
  owner = User.objects.filter(pk = user_pk).first()
  follow = Follow.objects.filter(user__pk = user_pk).first()
  if request.user in follow.followers.all():
    is_followed = True
  return is_followed, owner, follow