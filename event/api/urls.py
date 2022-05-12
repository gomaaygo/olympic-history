# DJANGO
from django.urls import include, path

# DRF
# from .views import GameDetail, GameList
from . import views

app_name = 'api'

urlpatterns = [
    # Urls Game
    path('game/<int:pk>/', views.GameDetail().as_view(), name="detail_game"),
    path('games/', views.GameList().as_view(), name="list_games"),
    # Urls City
    path('city/<int:pk>/', views.CityDetail().as_view(), name="detail_city"),
    path('cities/', views.CityList().as_view(), name="list_cities"),
    # Urls Sport
    path('sport/<int:pk>/', views.SportDetail().as_view(), name="detail_sport"),
    path('sports/', views.SportList().as_view(), name="list_sports"),
    # Urls Event
    path('event/<int:pk>/', views.EventDetail().as_view(), name="detail_event"),
    path('events/', views.EventList().as_view(), name="list_event"),
    # Urls AthleteEvent
    path('athlete/event/<int:pk>/', views.AthleteEventDetail().as_view(), name="detail_athlete_event"),
    path('athlete/events/', views.AthleteEventList().as_view(), name="list_athlete_event"),               
]
