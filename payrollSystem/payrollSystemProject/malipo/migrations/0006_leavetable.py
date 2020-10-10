# Generated by Django 3.0.3 on 2020-09-30 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('malipo', '0005_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveTable',
            fields=[
                ('leave_ID', models.AutoField(primary_key=True, serialize=False)),
                ('leave_Start_Date', models.DateField()),
                ('leave_End_Date', models.DateField()),
                ('leave_employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='malipo.Employee')),
            ],
            options={
                'db_table': 'LeaveTable',
            },
        ),
    ]