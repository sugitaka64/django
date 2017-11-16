from django.conf.urls import url
from . import views

app_name = 'word_of_mouth'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<word_of_mouth_id>[0-9]+)/$', views.detail, name='detail'),
]
