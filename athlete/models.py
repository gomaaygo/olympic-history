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