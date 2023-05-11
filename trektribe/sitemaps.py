from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Event


class EventSitemap(Sitemap):
    priority = 0.6
    changefreq = "weekly"

    def items(self):
        return Event.objects.all()

    def lastmod(self, item):
        return item.modified_date

    def get_domain(self, site):
        # used to override the domain in the sitemap
        return "trektribe.dennybiasiolli.com"

    def location(self, item):
        return reverse("event_detail", kwargs={"pk": item.id})
        # return f"/news/{item.id}/"
