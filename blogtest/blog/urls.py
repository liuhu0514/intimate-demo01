from django.conf.urls import url
from . import views
from .feed import ArticleFeed
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detailadd/(\d+)/$', views.detailadd, name='detailadd'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^cls/(\d+)/$', views.cls, name='cls'),
    url(r'^label/(\d+)/$', views.label, name='label'),
    url(r'^file/(\d+)/(\d+)/$', views.file, name='file'),
    url(r'^author/(\d+)/$', views.author, name='author'),
    url(r'^rss/$', ArticleFeed(), name='rss'),
]
