from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    display_name = models.CharField(
        max_length=50, blank=True, verbose_name="Nome visualizzato"
    )
    bio = RichTextField(verbose_name="Bio", blank=True)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = "Profilo Utente"
        verbose_name_plural = "Profili Utente"


class SocialLink(models.Model):
    class LinkType(models.TextChoices):
        FACEBOOK = "facebook", "Facebook"
        INSTAGRAM = "instagram", "Instagram"
        TELEGRAM = "telegram", "Telegram"
        TIKTOK = "tiktok", "TikTok"
        TWITTER = "twitter", "Twitter"
        WHATSAPP = "whatsapp", "WhatsApp"
        YOUTUBE = "youtube", "YouTube"
        LINKEDIN = "linkedin", "LinkedIn"
        WEBSITE = "website", "Sito Web"
        OTHER = "other", "Altro"

        LINK_TYPES_WITH_RELATED_ICON = [
            FACEBOOK,
            INSTAGRAM,
            TELEGRAM,
            TIKTOK,
            TWITTER,
            WHATSAPP,
            YOUTUBE,
            LINKEDIN,
        ]

    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="social_links"
    )
    link_type = models.CharField(
        max_length=max(len(v) for v in LinkType.values),
        choices=LinkType.choices,
        verbose_name="Tipo di link",
    )
    url = models.URLField(verbose_name="URL")

    def __str__(self) -> str:
        return f"{self.get_link_type_display()}: {self.url}"

    class Meta:
        verbose_name = "Link Social"
        verbose_name_plural = "Links Social"
