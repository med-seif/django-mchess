from django.core.management.base import BaseCommand, CommandError
from django.core import management

class Command(BaseCommand):
    help = 'Generates all fixtures for all archives at once'

    def handle(self, *args, **options):
        management.call_command('loaddata', 'games_2020_04.json')
        management.call_command('loaddata', 'games_2021_03.json')
        management.call_command('loaddata', 'games_2021_04.json')
        management.call_command('loaddata', 'games_2021_05.json')
        management.call_command('loaddata', 'games_2021_06.json')
        management.call_command('loaddata', 'games_2021_07.json')
        self.stdout.write(self.style.SUCCESS('Data was loaded successfully in database'))
