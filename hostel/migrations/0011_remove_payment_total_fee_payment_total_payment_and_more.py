# Generated by Django 4.2.5 on 2025-02-08 19:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0010_room_room_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='total_fee',
        ),
        migrations.AddField(
            model_name='payment',
            name='total_payment',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='fees_type',
            field=models.CharField(default='ONE TIME', max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pending_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='room_assigned',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostel.roomassign'),
        ),
        migrations.AlterField(
            model_name='roomassign',
            name='Duration',
            field=models.IntegerField(default=1, help_text='In months'),
        ),
        migrations.AlterField(
            model_name='roomassign',
            name='room_assigned_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='RecurringPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateField()),
                ('is_paid', models.BooleanField(default=False)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.payment')),
            ],
        ),
    ]
