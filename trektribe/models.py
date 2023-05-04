from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(verbose_name="Data e ora")
    title = models.CharField(verbose_name="Titolo", max_length=128)
    description = models.TextField(verbose_name="Descrizione estesa", blank=True)
