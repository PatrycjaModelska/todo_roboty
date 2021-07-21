from django.urls import path
from .views import view_list, new_list

urlpatterns = [
    path('<list_id>/', view_list, name='view list'),
    path('new', new_list, name='new list'),
]
