from django.db import models
from django.db.models import CASCADE

from director.models import Director


class Movie(models.Model):
    movie_name = models.fields.CharField(verbose_name='movie name', max_length=25, unique=True)
    production_year = models.IntegerField(verbose_name='production year')
    actors = models.ManyToManyField('actors.actor')
    director = models.ForeignKey(Director, on_delete=CASCADE, related_name='movies')
    create_time = models.TimeField(verbose_name='Created at', auto_now=True)
    update_time = models.TimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return f'{self.movie_name}'

    def __unicode__(self):
        return u'%s' % self.director.director_name
