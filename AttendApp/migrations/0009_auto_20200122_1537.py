# Generated by Django 3.0.2 on 2020-01-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AttendApp', '0008_auto_20200122_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]