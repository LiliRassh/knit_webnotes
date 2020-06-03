from django.urls import path, re_path
from .views import index, create, details, edit, delete


urlpatterns = [
    path('', index),
    path('index', index),
    path('create', create),
    re_path(r'^details/(?P<yarn_id>[0-9]+)$', details),
    re_path(r'^edit/(?P<yarn_id>[0-9]+)$', edit),
    re_path(r'^delete/(?P<yarn_id>[0-9]+)$', delete)
    # path('details', details),
    # path('edit', edit),
    # path('delete', delete)
]
