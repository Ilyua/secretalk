
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_chat$', views.get_chat, name='get_chat'),
    url(r'^current_ids$', views.current_ids, name='current_ids'),
]
