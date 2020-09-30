from django.http import HttpResponse
from django.shortcuts import render


# /products -> index
def index(request):
    context = {}
    return render(request, 'index.html', context)
