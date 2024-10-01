from django.urls import path

from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, \
    ArticleView, ArticleFormCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    # path('<tags>/<article_id>/', views.article, name='article'),
    path('<int:id>/', ArticleView.as_view()),
    path('create/', ArticleFormCreateView.as_view(),
         name='article_create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]
