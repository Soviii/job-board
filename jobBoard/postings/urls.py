from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'postings-home'),
    path('about/', views.about, name = 'postings-about'),
]