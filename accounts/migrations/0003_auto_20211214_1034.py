# Generated by Django 2.2 on 2021-12-14 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211210_1147'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='register',
            new_name='user',
        ),
    ]
