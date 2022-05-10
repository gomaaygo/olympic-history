from django.db import models

# Create your models here.

class Team(models.Model):
    team = models.CharField(verbose_name="Team", max_length=255, null=False, blank=False)
    noc = models.CharField(verbose_name="NOC", max_length=3, null=False, blank=False)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.team


class Athlete(models.Model):
    SEX_CHOICES = (
        ("M", "M"),
        ("F", "F"),
    )
    name = models.CharField(verbose_name="Name", max_length=200, null=False, blank=False)
    sex = models.CharField(verbose_name="Sex", max_length=1, choices=SEX_CHOICES, null=False, blank=False)
    team = models.ForeignKey(Team, verbose_name="Team", on_delete=models.PROTECT) 

    class Meta:
        verbose_name = "Athlete"
        verbose_name_plural = "Athletes"

    def __str__(self):
        return self.name