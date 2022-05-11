# DJANGO 
from event.models import *
from .serializers import GameSerializer

# DRF
from rest_framework import generics
from rest_framework import filters


class GameList(generics.ListCreateAPIView):
    """
        This endpoint allows creating a game object and listing.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        This endpoint allows viewing, updating and deleting the game object.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer