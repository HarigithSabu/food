# Generated by Django 2.2 on 2021-12-16 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20211214_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password2',
        ),
    ]
