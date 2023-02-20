from django.core.management.base import BaseCommand, CommandError
from django.core import management


class Command(BaseCommand):
    help = 'Gets data for all months from chess.com API and export them to DB'

    def add_arguments(self, parser):
        parser.add_argument('--period', type=str, help='MM/YYYY, example 07/2021')

    def handle(self, *args, **options):
        if options['period']:
            management.call_command('loadarchive', options['period'])
            listperiod = options['period'].split('/')
            management.call_command('loaddata', 'games_' + listperiod[1] + '_' + listperiod[0] + '.json')
            self.stdout.write(self.style.SUCCESS(
                'Data for period [' + options['period'] + '] was pulled and loaded successfully in database'))
        else:
            management.call_command('generateallfixtures')
            management.call_command('loadalldata') 
            self.stdout.write(self.style.SUCCESS('All data was pulled and loaded successfully in database'))
