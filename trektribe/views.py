from datetime import date, timedelta

from django.shortcuts import get_object_or_404, render

from .models import Event


def event_list(request):
    two_days_ago = date.today() - timedelta(days=2)
    events = Event.objects.filter(date__gte=two_days_ago).order_by("date")
    return render(request, "trektribe/event_list.html", {"events": events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, "trektribe/event_detail.html", {"event": event})
