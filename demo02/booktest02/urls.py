from django.conf.urls import url
from . import views

app_name = 'booktest02'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tealist/$', views.list, name='tealist'),
    url(r'^class/(\d+)/$', views.cla, name='class1'),
    url(r'^student/(\d+)/$', views.student, name='student'),
]
