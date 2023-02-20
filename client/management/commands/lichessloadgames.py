from pprint import pprint
from django.core.management.base import BaseCommand, CommandError
import berserk


class Command(BaseCommand):
    help = 'Creates fixtures for lichess games'

    def handle(self, *args, **options):
        client = berserk.Client()
        games = client.games.export_by_player('msbr_tn',as_pgn=True)
        for g in games:
            pprint(g);
            