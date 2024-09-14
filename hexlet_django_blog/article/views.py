from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View


class Articles(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


def article(request, tags, article_id):
    return render(
        request,
        'articles/base_articles.html',
        context={
            'tags': tags,
            'article_id': article_id
        }
    )

# Create your views here.
