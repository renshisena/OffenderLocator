# Generated by Django 4.0.1 on 2022-02-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offenderLocatorApp', '0006_remove_offenders1_datecomplaint_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offenders1',
            name='caseStatus',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Released', 'Released'), ('Transferred', 'Transferred')], default='Ongoing', max_length=11),
        ),
    ]
