from django.core.management.base import BaseCommand
from faker import Faker
from fire.models import (
    Locations, Incident, FireStation, 
    WeatherConditions, FireTruck, Firefighters, Boat
)

class Command(BaseCommand):
    help = 'Generates fake data for testing'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Example: Generate fake Fire Stations
        for _ in range(10):
            FireStation.objects.create(
                name=fake.company(),
                address=fake.street_address(),
                city=fake.city(),
                country=fake.country(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data!'))