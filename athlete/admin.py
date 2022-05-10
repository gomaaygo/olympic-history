from django.contrib import admin

from .models import Team, Athlete


class TeamModelAdmin(admin.ModelAdmin):
    list_display = ['team', 'noc']

class AthleteModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'team']


admin.site.register(Team, TeamModelAdmin)
admin.site.register(Athlete, AthleteModelAdmin)
