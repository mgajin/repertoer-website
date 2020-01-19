from django.shortcuts import render

from .models import Movie

def index(request):

    # movies = Movie.objects.all()
    movies = Movie.objects.order_by('title')

# Search movie by title
    if 'movie' in request.GET:
        movie = request.GET['movie']
        if movie:
            movies = movies.filter(title__icontains=movie)

    context = {
        'movies': movies
    }

    return render(request, 'movies/movies.html', context)

def movie(request, movie_id):
    return render(request, 'movies/movie.html')
