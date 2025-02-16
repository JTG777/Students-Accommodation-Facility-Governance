# Generated by Django 4.2.5 on 2025-02-04 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='OneteamBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isactive', models.BooleanField(default=True, verbose_name='Active')),
                ('branch_name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'OneTeam Branches',
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(max_length=40)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseapp.oneteambranch')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=40, null=True)),
                ('student_dob', models.DateField(help_text='Write date of birth in yyyy-mm-dd format')),
                ('student_no', models.BigIntegerField(unique=True, verbose_name='Mobile No.')),
                ('student_email_id', models.EmailField(default=None, max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=6)),
                ('guardian_name', models.CharField(max_length=40)),
                ('guardian_no', models.BigIntegerField(unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseapp.course')),
                ('oneteam_branch_name', models.ForeignKey(limit_choices_to={'isactive': True}, on_delete=django.db.models.deletion.CASCADE, to='baseapp.oneteambranch')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseapp.trainer')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
