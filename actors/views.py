from django.shortcuts import render, redirect

from actors.forms import ActorForm
from actors.models import Actor


def list_all_actors(request):
    actors = Actor.objects.all()
    form = ActorForm()
    return render(request, 'actors/list_actors.html', context={'actors': actors, 'form': form})


def get_actor_details(request, **kwargs):
    actor_id = kwargs['id']
    record = Actor.objects.filter(id=actor_id)[0]
    return render(request, 'actors/actor_details.html', context={'actor': record})


def edit_actor(request, **kwargs):
    actor_id = kwargs['id']
    actor = Actor.objects.filter(id=actor_id)[0]

    if request.method == 'GET':
        edit_form = ActorForm(instance=actor)
        return render(request, 'actors/edit_actor.html', context={'form': edit_form, 'actor': actor})
    elif request.method == 'POST':
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()

        return redirect('actors:list')


def add_actor(request):
    if request.method == 'GET':
        add_form = ActorForm()
        return render(request, 'actors/add_actor.html', context={'form': add_form})
    elif request.method == 'POST':
        add_form = ActorForm(data=request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('actors:list')


def delete_actor(request, **kwargs):
    actor_id = kwargs['id']
    Actor.objects.filter(id=actor_id).delete()
    return redirect('actors:list')
