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
