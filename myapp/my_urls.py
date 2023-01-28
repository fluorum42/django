from django.urls import path
from .views import article_id, article_slug

urlpatterns = [
    path('<int:article_id>', article_id, name='article_id'),
    path('<int:article_id>/<slug:slug_text>', article_slug, name='article_slug'),
    path('<int:article_id>/archive/', article_id, name='article'),
]