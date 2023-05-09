from datetime import datetime, timezone

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from trektribe.models import Event

User = get_user_model()


class TrekTribeAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create_user("username1", "password1")
        self.user2 = User.objects.create_user("username2", "password2")
        return super().setUp()


class eventApiTestCase(TrekTribeAPITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.event1 = Event.objects.create(
            date_time=datetime(2023, 5, 6, 9, 30, tzinfo=timezone.utc),
            user=self.user1,
        )
        self.event2 = Event.objects.create(
            date_time=datetime(2023, 5, 7, 9, 30, tzinfo=timezone.utc),
            user=self.user2,
        )

    def test_api_calls_require_authentication(self):
        urls = (
            reverse("api-trektribe:event-list"),
            reverse("api-trektribe:event-detail", kwargs={"pk": self.event1.pk}),
        )
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_login(self.user1)
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filtering_by_sezione(self):
        self.client.force_login(self.user1)

        url = reverse("api-trektribe:event-list")
        response = self.client.get(url)
        self.assertEqual(response.json()["count"], 1)
        self.assertEqual(len(response.json()["results"]), 1)

        url = reverse("api-trektribe:event-detail", kwargs={"pk": self.event2.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)