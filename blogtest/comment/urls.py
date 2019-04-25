from django.conf.urls import url
from . import views

app_name = 'comment'

urlpatterns = [
    url(r'comment/(\d+)/', views.commit_comment, name='comment'),
]

