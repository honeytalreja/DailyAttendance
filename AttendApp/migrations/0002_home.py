# Generated by Django 3.0.2 on 2020-01-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AttendApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('data', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]
