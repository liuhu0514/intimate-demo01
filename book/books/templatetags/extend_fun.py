from django import template
from ..models import HotPic
from manager.models import Article

register = template.Library()


@register.simple_tag
def get_hot():
    hots = HotPic.objects.all().order_by('index')
    return hots


@register.simple_tag
def get_art():
    arts = Article.objects.all()
    return arts
