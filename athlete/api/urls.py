# DJANGO
from django.urls import include, path

# DRF
from .views import TeamList, TeamDetail
from . import views

app_name = 'api'

urlpatterns = [
    path('team/<int:pk>/', views.TeamDetail().as_view(), name="detail_team"),
    path('teams/', views.TeamList().as_view(), name="list_teams"),
]
