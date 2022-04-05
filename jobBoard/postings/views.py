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



# Create your views here.
