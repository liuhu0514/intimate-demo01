from django import template
from ..models import Article

register = template.Library()


@register.simple_tag
def getfile():
    res = Article.objects.dates('pub_time', 'month', 'DESC')[:3]
    a = res[1].year
    return res
