# Generated by Django 3.0.2 on 2020-01-21 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AttendApp', '0003_auto_20200122_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='zone',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AttendApp.Zone'),
        ),
    ]
