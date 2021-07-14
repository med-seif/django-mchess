from django.core.management.base import BaseCommand, CommandError
from client.models import Game
from django_seed import Seed
from random import randint


class Command(BaseCommand):
    help = 'Seeds games rows in database'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of rows to be inserted')

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        seeder.add_entity(Game, options['number'], {
            'id': lambda x: randint(1, 1000000)
        })

        games_count_before = Game.objects.all().count()

        try:
            inserted_pks = seeder.execute()
            c =  len(inserted_pks[Game])
            self.stdout.write(self.style.SUCCESS('Successfully inserted %s games' % c))
        except Exception as e:
            self.stdout.write(str(e))
            games_count_after = Game.objects.all().count()
            cdb = str(games_count_after - games_count_before)
            self.stdout.write(self.style.SUCCESS(cdb) + ' games were inserted before exception')


