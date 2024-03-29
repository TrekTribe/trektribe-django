from django.contrib import admin
from django.contrib.auth import get_user_model
from django.http import HttpRequest

from .models import Event, Quote

User = get_user_model()


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "user", "short_description", "views_count"]
    list_filter = ["date", ("user", admin.RelatedOnlyFieldListFilter)]
    ordering = ["-date", "-modified_date"]
    readonly_fields = ["views_count"]
    search_fields = ["title", "short_description", "description"]

    def get_queryset(self, request: HttpRequest):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["initial"] = request.user.id
            if not request.user.is_superuser:
                kwargs["queryset"] = User.objects.filter(pk=request.user.id)
        return super(EventAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ["quote", "author", "date", "user"]
    list_filter = ["date", ("user", admin.RelatedOnlyFieldListFilter)]
    search_fields = ["quote", "author"]

    def get_queryset(self, request: HttpRequest):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["initial"] = request.user.id
            if not request.user.is_superuser:
                kwargs["queryset"] = User.objects.filter(pk=request.user.id)
        return super(QuoteAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )
