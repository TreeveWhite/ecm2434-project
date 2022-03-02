"""
The urls.py file declares the urls and the views
that they are linked to.
"""
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('about', views.about, name='about'),
    path('game', views.game, name='game'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('locations', views.locations, name='locations'),
    path('claim', views.claim, name='claim')
]
