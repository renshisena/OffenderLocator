# Generated by Django 4.0.1 on 2022-02-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offenderLocatorApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offenders',
            name='casedescription',
        ),
        migrations.AddField(
            model_name='offenders',
            name='caseDescription',
            field=models.TextField(max_length=400, null=b'I01\n', verbose_name='caseDescription'),
            preserve_default=b'I01\n',
        ),
        migrations.AddField(
            model_name='offenders',
            name='offenderID',
            field=models.CharField(max_length=4, null=b'I01\n', verbose_name='offenderID'),
            preserve_default=b'I01\n',
        ),
        migrations.AlterField(
            model_name='offenders',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='offenders',
            name='caseStatus',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Release', 'Release'), ('Transfer', 'Transfer')], default='Ongoing', max_length=8),
        ),
        migrations.AlterField(
            model_name='offenders',
            name='dateComplaint',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='offenders',
            name='dateRelease',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='offenders',
            name='dateTransfer',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='offenders',
            name='gender',
            field=models.CharField(max_length=6, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='offenders',
            name='offender',
            field=models.CharField(max_length=45, verbose_name='offender'),
        ),
        migrations.AlterField(
            model_name='offenders',
            name='offense',
            field=models.CharField(max_length=45, verbose_name='offense'),
        ),
        migrations.AlterField(
            model_name='offenders',
            name='password',
            field=models.CharField(max_length=12, verbose_name='password'),
        ),
    ]
