# Generated by Django 2.2 on 2021-12-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]