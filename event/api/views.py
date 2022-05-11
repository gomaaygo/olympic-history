# DJANGO 
from event.models import *
from .serializers import GameSerializer, CitySerializer, SportSerializer, EventSerializer

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


class CityList(generics.ListCreateAPIView):
    """
        This endpoint allows creating a city object and listing.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        This endpoint allows viewing, updating and deleting the city object.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SportList(generics.ListCreateAPIView):
    """
        This endpoint allows creating a sport object and listing.
    """
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class SportDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        This endpoint allows viewing, updating and deleting the sport object.
    """
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class EventList(generics.ListCreateAPIView):
    """
        This endpoint allows creating a event object and listing.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        This endpoint allows viewing, updating and deleting the event object.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer