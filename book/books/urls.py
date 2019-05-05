from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^reader/$', views.reader, name='reader'),
    url(r'^query/$', views.query, name='query'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^userinfo/$', views.userinfo, name='userinfo'),
    url(r'^modify/$', views.modify, name='modify'),
    url(r'^history/$', views.history, name='history'),
    url(r'^bookdetail/(\d+)/$', views.bookdetail, name='bookdetail'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^mail/$', views.mail, name='mail'),
    url(r'^active/(.*?)/$', views.active, name='active'),
    url(r'^ajax$', views.ajax, name='ajax'),
    url(r'^ajaxload/$', views.ajaxload, name='ajaxload'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'option/', views.option, name='option'),
]
