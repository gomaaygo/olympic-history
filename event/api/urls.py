# DJANGO
from django.urls import include, path

# DRF
from .views import GameDetail, GameList
from . import views

app_name = 'api'

urlpatterns = [
    # Urls Game
    path('game/<int:pk>/', views.GameDetail().as_view(), name="detail_game"),
    path('games/', views.GameList().as_view(), name="list_games"),
]
