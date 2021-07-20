from django.core.management.base import BaseCommand, CommandError
from chessdotcom import *


class Command(BaseCommand):
    help = 'Lists all available archives from chess.com'

    def handle(self, *args, **options):
        archives = get_player_game_archives('seiftn').archives
        for arch in archives:
            self.stdout.write(self.style.SUCCESS(arch))
