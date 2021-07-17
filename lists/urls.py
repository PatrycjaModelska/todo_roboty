from django.urls import path
from .views import home_page, view_list, new_list, add_item

urlpatterns = [
    path('', home_page, name='home'),
    path('lists/<list_id>/', view_list, name='view list'),
    path('lists/<list_id>/add_item', add_item, name='add item'),
    path('lists/new', new_list, name='new list'),
]
