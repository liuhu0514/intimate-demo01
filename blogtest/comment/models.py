from django.db import models
from blog.models import Article

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

