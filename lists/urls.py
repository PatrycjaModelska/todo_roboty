from django.urls import path
from .views import view_list, new_list, add_item

urlpatterns = [
    path('<list_id>/', view_list, name='view list'),
    path('<list_id>/add_item', add_item, name='add item'),
    path('new', new_list, name='new list'),
]
