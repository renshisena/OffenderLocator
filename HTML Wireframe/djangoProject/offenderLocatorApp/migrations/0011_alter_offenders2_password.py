# Generated by Django 4.0.1 on 2022-02-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offenderLocatorApp', '0010_remove_offenders2_newpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offenders2',
            name='password',
            field=models.CharField(default='admin', max_length=12, null=True, verbose_name='password'),
        ),
    ]
