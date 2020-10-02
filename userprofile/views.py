from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from articles.models import Post
from django.contrib.auth.models import User

@login_required()
def userprofile(request):
    current_user = request.user
    posts = Post.objects.all()
    context ={
        'my_posts' : current_user.post_set.all()
    }

    return render(request, 'userprofile.html', context)





