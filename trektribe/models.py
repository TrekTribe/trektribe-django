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
    date = models.DateField(verbose_name="Data")
    title = models.CharField(
        verbose_name="Titolo",
        max_length=128,
    )
    description = models.TextField(verbose_name="Descrizione estesa", blank=True)
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
        return f"{self.date.strftime('%Y-%m-%d')} - {self.title}"
