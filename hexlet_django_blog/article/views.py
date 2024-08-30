from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(
        request,
        'articles/base_articles.html',
        context={'tags': 'article'}
    )
# Create your views here.
