# Generated by Django 4.0.1 on 2022-02-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offenderLocatorApp', '0005_offenders2_delete_offenders_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offenders1',
            name='dateComplaint',
        ),
        migrations.AlterField(
            model_name='offenders1',
            name='caseStatus',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Released', 'Release'), ('Transferred', 'Transfer')], default='Ongoing', max_length=11),
        ),
    ]
