from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def repertoer(request):
    return render(request, 'pages/repertoer.html')

