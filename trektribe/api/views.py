from rest_framework.viewsets import ReadOnlyModelViewSet

from website.paginations import DefaultLimitOffsetPagination

from ..models import Event
from .serializers import EventDetailSerializer, EventListSerializer


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
