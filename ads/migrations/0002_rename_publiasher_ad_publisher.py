# Generated by Django 4.1 on 2024-04-24 20:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ad",
            old_name="publiasher",
            new_name="publisher",
        ),
    ]