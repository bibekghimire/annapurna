# Generated by Django 5.0.6 on 2024-08-04 23:39

import person.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_alter_employee_mobile_number_alter_post_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_for',
            field=models.IntegerField(choices=person.models.Choices.catagory, default=1),
        ),
    ]