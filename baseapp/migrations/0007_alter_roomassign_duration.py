# Generated by Django 4.2.4 on 2023-09-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0006_remove_roomassign_room_left_date_roomassign_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomassign',
            name='Duration',
            field=models.IntegerField(default=None, help_text='In months'),
        ),
    ]
