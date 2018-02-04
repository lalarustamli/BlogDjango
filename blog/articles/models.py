from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 250)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # author
    # thumbnail

    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]
        