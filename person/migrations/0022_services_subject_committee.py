# Generated by Django 5.0.7 on 2024-08-27 02:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0021_alter_employee_email_alter_employee_mobile_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='सेवा')),
                ('required_docs', models.TextField()),
                ('serv_fee', models.PositiveBigIntegerField(verbose_name='लाग्ने शुल्क')),
                ('serv_time', models.CharField(max_length=200, verbose_name='लाग्ने समय')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='person.section', verbose_name='सम्बन्धित शाखा')),
            ],
        ),
        migrations.CreateModel(
            name='subject_committee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='विषयगत समितिको नाम')),
                ('coordinator', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coordinated_committee', to='person.publicrepresentative', verbose_name='समिति संयोजक')),
                ('members', models.ManyToManyField(blank=True, to='person.publicrepresentative', verbose_name='सदस्य हरु')),
                ('secretary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='committes_secretary', to='person.employee', verbose_name='सदस्य सचिव')),
            ],
        ),
    ]
