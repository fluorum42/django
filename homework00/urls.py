"""homework00 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from myapp.views import main, articles, articles_archive, users, article, regex

urlpatterns = [
    path('', main),
    path('articles/', articles),
    path('articles_archive/', articles_archive, name='arctiles_archive'),
    path('users', users, name='users'),
    path('users/<int:user_number>/', users, name='users'),
    path('article/<int:article_id>/', article, name='article'),
    path('article/<int:article_id>/<slug:slug_text>', article, name='article'),
    path('article/<int:article_id>/archive/', article, name='article'),
    re_path(r'^(?P<text>[0-9a-fA-F]{4}-[0-9a-fA-F]{6}$)', regex),
    re_path(r'^(?P<text>(039|050|063|066|067|068|073|089|091|092|093|094|095|096|097|098|099)\d{7}$)', regex),
]
