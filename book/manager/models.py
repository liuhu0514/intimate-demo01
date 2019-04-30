from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Manager(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = HTMLField()

    def __str__(self):
        return self.title

