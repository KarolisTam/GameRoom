# Generated by Django 4.2.2 on 2023-06-22 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0004_alter_player_options_player_played_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_at', models.DateTimeField(auto_now_add=True, verbose_name='Played_at')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_matches', to=settings.AUTH_USER_MODEL, verbose_name='Player 1')),
                ('player2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='joined_matches', to=settings.AUTH_USER_MODEL, verbose_name='Player 2')),
            ],
            options={
                'verbose_name': 'match',
                'verbose_name_plural': 'matchs',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.match', verbose_name='match'),
        ),
    ]