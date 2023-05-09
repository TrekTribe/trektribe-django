# Generated by Django 4.2.1 on 2023-05-09 13:22

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                ("date", models.DateField(verbose_name="Data")),
                ("title", models.CharField(max_length=128, verbose_name="Titolo")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Descrizione estesa"),
                ),
                (
                    "gpx_track",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="gpx_tracks/uploads/%Y/%m/%d/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["gpx"]
                            )
                        ],
                        verbose_name="Traccia GPX",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Utente organizzatore",
                    ),
                ),
            ],
            options={
                "verbose_name": "Evento",
                "verbose_name_plural": "Eventi",
            },
        ),
    ]
