from django.urls import path

from articles.views import ArticleView

app_name = 'articles'
urlpatterns = [
    path('', ArticleView.as_view(), name='index'),
]
