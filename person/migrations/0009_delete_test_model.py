# Generated by Django 5.0.6 on 2024-08-13 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0008_remove_test_model_year'),
    ]

    operations = [
        migrations.DeleteModel(
            name='test_model',
        ),
    ]
