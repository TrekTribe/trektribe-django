from typing import Any, Dict

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from .models import SocialLink, UserProfile

User = get_user_model()


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "link_type", "url"]
    list_filter = ["link_type", ("user_profile", admin.RelatedOnlyFieldListFilter)]

    def get_model_perms(self, request: HttpRequest) -> Dict[str, bool]:
        if not request.user.is_superuser:
            return {}
        return super().get_model_perms(request)


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    max_num = 10


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "get_user_email", "display_name"]
    list_select_related = ["user"]
    readonly_fields = ["user"]
    inlines = [SocialLinkInline]

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    @admin.display(ordering="user__email", description="Email")
    def get_user_email(self, obj):
        return obj.user.email

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)
        return qs


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False
    show_change_link = True


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super().add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline]
        return super().change_view(*args, **kwargs)
