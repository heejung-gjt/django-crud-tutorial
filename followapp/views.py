from crudapp.models import Follow
from django.shortcuts import redirect


def follow(request, user_pk):
  follow = Follow.objects.filter(user__pk = user_pk).first()
  followers_list = follow.followers.all()
  if request.user in followers_list:
    follow.followers.remove(request.user)
    return redirect('user:my_page',user_pk)
  follow.followers.add(request.user)    
  return redirect('user:my_page',user_pk)
