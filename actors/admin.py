from django.contrib import admin

from actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ('actor_name',)
    list_filter = ('gender',)
    list_display = ['actor_name', 'age', 'gender', 'movies_count']
    readonly_fields = ['movies_count']

    def movies_count(self, obj):
        return obj.movie_set.count()

    movies_count.short_description = 'movie count'
