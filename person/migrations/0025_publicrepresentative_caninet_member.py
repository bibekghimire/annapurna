# Generated by Django 5.0.7 on 2024-09-02 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0024_rename_subject_committee_subjectcommittee'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicrepresentative',
            name='caninet_member',
            field=models.BooleanField(default=True, verbose_name='कार्यपालिका सदस्य'),
            preserve_default=False,
        ),
    ]