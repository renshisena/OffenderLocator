# Generated by Django 4.0.1 on 2022-02-08 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offenderLocatorApp', '0014_alter_offenders2_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offenders2',
            name='password',
            field=models.CharField(default='admin', max_length=12, null=b'I01\n', verbose_name='password'),
        ),
    ]