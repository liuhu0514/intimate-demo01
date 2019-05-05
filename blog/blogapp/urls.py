from django.conf.urls import url
from . import views
app_name = 'blogapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^detailadd/(\d+)/$', views.detailadd, name='detailadd'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^blogs/(\d+)/$', views.blogs, name='blogs'),
    url(r'^bloges/(\d+)/$', views.bloges, name='bloges'),
    url(r'^file/(\d+)/(\d+)/$', views.file, name='file'),
]
