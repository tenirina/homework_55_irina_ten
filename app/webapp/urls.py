from django.urls import path

from webapp.view.add_todo import add_view, detail_view, edit_view, delete_view, confirm_delete_view
from webapp.view.base import index_view

urlpatterns = [
    path("", index_view, name='index'),
    path("add_todo/", add_view, name='add_todo'),
    path("todo/<int:pk>/edit", edit_view, name='edit_todo'),
    path("todo/<int:pk>", detail_view, name='todo'),
    path("todo/<int:pk>/delete", delete_view, name='delete_todo'),
    path("todo/<int:pk>/confirm-delete", confirm_delete_view, name='confirm_delete')
]
