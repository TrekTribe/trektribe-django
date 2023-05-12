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
    description = RichTextField(verbose_name="Descrizione estesa", blank=True)
    gpx_track = models.FileField(
        verbose_name="Traccia GPX",
        upload_to="gpx_tracks/uploads/%Y/%m/%d/",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["gpx"])],
    )

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
    date = models.DateField(verbose_name="Data")
    quote = models.CharField(verbose_name="Citazione", max_length=1028)
    likes = models.IntegerField(verbose_name="Mi piace")
    author = models.CharField(verbose_name="Autore", max_length=128)

    class Meta:
        verbose_name = "Citazione"
        verbose_name_plural = "Citazioni"
