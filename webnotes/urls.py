from django.urls import re_path, path
from .views import index, create, details, edit, delete, public


urlpatterns = [
    re_path(r'^(?P<user_id>[0-9]+)$', index),
    re_path(r'^index/(?P<user_id>[0-9]+)$', index),
    path('create', create),
    re_path(r'^details/(?P<webnote_id>[0-9]+)$', details),
    re_path(r'^edit/(?P<webnote_id>[0-9]+)$', edit),
    re_path(r'^delete/(?P<webnote_id>[0-9]+)$', delete),
    path('public', public),
]
