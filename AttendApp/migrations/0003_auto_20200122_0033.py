# Generated by Django 3.0.2 on 2020-01-21 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AttendApp', '0002_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Location',
            new_name='Site',
        ),
    ]
