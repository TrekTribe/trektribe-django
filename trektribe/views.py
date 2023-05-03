from rest_framework.viewsets import ModelViewSet

from website.paginations import DefaultLimitOffsetPagination

from .models import Event
from .serializers import EventDetailSerializer, EventListSerializer


class EventViewSet(ModelViewSet):
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

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
