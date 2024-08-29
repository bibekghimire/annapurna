# Generated by Django 5.0.7 on 2024-07-29 00:47

import django.core.validators
import django.db.models.deletion
import person.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='पदनाम')),
                ('post_for', models.IntegerField(choices=person.models.Choices.catagory, default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_mobile_number', message='Mobile number must be 10 digits starting with 9.', regex='^9[0-9]{9}$')])),
                ('email', models.EmailField(default='hello@example.com', max_length=254)),
                ('status', models.IntegerField(choices=person.models.Choices.StatusChoices, default=1)),
                ('weight', models.IntegerField(choices=person.models.Choices.IntegerChoices100, default=1)),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_personalinfo', to='person.post')),
            ],
            options={
                'verbose_name': 'कर्मचारि',
                'verbose_name_plural': 'कर्मचारिहरु',
            },
        ),
        migrations.CreateModel(
            name='PublicRepresentative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_mobile_number', message='Mobile number must be 10 digits starting with 9.', regex='^9[0-9]{9}$')])),
                ('email', models.EmailField(default='hello@example.com', max_length=254)),
                ('status', models.IntegerField(choices=person.models.Choices.StatusChoices, default=1)),
                ('weight', models.IntegerField(choices=person.models.Choices.IntegerChoices100, default=1)),
                ('ward', models.PositiveBigIntegerField(choices=person.models.Choices.WardChoices, default=1)),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_personalinfo', to='person.post')),
            ],
            options={
                'verbose_name': 'जनप्रतिनिधि',
                'verbose_name_plural': 'जनप्रतिनिधिहरु',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='शाखा')),
                ('head', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headed_section', to='person.employee', verbose_name='शाखा प्रमुख')),
            ],
            options={
                'verbose_name': 'शाखा',
                'verbose_name_plural': 'शाखाहरु',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='section',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='person.section'),
        ),
    ]
