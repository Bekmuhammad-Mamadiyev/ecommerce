import os
import json
from django.core.management.base import BaseCommand
from core.settings.base import BASE_DIR
from common.models import Country


class Command(BaseCommand):
    help = 'Load all countries'

    def handle(self, *args, **kwargs):
        try:
            file_path = os.path.join(BASE_DIR, 'data', 'countries.json')
            if not os.path.exists(file_path):
                self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
                return

            with open(file_path, 'r') as f:
                countries = json.load(f)
                for country in countries:
                    Country.objects.get_or_create(name=country['name_uz'], code=country['code'])
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(countries)} countries'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))

# class Command(BaseCommand):
#     help = 'Load all countries'
#
#     def handle(self, *args, **kwargs):
#         try:
#             with open(str(BASE_DIR) + '/data/countries.json') as f:
#                 countries = json.load(f)
#                 for country in countries:
#                     Country.objects.get_or_create(name=country['name_uz'], code=country['code'])
#             self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(countries)} countries')
#         except Exception as e:
#             self.stdout.write(self.style.ERROR(f'Error {e}'))
