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

    genres = ['All', 'Action', 'Comedy', 'Drama', 'Sci-Fi', 'Thriller', 'Crime', 'Adventure']
    cinemas = Cinema.objects.all()

    # Get selected cinema 
    if 'cinema' in request.GET:
        cinema = Cinema.objects.get(name=request.GET['cinema'])
    else:
        cinema = Cinema.objects.get(id=1)
    
    # Get moies in selected cinema
    movies = Movie.objects.filter(cinema=cinema.id).order_by('title')

    # Search movie by title
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            movies = movies.filter(title__icontains=title)

    # Filter movies by genre 
    if 'genre' in request.GET:
        genre = request.GET['genre']
        if genre != 'All':
            movies = movies.filter(genre__icontains=genre)

    context = {
        'cinema': cinema,
        'cinemas': cinemas,
        'genres': genres,
        'movies': movies,
        'values': request.GET
    }

    return render(request, 'pages/repertoer.html', context)

