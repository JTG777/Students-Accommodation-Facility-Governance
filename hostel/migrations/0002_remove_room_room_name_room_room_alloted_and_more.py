# Generated by Django 4.2.5 on 2025-02-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_name',
        ),
        migrations.AddField(
            model_name='room',
            name='room_alloted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='room_max_capacity',
            field=models.IntegerField(default=1),
        ),
    ]
