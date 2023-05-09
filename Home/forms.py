import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from Home import models


class Command(BaseCommand):
    help = 'Load data from EV Station file'

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / 'pontos.csv'
        keys = ('Station Name', 'New Georeferenced Column')  # the CSV columns we will gather data from.
        
        records = []
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append({k: row[k] for k in keys})

        # extract the latitude and longitude from the Point object
        for record in records:
            longitude, latitude = record['New Georeferenced Column'].split("(")[-1].split(")")[0].split()
            record['longitude'] = float(longitude)
            record['latitude'] = float(latitude)

            # add the data to the database
            models.objects.get_or_create(
                nome_ponto=record['Station Name'],
                latitude=record['latitude'],
                longitude=record['longitude']
            )