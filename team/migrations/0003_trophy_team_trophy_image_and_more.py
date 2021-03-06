# Generated by Django 4.0.2 on 2022-03-02 20:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_player_statistics_ranking_player_team_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trophy_team',
            name='trophy_image',
            field=models.ImageField(default='cup.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='player_profile',
            name='player_born',
            field=models.DateTimeField(blank=True, default=datetime.date(2022, 3, 2), null=True),
        ),
        migrations.AlterField(
            model_name='trophy',
            name='trophy_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='trophy',
            name='trophy_year',
            field=models.DateField(),
        ),
    ]
