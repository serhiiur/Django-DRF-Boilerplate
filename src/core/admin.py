from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin  # type: ignore[import-untyped]
from unfold.contrib.filters.admin import RangeDateFilter  # type: ignore[import-untyped]
from unfold.forms import (  # type: ignore[import-untyped]
  AdminPasswordChangeForm,
  UserChangeForm,
  UserCreationForm,
)

from .models import User

admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):  # type: ignore[misc]
  """Custom admin for Group model using django-unfold package."""


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):  # type: ignore[misc, type-arg]
  """Custom admin for User model using django-unfold package."""

  form = UserChangeForm
  add_form = UserCreationForm
  change_password_form = AdminPasswordChangeForm
  list_filter = (
    "is_staff",
    "is_active",
    ("created_at", RangeDateFilter),
    ("updated_at", RangeDateFilter),
  )
  readonly_fields = ("last_login", "created_at", "updated_at")
  fieldsets = (
    (None, {"fields": ("username", "password")}),
    (
      "Personal info",
      {"fields": ("first_name", "last_name", "email")},
    ),
    (
      "Permissions",
      {
        "fields": (
          "is_active",
          "is_staff",
          "is_superuser",
          "groups",
          "user_permissions",
        ),
      },
    ),
    (
      "Important dates",
      {"fields": ("last_login", "created_at", "updated_at")},
    ),
  )
  list_display = (
    "username",
    "email",
    "first_name",
    "last_name",
    "is_staff",
    "is_active",
    "created_at",
    "updated_at",
  )
