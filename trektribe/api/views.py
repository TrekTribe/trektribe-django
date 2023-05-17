from rest_framework.viewsets import ReadOnlyModelViewSet

from website.paginations import DefaultLimitOffsetPagination

from ..models import Event, Quote
from .serializers import EventDetailSerializer, EventListSerializer, QuoteSerializer


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
    serializer_class = QuoteSerializer
    filterset_fields = ["quote", "author"]
    search_fields = ["quote", "author"]
