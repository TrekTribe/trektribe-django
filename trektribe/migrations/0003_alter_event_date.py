# Generated by Django 4.2.1 on 2023-05-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trektribe", "0002_alter_event_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="date",
            field=models.DateField(blank=True, null=True, verbose_name="Data"),
        ),
    ]
