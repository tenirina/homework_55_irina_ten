from django.urls import path

from webapp.view.add_todo import add_view, detail_view
from webapp.view.base import index_view

urlpatterns = [
    path("", index_view),
    path("add_todo/", add_view),
    path("todo/", detail_view)
]
