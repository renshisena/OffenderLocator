# Generated by Django 4.0.1 on 2022-02-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='offenders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offender', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.PositiveSmallIntegerField()),
                ('offense', models.CharField(max_length=45)),
                ('caseStatus', models.CharField(max_length=8)),
                ('casedescription', models.TextField()),
                ('password', models.CharField(max_length=12)),
                ('dateRelease', models.DateField()),
                ('dateTransfer', models.DateField()),
                ('dateComplaint', models.DateField()),
            ],
        ),
    ]
