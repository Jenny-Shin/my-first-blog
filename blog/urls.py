from django.conf.urls import url
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/ 을 식별
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
