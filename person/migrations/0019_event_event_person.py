# Generated by Django 5.0.6 on 2024-08-21 14:26

import person.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0018_alter_event_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_person',
            field=models.IntegerField(choices=person.models.Choices.event_person_choices, default=1, verbose_name='पदाधिकारी/कर्मचारी'),
        ),
    ]
