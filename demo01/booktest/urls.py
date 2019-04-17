from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='booklist'),
    url(r'^detail/(\d+)/$', views.detail, name='bookdetail'),
    url(r'^herodetail/(\d+)/$', views.herodetail, name='herodetail'),
]
