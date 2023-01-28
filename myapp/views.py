from django.http import HttpResponse
from django.shortcuts import render


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    return render(request, 'index.html')


def articles(request):
    return render(request, 'articles.html')


def articles_archive(request):
    return render(request, 'articles_archive.html')


def users(request):
    return render(request, 'users.html')


def article(request, article_id, slug_text=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "{}".format(
            slug_text) if slug_text else "This article will be written soon."))


def article_id(request, article_id):
    return render(request, 'article_id.html', {
        "article_id": article_id,
    })


def article_slug(request, article_id, slug_text):
    return render(request,'article_slug.html', {
        "article_id": article_id,
        "slug_text": slug_text,
    })


def regex(request, text):
    return HttpResponse(f"It's regexp with text: {text}")
