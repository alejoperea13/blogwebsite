from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required()
def articles(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'articles.html', context)
