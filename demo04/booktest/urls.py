from django.conf.urls import url
from . import views

app_name = 'booktest'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='booklist'),
    url(r'^detail/(\d+)/$', views.detail, name='bookdetail'),
    url(r'^herodetail/(\d+)/$', views.herodetail, name='herodetail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^delete/(\d+)/$', views.delete, name='delete'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'^addherohandle/(\d+)/$', views.addherohandle, name='addherohandle'),
    url(r'^addhandle/$', views.addhandle, name='addhandle'),
    url(r'^edit/(\d+)/$', views.edit, name='edit'),
    url(r'^edithandle/(\d+)/$', views.edithandle, name='edithandle'),
    url(r'^edithero/(\d+)/$', views.edithero, name='edithero'),
    url(r'^editherohandle/(\d+)/$', views.editherohandle, name='editherohandle'),
    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),
    url(r'^area/$', views.area, name='area'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
