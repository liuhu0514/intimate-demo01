from django.conf.urls import url
from . import views
app_name = 'templatest'

urlpatterns = [
    url('^goods/$', views.goods, name='goods'),
    url('^user/$', views.user, name='user'),
    url('^login/$', views.login, name='login'),
]
