from django.db import models


GENDER_LIST = [('male', 'male'), ('female', 'female')]


class Director(models.Model):
    director_name = models.CharField(verbose_name='director name', max_length=30, unique=True)
    gender = models.CharField(verbose_name='gender', max_length=6, choices=GENDER_LIST, default='male')
    age = models.IntegerField(default=0)
    create_time = models.TimeField(verbose_name='Created at', auto_now=True)
    update_time = models.TimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return f'{self.director_name}'
