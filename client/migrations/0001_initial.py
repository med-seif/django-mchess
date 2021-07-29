# Generated by Django 3.2.5 on 2021-07-29 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('game_date', models.DateField(null=True)),
                ('game_time', models.TimeField(null=True)),
                ('game_end_date', models.DateField(null=True)),
                ('game_end_time', models.TimeField(null=True)),
                ('time_class', models.CharField(max_length=10)),
                ('opponent_rating', models.PositiveIntegerField()),
                ('opponent_username', models.CharField(max_length=50)),
                ('opponent_country', models.CharField(max_length=2, null=True)),
                ('my_rating', models.PositiveIntegerField()),
                ('my_color', models.CharField(max_length=1, null=True)),
                ('result', models.CharField(max_length=20, null=True)),
                ('result_detail', models.CharField(max_length=20, null=True)),
                ('pgn', models.TextField()),
                ('eco', models.CharField(max_length=10, null=True)),
                ('eco_url', models.CharField(max_length=300, null=True)),
                ('termination', models.CharField(max_length=100, null=True)),
                ('moves_number', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'game',
            },
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('clk', models.TimeField()),
                ('piece', models.CharField(max_length=2, null=True)),
                ('san', models.CharField(max_length=15, null=True)),
                ('color', models.CharField(max_length=1, null=True)),
                ('is_take', models.IntegerField(null=True)),
                ('is_check', models.IntegerField(null=True)),
                ('is_checkmate', models.IntegerField(null=True)),
                ('order', models.IntegerField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.game')),
            ],
            options={
                'db_table': 'move',
            },
        ),
    ]
