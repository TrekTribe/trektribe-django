# Generated by Django 4.2.1 on 2023-05-19 13:04

import django.db.models.deletion
from django.db import migrations, models

from user_profile.models import SocialLink


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0002_add_existing_profiles"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialLink",
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
                (
                    "link_type",
                    models.CharField(
                        choices=SocialLink.LinkType.choices,
                        max_length=9,
                        verbose_name="Tipo di link",
                    ),
                ),
                ("url", models.URLField(verbose_name="URL")),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="social_links",
                        to="user_profile.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Link Social",
                "verbose_name_plural": "Links Social",
            },
        ),
    ]
