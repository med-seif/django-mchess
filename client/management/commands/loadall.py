from django.core.management.base import BaseCommand, CommandError
from django.core import management

class Command(BaseCommand):
    help = 'Generates all fixtures for all archives at once'

    def handle(self, *args, **options):
        management.call_command('loadallarchives')
        management.call_command('loadalldata')
        self.stdout.write(self.style.SUCCESS('All data was pulled and loaded successfully in database'))
