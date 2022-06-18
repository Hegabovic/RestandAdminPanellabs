from django.shortcuts import render, redirect

from movies.forms import MovieForm
from movies.models import Movie


def list_all_movies(request):
    movies = Movie.objects.all()
    form = MovieForm
    return render(request, 'movies/list_movies.html', context={'movies': movies, 'form': form})


def get_movie_details(request, **kwargs):
    movie_id = kwargs['id']
    record = Movie.objects.filter(id=movie_id)[0]
    return render(request, 'movies/movie_details.html', context={'movie': record})


def edit_movie(request, **kwargs):
    movie_id = kwargs['id']
    movie = Movie.objects.filter(id=movie_id)[0]

    if request.method == 'GET':
        edit_form = MovieForm(instance=movie)
        return render(request, 'movies/edit_movie.html', context={'form': edit_form, 'movie': movie})
    elif request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()

        return redirect('movies:list')


def add_movie(request):
    if request.method == 'GET':
        add_form = MovieForm()
        return render(request, 'movies/add_movie.html', context={'form': add_form})
    elif request.method == 'POST':
        form = MovieForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:list')


def delete_movie(request, **kwargs):
    movie_id = kwargs['id']
    Movie.objects.filter(id=movie_id).delete()
    return redirect('movies:list')
