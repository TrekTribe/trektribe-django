import time
from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from trektribe.models import Event

User = get_user_model()


class TrekTribeTestCase(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create_user("username1", "password1")
        return super().setUp()


class EventTests(TrekTribeTestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_event_list_ensure_context_and_sorting(self):
        elements_to_create = 4
        days_ago = 2
        today = date.today()
        # recent events
        for i in range(elements_to_create):
            Event.objects.create(
                user=self.user1,
                date=(today + timedelta(days=i - days_ago)),
                title=f"recent event {i+1}",
            )
        # generic events
        for i in range(elements_to_create):
            Event.objects.create(
                user=self.user1,
                date=None,
                title=f"generic event {i+1}",
            )
            time.sleep(0.2)
        # past events
        for i in range(elements_to_create):
            Event.objects.create(
                user=self.user1,
                date=(today + timedelta(days=i - elements_to_create - days_ago)),
                title=f"past event {i+1}",
            )
        response = self.client.get(reverse("event_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tab_selected"], "events")
        self.assertEqual(response.context["next_event"].title, "recent event 1")
        self.assertEqual(response.context["page_obj"].paginator.per_page, 10)
        self.assertEqual(response.context["page_obj"].paginator.count, 11)
        self.assertEqual(response.context["page_obj"].paginator.num_pages, 2)
        self.assertIn("page_range", response.context)

        self.assertEqual(response.context["page_obj"][0].title, "recent event 2")
        self.assertEqual(response.context["page_obj"][1].title, "recent event 3")
        self.assertEqual(response.context["page_obj"][2].title, "recent event 4")
        self.assertEqual(response.context["page_obj"][3].title, "generic event 4")
        self.assertEqual(response.context["page_obj"][4].title, "generic event 3")
        self.assertEqual(response.context["page_obj"][5].title, "generic event 2")
        self.assertEqual(response.context["page_obj"][6].title, "generic event 1")
        self.assertEqual(response.context["page_obj"][7].title, "past event 4")
        self.assertEqual(response.context["page_obj"][8].title, "past event 3")
        self.assertEqual(response.context["page_obj"][9].title, "past event 2")
