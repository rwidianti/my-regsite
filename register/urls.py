from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^regdata/new/$', views.regdata_new, name='regdata_new'),
    url(r'^regdata/(?P<pk>\d+)/$', views.regdata_detail, name='regdata_detail'),
    url(r'^regdata/(?P<pk>\d+)/edit/$', views.regdata_edit, name='regdata_edit'),
]
