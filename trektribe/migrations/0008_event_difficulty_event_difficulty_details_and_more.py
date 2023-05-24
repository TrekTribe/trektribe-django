# Generated by Django 4.2.1 on 2023-05-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trektribe", "0007_event_whatsapp_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="difficulty",
            field=models.CharField(
                blank=True, max_length=10, verbose_name="Difficoltà"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="difficulty_details",
            field=models.TextField(
                blank=True, verbose_name="Maggiori dettagli sulla difficoltà"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="distance",
            field=models.FloatField(
                blank=True,
                help_text="Se non indicata, verrà calcolata dalla traccia GPX",
                null=True,
                verbose_name="Lunghezza (km)",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="elevation_gain",
            field=models.IntegerField(
                blank=True,
                help_text="Se non indicato, verrà calcolato dalla traccia GPX",
                null=True,
                verbose_name="Dislivello (m)",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="max_altitude",
            field=models.IntegerField(
                blank=True,
                help_text="Se non indicata, verrà calcolata dalla traccia GPX",
                null=True,
                verbose_name="Altitudine massima (m)",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="starting_altitude",
            field=models.IntegerField(
                blank=True,
                help_text="Se non indicata, verrà calcolata dalla traccia GPX",
                null=True,
                verbose_name="Altitudine di partenza (m)",
            ),
        ),
    ]
