from django.contrib import admin

from director.models import Director
from movies.models import Movie


class MovieInline(admin.StackedInline):
    model = Movie


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    search_fields = ('movies__movie_name',)
    list_display = ('director_name', 'age',)


inlines = [MovieInline]
