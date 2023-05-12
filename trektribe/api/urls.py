from rest_framework.routers import DefaultRouter

from .views import EventViewSet, QuoteViewSet

router = DefaultRouter()
router.register("events", EventViewSet)
router.register("quotes", QuoteViewSet)
