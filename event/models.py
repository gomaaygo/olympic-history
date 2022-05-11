from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Game(models.Model):
    SEASON_CHOICES = (
        ("Summer", "Summer"),
        ("Winter", "Winter"),
    )
    year = models.IntegerField(verbose_name="Year", validators=[MinValueValidator(1896)], null=False, blank=False)
    season = models.CharField(verbose_name="Season", max_length=6, choices=SEASON_CHOICES, null=False, blank=False)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        return str(self.year) + str(self.season)


class City(models.Model):
    city = models.CharField(verbose_name="City", max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city


class Sport(models.Model):
    sport = models.CharField(verbose_name="Sport", max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = "Sport"
        verbose_name_plural = "Sports"

    def __str__(self):
        return self.sport


class Event(models.Model):
    event = models.CharField(verbose_name="Event", max_length=255, null=False, blank=False)
    sport = models.ForeignKey(Sport, on_delete=models.PROTECT, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.event
