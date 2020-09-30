from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def userprofile(request):
    context = {}
    return render(request, 'userprofile.html', context)
