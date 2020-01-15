from django.shortcuts import render

from .models import Movie

def index(request):

    # movies = Movie.objects.all()
    movies = Movie.objects.order_by('title')

    context = {
        'movies': movies
    }

    return render(request, 'movies/movies.html', context)

def movie(request, movie_id):
    return render(request, 'movies/movie.html')
