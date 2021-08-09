from django.core.management.base import BaseCommand, CommandError
from django.core import management
from chessdotcom import *
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Generates all fixtures for all archives at once'

    def handle(self, *args, **options):
        archives = get_player_game_archives('seiftn').archives
        pbar = tqdm(archives)
        for arch in pbar:
            arch_url_data = arch.split('/')
            arch_url_data.reverse()
            pbar.set_description("Writing from %s" % arch)
            management.call_command('loadarchive', arch_url_data[0] + '/' + arch_url_data[1])

        self.stdout.write(self.style.SUCCESS('Fixtures were created successfully'))
