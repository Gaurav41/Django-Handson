# Generated by Django 3.2.6 on 2021-08-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0002_volume_switch_to_decimal'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricehistory',
            name='temp',
            field=models.CharField(default='', max_length=10),
        ),
    ]