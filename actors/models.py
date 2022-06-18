from django.db import models

GENDER_LIST = [('male', 'male'), ('female', 'female')]


class Actor(models.Model):
    actor_name = models.fields.CharField(verbose_name='Name', max_length=25, unique=True)
    gender = models.CharField(verbose_name='Gender', choices=GENDER_LIST, max_length=6, default='male')
    age = models.IntegerField(default=0)
    create_time = models.TimeField(verbose_name='Created at', auto_now=True)
    update_time = models.TimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return f'{self.actor_name}'
