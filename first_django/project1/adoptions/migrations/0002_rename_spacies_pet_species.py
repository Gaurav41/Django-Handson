# Generated by Django 3.2.6 on 2021-08-11 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='spacies',
            new_name='species',
        ),
    ]
