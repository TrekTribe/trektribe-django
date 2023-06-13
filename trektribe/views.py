from datetime import date, timedelta

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import connection
from django.db.models import DurationField, ExpressionWrapper, F, Value
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from user_profile.models import SocialLink, UserProfile

from .models import Event


def _get_search_qs(search):
    if connection.vendor == "postgresql":
        search_vector = SearchVector(
            "title", weight="A", config="italian"
        ) + SearchVector("short_description", weight="B", config="italian")
        search_query = SearchQuery(search, config="italian")
        search_rank = SearchRank(search_vector, search_query)
        qs = Event.objects.annotate(search=search_vector, rank=search_rank).filter(
            search=search_query
        )
    else:
        search_title_qs = Event.objects.filter(title__icontains=search).annotate(
            rank=Value(1.0)
        )
        search_short_description_qs = (
            Event.objects.filter(short_description__icontains=search)
            .exclude(title__icontains=search)
            .annotate(rank=Value(0.4))
        )
        qs = search_title_qs.union(search_short_description_qs)
    return qs.order_by("-rank")


def _get_event_qs():
    today = date.today()
    two_days_ago = today - timedelta(days=2)
    now = timezone.now()

    qs = Event.objects.all()
    recent_events = (
        qs.filter(date__gte=two_days_ago)
        # .order_by("date")
        .annotate(
            custom_order1=Value(1),
            custom_order2=ExpressionWrapper(F("date") - today, DurationField()),
        )
    )
    generic_events = (
        qs.filter(date__isnull=True)
        # .order_by("-modified_date")
        .annotate(
            custom_order1=Value(2),
            custom_order2=ExpressionWrapper(now - F("modified_date"), DurationField()),
        )
    )
    past_events = (
        qs.filter(date__lt=two_days_ago)
        # .order_by("-date")
        .annotate(
            custom_order1=Value(3),
            custom_order2=ExpressionWrapper(today - F("date"), DurationField()),
        )
    )
    aggregated_events = recent_events.union(generic_events, past_events).order_by(
        "custom_order1", "custom_order2", "-modified_date"
    )
    return aggregated_events


def event_list(request):
    page = request.GET.get("page", 1)
    search = request.GET.get("search", "")

    if search:
        qs = _get_search_qs(search)
    else:
        qs = _get_event_qs()

    next_event = None
    start_index = 0
    if not search:
        next_event = qs.first()
        start_index = 1

    paginator = Paginator(qs[start_index::1], per_page=10)
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
            "search": search,
        },
    )


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if not request.user.is_authenticated:
        Event.objects.filter(pk=pk).update(
            views_count=event.views_count + 1,
            modified_date=event.modified_date,
        )
    return render(
        request,
        "trektribe/event_detail.html",
        {
            "tab_selected": "events",
            "event": event,
        },
    )


def info(request):
    return render(request, "trektribe/info.html", {"tab_selected": "info"})


def user_profile_detail(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    return render(
        request,
        "trektribe/user_profile_detail.html",
        {
            "user_profile": user_profile,
            "link_types_with_related_icon": SocialLink.LINK_TYPES_WITH_RELATED_ICON,
        },
    )
