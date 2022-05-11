# DJANGO 
from athlete.models import *
from .serializers import TeamSerializer, AthleteSerializer

# DRF
from rest_framework import generics
from rest_framework import filters


class TeamList(generics.ListCreateAPIView):
    """
        This endpoint allows creating a team object and listing.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        This endpoint allows viewing, updating and deleting the team object.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class AthleteList(generics.ListCreateAPIView):
    """
        This endpoint allows creating a athlete object and listing.
    """
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['sex', 'team__team']


class AthleteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        This endpoint allows viewing, updating and deleting the athlete object.
    """
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer