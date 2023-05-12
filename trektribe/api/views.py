from rest_framework.viewsets import ReadOnlyModelViewSet

from website.paginations import DefaultLimitOffsetPagination

from ..models import Event, Quote
from .serializers import (
    EventDetailSerializer,
    EventListSerializer,
    QuoteDetailSerializer,
    QuoteListSerializer,
)


class EventViewSet(ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    pagination_class = DefaultLimitOffsetPagination
    serializers = {
        "list": EventListSerializer,
        "default": EventDetailSerializer,
    }
    filterset_fields = ["title"]
    search_fields = ["title", "description"]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])


class QuoteViewSet(ReadOnlyModelViewSet):
    queryset = Quote.objects.all()
    pagination_class = DefaultLimitOffsetPagination
    serializers = {
        "list": QuoteListSerializer,
        "default": QuoteDetailSerializer,
    }
    filterset_fields = ["quote", "author"]
    search_fields = ["quote", "author"]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])
