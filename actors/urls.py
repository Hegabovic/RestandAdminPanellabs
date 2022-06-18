from django.urls import path

from actors.views import *

app_name = 'actors'
urlpatterns = [
    path('list', list_all_actors, name='list'),
    path('add', add_actor, name='add'),
    path('edit/<int:id>', edit_actor, name='edit'),
    path('details/<int:id>', get_actor_details, name='details'),
    path('delete/<int:id>', delete_actor, name='delete'),
]
