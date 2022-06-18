from django.contrib import admin

from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ('production_year',)
    list_display = ['movie_name', 'director']
