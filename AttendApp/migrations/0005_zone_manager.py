# Generated by Django 3.0.2 on 2020-01-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AttendApp', '0004_site_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='manager',
            field=models.CharField(default='', max_length=100),
        ),
    ]
