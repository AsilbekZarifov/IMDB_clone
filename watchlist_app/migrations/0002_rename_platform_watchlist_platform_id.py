# Generated by Django 4.2.7 on 2023-12-06 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='platform',
            new_name='platform_id',
        ),
    ]