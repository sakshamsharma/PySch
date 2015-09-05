from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', views.getPapers, name='paperlist'),
    url(r'^author/1', views.auth1, name='a1'),
    url(r'^author/2', views.auth2, name='a2'),
    url(r'^author/3', views.auth3, name='a3'),
    url(r'^author/4', views.auth4, name='a4'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]
