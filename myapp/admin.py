from django.contrib import admin
from .models import FirstAuthor, FirstBook, Author, Book, Reader, User, Article, Comment, Like, Dislike


admin.site.register(FirstAuthor)
admin.site.register(FirstBook)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)