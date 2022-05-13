import csv
import os

# Import models
from athlete.models import Team, Athlete
from event.models import Game, City, Sport, Event, AthleteEvent


def none_or_not(info):
    """
        Function that checks if the field has valid information, otherwise none is returned.
    """
    if info == "NA":
        return None
    else:
        return info

def reset_db():
    """
        This function cleans the database.
    """
    Team.objects.all().delete()
    Game.objects.all().delete()
    City.objects.all().delete()
    Sport.objects.all().delete()
    Event.objects.all().delete()
    AthleteEvent.objects.all().delete()
    Athlete.objects.all().delete()

def run():
    # Open csv
    file = open('scripts/athlete_events.csv')
    data = csv.reader(file)

    # Clean database 
    reset_db()

    count = 1
    for row in data:
        if count == 1:
            pass
        else:
            # Create objects in database
            t, created = Team.objects.get_or_create(team=row[6], noc=row[7])

            a, created = Athlete.objects.get_or_create(name=row[1], sex=row[2], team=t)

            g, created = Game.objects.get_or_create(year=row[9], season=row[10])

            c, created = City.objects.get_or_create(city=row[11])

            s, created = Sport.objects.get_or_create(sport=row[12])

            e, created = Event.objects.get_or_create(event=row[13], sport=s, city=c, game=g)

            a_e, created = AthleteEvent.objects.get_or_create(athlete=a, event=e, weight=none_or_not(row[5]), height=none_or_not(row[4]), age=none_or_not(row[3]), medal=row[14])     
        
        count = count + 1

    print("Data added successfully!")