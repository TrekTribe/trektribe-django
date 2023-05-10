from datetime import date, timedelta

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Event


def event_list(request):
    page = request.GET.get("page", 1)
    two_days_ago = date.today() - timedelta(days=2)
    recent_events = Event.objects.filter(date__gte=two_days_ago).order_by("date")
    past_events = Event.objects.filter(date__lte=two_days_ago).order_by("date")
    generic_events = Event.objects.filter(date__isnull=True).order_by("id")
    aggregated_events = recent_events | past_events | generic_events
    next_event = aggregated_events.first()
    paginator = Paginator(aggregated_events[1:], per_page=10)
    page_obj = paginator.get_page(page)
    page_range = page_obj.paginator.get_elided_page_range(number=page)
    return render(
        request,
        "trektribe/event_list.html",
        {
            "tab_selected": "events",
            "next_event": next_event,
            "page_obj": page_obj,
            "page_range": page_range,
        },
    )


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(
        request,
        "trektribe/event_detail.html",
        {
            "tab_selected": "events",
            "event": event,
        },
    )
