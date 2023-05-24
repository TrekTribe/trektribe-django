from datetime import date

from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Utente organizzatore"
    )
    date = models.DateField(verbose_name="Data", null=True, blank=True)
    title = models.CharField(
        verbose_name="Titolo",
        max_length=128,
    )
    short_description = models.TextField(
        verbose_name="Breve descrizione",
        max_length=500,
        help_text="Visualizzata nell'elenco escursioni",
    )
    whatsapp_group = models.URLField(
        verbose_name="Link gruppo WhatsApp dedicato",
        blank=True,
        help_text=(
            "Visualizzato solo se è indicata anche la data,"
            + " e fino a quello stesso giorno."
        ),
    )
    distance = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Lunghezza (km)",
        help_text="Se non indicata, verrà calcolata dalla traccia GPX",
    )
    elevation_gain = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Dislivello (m)",
        help_text="Se non indicato, verrà calcolato dalla traccia GPX",
    )
    starting_altitude = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Altitudine di partenza (m)",
        help_text="Se non indicata, verrà calcolata dalla traccia GPX",
    )
    max_altitude = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Altitudine massima (m)",
        help_text="Se non indicata, verrà calcolata dalla traccia GPX",
    )
    difficulty = models.CharField(max_length=10, blank=True, verbose_name="Difficoltà")
    difficulty_details = models.TextField(
        blank=True, verbose_name="Maggiori dettagli sulla difficoltà"
    )
    #  Altitudine partenza: 890 m
    #  Altitudine massima: 1.763 m
    #  Difficoltà: E (Escursionisti)
    # info difficoltà

    description = RichTextField(verbose_name="Descrizione estesa", blank=True)
    gpx_track = models.FileField(
        verbose_name="Traccia GPX",
        upload_to="gpx_tracks/uploads/%Y/%m/%d/",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["gpx"])],
    )
    views_count = models.BigIntegerField(
        verbose_name="Contatore visualizzazioni", default=0
    )

    @property
    def is_past_due(self):
        return self.date and date.today() > self.date

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventi"

    def __str__(self) -> str:
        if self.date:
            return f"{self.date.strftime('%Y-%m-%d')} - {self.title}"
        else:
            return self.title


class Quote(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utente")
    date = models.DateField(verbose_name="Data", default=date.today)
    quote = models.TextField(verbose_name="Citazione")
    author = models.CharField(verbose_name="Autore", max_length=128)
    likes = models.IntegerField(verbose_name="Mi piace", default=0)

    class Meta:
        verbose_name = "Citazione"
        verbose_name_plural = "Citazioni"

    def __str__(self) -> str:
        if self.date:
            return f"{self.date.strftime('%Y-%m-%d')} - {self.quote} - {self.author}"
        else:
            return f"{self.quote} - {self.author}"
