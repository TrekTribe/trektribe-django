from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from trektribe.models import Event, Quote

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
            date=date(2023, 5, 6),
            user=self.user1,
        )
        self.event2 = Event.objects.create(
            date=date(2023, 5, 7),
            user=self.user2,
        )
        self.quote1 = Quote.objects.create(
            quote="The most important thing is to be whatever you are without shame.",
            author="Rod Steiger",
            user=self.user1,
        )
        self.quote2 = Quote.objects.create(
            quote="There are some things you learn best in calm, and some in storm.",
            author="Willa Cather",
            user=self.user2,
        )

    def test_api_calls_require_authentication(self):
        urls = (
            reverse("api-trektribe:event-list"),
            reverse("api-trektribe:event-detail", kwargs={"pk": self.event1.pk}),
            reverse("api-trektribe:quote-list"),
            reverse("api-trektribe:quote-detail", kwargs={"pk": self.quote1.pk}),
        )
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_login(self.user1)
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_events(self):
        self.client.force_login(self.user1)

        url = reverse("api-trektribe:event-list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(data["count"], 2)
        self.assertEqual(len(data["results"]), 2)

        url = reverse("api-trektribe:event-detail", kwargs={"pk": self.event2.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_quotes(self):
        self.client.force_login(self.user1)

        url = reverse("api-trektribe:quote-list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(data["count"], 2)
        self.assertEqual(len(data["results"]), 2)

        url = reverse("api-trektribe:quote-detail", kwargs={"pk": self.quote2.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
