from django.urls import path
from movies.views import *

app_name = 'movies'
urlpatterns = [
    path('list', list_all_movies, name='list'),
    path('add', add_movie, name='add'),
    path('edit/<int:id>', edit_movie, name='edit'),
    path('details/<int:id>', get_movie_details, name='details'),
    path('delete/<int:id>', delete_movie, name='delete')
]
