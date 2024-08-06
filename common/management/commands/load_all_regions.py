import json
from django.core.management.base import BaseCommand
from core.settings.base import BASE_DIR
from common.models import Region, Country


class Command(BaseCommand):
    help = 'Load all regions'

    def handle(self, *args, **kwargs):
        try:
            with open(str(BASE_DIR) + '/data/regions.json') as f:
                regions = json.load(f)
                country = Country.objects.get(name="O'zbekiston", code='UZ')
                for region in regions:
                    Region.objects.get_or_create(name=region['name_uz'], country=country)
                self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(regions)} regions'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error {e}'))
