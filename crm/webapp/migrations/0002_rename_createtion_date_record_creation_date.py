# Generated by Django 5.0.6 on 2024-05-29 10:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="record",
            old_name="createtion_date",
            new_name="creation_date",
        ),
    ]
