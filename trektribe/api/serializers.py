from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Event, Quote

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="get_full_name")

    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
        ]


class EventListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "date",
            "user",
        ]


class EventDetailSerializer(EventListSerializer):
    user_id = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )

    class Meta:
        model = Event
        fields = "__all__"


class QuoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = [
            "id",
            "quote",
            "date_time",
            "likes",
        ]


class QuoteDetailSerializer(EventListSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Quote
        fields = "__all__"
