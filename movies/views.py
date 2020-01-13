from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'movies/movies.html')

def movie(request):
    return render(request, 'movies/movie.html')

def search(request):
    return render(request, 'movies/search.html')