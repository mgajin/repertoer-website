from django.shortcuts import render
from django.http import HttpResponse

from movies.models import Movie
from cinemas.models import Cinema 

def index(request):

    latest_movies = Movie.objects.order_by('-released')[:5]
    top_rated = Movie.objects.order_by('-rating')[:6]


    context = {
        'latest_movies': latest_movies,
        'top_rated': top_rated
    }

    return render(request, 'pages/index.html', context)

def repertoer(request):

    cinemas = Cinema.objects.all()
    genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Thriller', 'Crime']

    context = {
        'cinemas': cinemas,
        'genres': genres
    }

    return render(request, 'pages/repertoer.html', context)

