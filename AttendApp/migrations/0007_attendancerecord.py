# Generated by Django 3.0.2 on 2020-01-22 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AttendApp', '0006_shift'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('zonal_manager', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AttendApp.Site')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AttendApp.Zone')),
            ],
        ),
    ]