# Generated by Django 4.2.1 on 2023-05-17 07:01
import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("trektribe", "0004_event_short_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Quote",
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
                (
                    "date",
                    models.DateField(default=datetime.date.today, verbose_name="Data"),
                ),
                ("quote", models.TextField(verbose_name="Citazione")),
                ("author", models.CharField(max_length=128, verbose_name="Autore")),
                ("likes", models.IntegerField(default=0, verbose_name="Mi piace")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Utente",
                    ),
                ),
            ],
            options={
                "verbose_name": "Citazione",
                "verbose_name_plural": "Citazioni",
            },
        ),
    ]
