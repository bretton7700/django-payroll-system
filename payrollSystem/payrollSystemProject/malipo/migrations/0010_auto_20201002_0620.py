# Generated by Django 3.0.3 on 2020-10-02 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malipo', '0009_auto_20201002_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='timeslot_Check_In_Time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 6, 20, 59, 523896)),
        ),
    ]
