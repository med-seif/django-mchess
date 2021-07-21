from django.core.management.base import BaseCommand, CommandError
from django.core import management
from chessdotcom import *


class Command(BaseCommand):
    help = 'Generates all fixtures for all archives at once'

    def handle(self, *args, **options):
        archives = get_player_game_archives('seiftn').archives
        for arch in archives:
            arch_url_data = arch.split('/')
            arch_url_data.reverse()
            management.call_command('loadarchive', arch[0] + '/' + arch[1])

        self.stdout.write(self.style.SUCCESS('Fixtures were created successfully'))
