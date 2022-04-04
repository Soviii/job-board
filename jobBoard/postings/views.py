from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'postings/home.html', context)
    
def about(request):
    return render(request, 'postings/about.html', {'title': 'About'})

def hello(request):
    return HttpResponse('<h1>Hello there</h1>')

def profile(request):
    return HttpResponse('<h1>Profile Info</h1>')

# Create your views here.
