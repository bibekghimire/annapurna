# Generated by Django 5.0.6 on 2024-08-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0010_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name='मिति चयन गर्नुहोस'),
        ),
    ]
