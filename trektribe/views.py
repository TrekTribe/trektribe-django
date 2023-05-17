from datetime import date, timedelta

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import DurationField, ExpressionWrapper, F, Value
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Event


def event_list(request):
    page = request.GET.get("page", 1)
    today = date.today()
    two_days_ago = today - timedelta(days=2)
    now = timezone.now()
    recent_events = (
        Event.objects.filter(date__gte=two_days_ago)
        # .order_by("date")
        .annotate(
            custom_order1=Value(1),
            custom_order2=ExpressionWrapper(F("date") - today, DurationField()),
        )
    )
    generic_events = (
        Event.objects.filter(date__isnull=True)
        # .order_by("-modified_date")
        .annotate(
            custom_order1=Value(2),
            custom_order2=ExpressionWrapper(now - F("modified_date"), DurationField()),
        )
    )
    past_events = (
        Event.objects.filter(date__lt=two_days_ago)
        # .order_by("-date")
        .annotate(
            custom_order1=Value(3),
            custom_order2=ExpressionWrapper(today - F("date"), DurationField()),
        )
    )
    aggregated_events = recent_events.union(generic_events, past_events).order_by(
        "custom_order1", "custom_order2", "-modified_date"
    )
    next_event = aggregated_events.first()
    paginator = Paginator(aggregated_events[1::1], per_page=10)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
        page = 1
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
        page = paginator.num_pages
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
    event.views_count += 1
    event.save()
    return render(
        request,
        "trektribe/event_detail.html",
        {
            "tab_selected": "events",
            "event": event,
        },
    )
