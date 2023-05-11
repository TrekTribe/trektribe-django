from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views
from .sitemaps import EventSitemap

urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("event/<int:pk>/", views.event_detail, name="event_detail"),
    path(
        "trektribe-sitemap.xml",
        sitemap,
        {
            "sitemaps": {
                "events": EventSitemap,
            },
        },
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
