from django.db import models

class FirstAuthor(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class FirstBook(models.Model):
    title = models.CharField(max_length=120)
    author = models.OneToOneField(FirstAuthor, on_delete=models.CASCADE, related_name='auth')

    def __str__(self):
        return self.title
    

class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=240)
    author = models.ManyToManyField(Author, related_name='books')
    AV = 'AVAILABLE'
    UNAV = 'UNAVAILABLE'
    STATUS_CHOICES = [
        (AV, 'Available'),
        (UNAV, 'Unavailable'),
    ]

    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default=AV,
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Reader(models.Model):
    name = models.CharField(max_length=120)
    book = models.ManyToManyField(Book, related_name='reader')

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=120)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


class Article(models.Model):
    headline = models.CharField(max_length=100)
    text = models.TextField(max_length=10000, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline


class Comment(models.Model):
    text = models.TextField(max_length=10000, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,)
    comment = models.ForeignKey('myapp.Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text} by {self.user.username}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,)

    def __str__(self):
        return f"by {self.user.username} to {self.article.headline}"
  

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,)

    def __str__(self):
        return f"by {self.user.username} to {self.article.headline}"
