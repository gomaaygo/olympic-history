# DJANGO 
from athlete.models import *
from .serializers import TeamSerializer

# DRF
from rest_framework import generics


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