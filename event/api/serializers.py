# DJANGO 
from event.models import *

# DRF
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"