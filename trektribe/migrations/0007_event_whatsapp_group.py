# Generated by Django 4.2.1 on 2023-05-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trektribe", "0006_event_views_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="whatsapp_group",
            field=models.URLField(
                blank=True,
                help_text=(
                    "Visualizzato solo se è indicata anche la data,"
                    + " e fino a quello stesso giorno."
                ),
                verbose_name="Link gruppo WhatsApp dedicato",
            ),
        ),
    ]