from django.conf.urls import url, include
from .views import get_todo_list, add_item, edit_an_item, toggle


urlpatterns = [
    url(r"^$", get_todo_list, name="todo_list"),
    url(r"^add_item$", add_item, name="item_form"),
    url(r'^edit/(?P<id>\d+)$', edit_an_item),
    url(r'^toggle/(?P<id>\d+)$', toggle),
]
