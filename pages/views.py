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

    queryset_list = Movie.objects.order_by('title')

    # Search movie by title
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains=title)

    # Filter movies by genre 
    if 'genre' in request.GET:
        genre = request.GET['genre']
        if genre != 'All':
            queryset_list = queryset_list.filter(genre__icontains=genre)

    cinemas = Cinema.objects.all()
    genres = ['All', 'Action', 'Comedy', 'Drama', 'Sci-Fi', 'Thriller', 'Crime']

    context = {
        'cinemas': cinemas,
        'genres': genres,
        'movies': queryset_list
    }

    return render(request, 'pages/repertoer.html', context)

