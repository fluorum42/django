from django.http import HttpResponse


def main(request):
    return HttpResponse("Hey! It's your main view!!")


def articles(request):
    return HttpResponse('There will be a list with articles.')


def articles_archive(request):
    return HttpResponse('This is articles archive.')


def users(request):
    return HttpResponse("There will be a list with users.")


def article(request, article_id, slug_text=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "{}".format(
            slug_text) if slug_text else "This article will be written soon."))


def regex(request, text):
    return HttpResponse(f"It's regexp with text: {text}")
