from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'postings-home'),
    path('hello', views.hello, name = 'postings-hello'),
    path('about', views.about, name = 'postings-about'),
    path('profile', views.profile, name = 'postings-profileInfo'),
 
    
]