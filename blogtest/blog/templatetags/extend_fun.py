from django import template
from ..models import User, Classify, Label, Article
register = template.Library()


# 获取所有类
@register.simple_tag
def get_cls():
    cls = Classify.objects.all()
    return cls


# 获取所有标签
@register.simple_tag
def get_label():
    labels = Label.objects.all()
    return labels


# 获取最新三篇文章
@register.simple_tag
def get_file():
    files = Article.objects.order_by('-add_time')[:3]
    return files


# 获取时间归档
@register.simple_tag
def get_time():
    res = Article.objects.dates('add_time', 'month', 'DESC')[:3]
    return res
