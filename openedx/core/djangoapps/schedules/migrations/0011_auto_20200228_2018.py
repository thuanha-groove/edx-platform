# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-28 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0010_remove_null_blank_from_schedules_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleexperience',
            name='schedule',
            field=models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='schedules.Schedule'),
        ),
    ]
