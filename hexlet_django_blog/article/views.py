from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View


class Articles(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


"""def index(request):
    return render(
        request,
        'articles/base_articles.html',
        context={'tags': 'article'}
    )"""

# Create your views here.
