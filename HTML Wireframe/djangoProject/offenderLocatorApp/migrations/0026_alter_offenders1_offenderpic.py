# Generated by Django 4.0.1 on 2022-06-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offenderLocatorApp', '0025_alter_offenders1_offenderpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offenders1',
            name='offenderPic',
            field=models.ImageField(blank=b'I01\n', null=b'I01\n', upload_to='Media/'),
        ),
    ]
