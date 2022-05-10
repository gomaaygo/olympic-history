from django.contrib import admin

from .models import Team


class TeamModelAdmin(admin.ModelAdmin):
    list_display = ['team', 'noc']


admin.site.register(Team, TeamModelAdmin)
