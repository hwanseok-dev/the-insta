# Generated by Django 3.1.5 on 2021-01-30 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210130_2050'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Owner',
        ),
    ]