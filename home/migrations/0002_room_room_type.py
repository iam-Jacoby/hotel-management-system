# Generated by Django 5.1 on 2025-04-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Deluxe', 'Deluxe'), ('Standard', 'Standard'), ('Family', 'Family')], default='Standard', max_length=20),
        ),
    ]
