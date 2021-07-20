from django.core.management.base import BaseCommand, CommandError
from django.core import management

class Command(BaseCommand):
    help = 'Generates all fixtures for all archives at once'

    def handle(self, *args, **options):
        management.call_command('loadarchive', '04/2020')
        management.call_command('loadarchive', '03/2021')
        management.call_command('loadarchive', '04/2021')
        management.call_command('loadarchive', '05/2021')
        management.call_command('loadarchive', '06/2021')
        management.call_command('loadarchive', '07/2021')
        self.stdout.write(self.style.SUCCESS('Fixtures were created successfully'))
