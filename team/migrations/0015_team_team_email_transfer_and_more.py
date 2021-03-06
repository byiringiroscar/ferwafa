# Generated by Django 4.0.2 on 2022-03-29 11:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0014_alter_connect_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_email_transfer',
            field=models.EmailField(default='aimegalile@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='club_managers',
            name='managers_birth_date',
            field=models.DateField(default=datetime.date(2022, 3, 29)),
        ),
        migrations.AlterField(
            model_name='connect_message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 29, 11, 16, 9, 542796, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='player_profile',
            name='player_born',
            field=models.DateTimeField(blank=True, default=datetime.date(2022, 3, 29), null=True),
        ),
    ]
