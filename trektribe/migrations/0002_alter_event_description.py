# Generated by Django 4.2.1 on 2023-05-09 21:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("trektribe", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="description",
            field=ckeditor.fields.RichTextField(
                blank=True, verbose_name="Descrizione estesa"
            ),
        ),
    ]
