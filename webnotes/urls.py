from django.urls import re_path
from .views import index, create, details, edit, delete


urlpatterns = [
    re_path(r'^(?P<user_id>[0-9]+)$', index),
    re_path(r'^index/(?P<user_id>[0-9]+)$', index),
    re_path(r'create', create),
    re_path(r'^details/(?P<webnote_id>[0-9]+)$', details),
    re_path(r'^edit/(?P<webnote_id>[0-9]+)$', edit),
    re_path(r'^delete/(?P<webnote_id>[0-9]+)$', delete)
    # path('details', details),
    # path('edit', edit),
    # path('delete', delete)
]
