from django.forms import ModelForm

from actors.models import Actor


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'
