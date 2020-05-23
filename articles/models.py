from django.db import models

class Article(models.Model):
    headline = models.CharField(max_length=100, unique=True)
    summary = models.TextField(max_length=1000)
    image_url = models.URLField()
    author = models.CharField(max_length=150)
    slug = models.SlugField(max_length=40, unique=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline
