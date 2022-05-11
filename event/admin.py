from django.contrib import admin

from .models import Game, City, Sport, Event, AthleteEvent

# Register your models here.

class GameModelAdmin(admin.ModelAdmin):
    list_display = ['year', 'season']

class CityModelAdmin(admin.ModelAdmin):
    list_display = ['city']

class SportModelAdmin(admin.ModelAdmin):
    list_display = ['sport']

class EventModelAdmin(admin.ModelAdmin):
    list_display = ['event', 'sport', 'city', 'game']

class AthleteEventModelAdmin(admin.ModelAdmin):
    list_display = ['athlete', 'event', 'weight', 'height', 'age', 'medal']


admin.site.register(Game, GameModelAdmin)
admin.site.register(City, CityModelAdmin)
admin.site.register(Sport, SportModelAdmin)
admin.site.register(Event, EventModelAdmin)
admin.site.register(AthleteEvent, AthleteEventModelAdmin)
