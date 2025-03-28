# Generated by Django 4.2.5 on 2025-02-05 12:15

from django.db import migrations

def copy_room_data(apps, schema_editor):
    RoomAssign = apps.get_model('hostel', 'RoomAssign')
    for obj in RoomAssign.objects.all():
        obj.room_new = obj.room  # Copy old field value to the new field
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0003_roomassign_room_new'),
    ]

    operations = [
        migrations.RunPython(copy_room_data),
    ]
