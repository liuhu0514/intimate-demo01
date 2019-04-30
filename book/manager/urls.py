from django.conf.urls import url
from . import views
app_name = 'manager'

urlpatterns = [
    url('^manager_login/$', views.manager_login, name='manager_login'),
    url('^$', views.index, name='index'),
    url('^book_manage/$', views.book_manage, name='book_manage'),
    url(r'^addbook/$', views.addbook, name='addbook'),
    url(r'^deletebook/$', views.deletebook, name='deletebook'),
    url(r'^bookdetail/(\d+)/$', views.bookdetail, name='bookdetail'),
    url(r'^book_modify/(\d+)/$', views.book_modify, name='book_modify'),
    url(r'^user_manage/$', views.user_manage, name='user_manage'),
    url(r'^userdetail/(\d+)/$', views.userdetail, name='userdetail'),
    url(r'^deleteuser/(\d+)/$', views.deleteuser, name='deleteuser'),
    url(r'^user_modify/(\d+)/$', views.user_modify, name='user_modify'),
    url(r'^hotinfo/(\d+)/$', views.hotinfo, name='hotinfo'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^hot_delete/(\d+)/$', views.hot_delete, name='hot_delete'),
    url(r'^einfo/(\d+)/$', views.einfo, name='einfo'),
    url(r'^edelete/(\d+)/$', views.edelete, name='edelete'),
]
