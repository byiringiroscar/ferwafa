# Generated by Django 4.0.2 on 2022-03-10 07:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_club_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club_managers',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Club Manager'},
        ),
        migrations.AddField(
            model_name='player_statistics_ranking',
            name='player_clean_shit',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player_statistics_ranking',
            name='player_game_played',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player_statistics_ranking',
            name='player_shot',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player_statistics_ranking',
            name='player_tackle',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='club_managers',
            name='managers_birth_date',
            field=models.DateField(default=datetime.date(2022, 3, 10)),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_position',
            field=models.CharField(choices=[('striker', 'striker'), ('goalkeeper', 'goalkeeper'), ('left_winger', 'left_winger'), ('right_winger', 'right_winger'), ('fullback', 'fullback'), ('left-fullback', 'left-fullback'), ('right-fullback', 'right-fullback'), ('wingback', 'wingback'), ('left-wingback', 'left-wingback'), ('right-wingback', 'right-wingback'), ('centre_back', 'centre_back'), ('attacking_midfielder', 'attacking_midfielder'), ('defensive_midfielder', 'defensive_midfielder'), ('centre_midfielder', 'centre_midfielder')], max_length=200),
        ),
        migrations.AlterField(
            model_name='player_profile',
            name='player_born',
            field=models.DateTimeField(blank=True, default=datetime.date(2022, 3, 10), null=True),
        ),
    ]