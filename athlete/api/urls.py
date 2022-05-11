# DJANGO
from django.urls import include, path

# DRF
from .views import TeamList, TeamDetail
from . import views

app_name = 'api'

urlpatterns = [
    # Urls Team
    path('team/<int:pk>/', views.TeamDetail().as_view(), name="detail_team"),
    path('teams/', views.TeamList().as_view(), name="list_teams"),
    # Urls Athlete
    path('athletes/<int:pk>/', views.AthleteDetail().as_view(), name="detail_athlete"),
    path('athletes/', views.AthleteList().as_view(), name="list_athletes"), 
]
