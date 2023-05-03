from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

from .models import Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
        ]

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "date_time",
        ]


class EventDetailSerializer(EventListSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Event
        fields = "__all__"
