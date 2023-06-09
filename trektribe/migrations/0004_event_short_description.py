# Generated by Django 4.2.1 on 2023-05-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trektribe", "0003_alter_event_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="short_description",
            field=models.TextField(
                default="",
                help_text="Visualizzata nell'elenco escursioni",
                max_length=500,
                verbose_name="Breve descrizione",
            ),
            preserve_default=False,
        ),
    ]
