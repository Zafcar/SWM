# Generated by Django 4.1.7 on 2023-03-31 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SWM', '0002_collection_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection_location',
            name='Garbage_type',
            field=models.CharField(choices=[('CW', 'Cloth Waste'), ('GW', 'Glass Waste'), ('EW', 'Electronic Waste')], default=123, max_length=10),
            preserve_default=False,
        ),
    ]
