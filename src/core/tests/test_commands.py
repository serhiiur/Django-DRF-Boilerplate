from io import StringIO
from typing import TYPE_CHECKING

import pytest
from django.core.management import call_command
from django.test import override_settings

if TYPE_CHECKING:
  from django.contrib.auth.models import User
  from faker import Faker

@pytest.mark.django_db
def test_createsu_success(
  faker: "Faker",
  django_user_model: type["User"],
) -> None:
  """Test that createsu management command creates a superuser."""
  output = StringIO()
  username = faker.user_name()
  email = faker.email()
  password = faker.password()

  with override_settings(
    DJANGO_ADMIN_USERNAME=username,
    DJANGO_ADMIN_EMAIL=email,
    DJANGO_ADMIN_PASSWORD=password,
  ):
    call_command("createsu", stdout=output, no_color=True)

  user = django_user_model.objects.get(username=username)
  assert user.email == email
  assert user.is_superuser is True
  assert user.is_staff is True
  assert user.check_password(password) is True
  assert f"Created superuser. Password: {password}" in output.getvalue()


@pytest.mark.django_db
def test_createsu_user_already_exists(
  faker: "Faker",
  django_user_model: type["User"],
) -> None:
  """Test that createsu skips creation if user already exists."""
  output = StringIO()
  existing_user = django_user_model.objects.create_user(
    username=faker.user_name(),
    email=faker.email(),
    password=faker.password(),
  )
  user_count_before = django_user_model.objects.count()

  with override_settings(
    DJANGO_ADMIN_USERNAME=existing_user.username,
    DJANGO_ADMIN_EMAIL=faker.email(),
    DJANGO_ADMIN_PASSWORD=faker.password(),
  ):
    call_command("createsu", stdout=output, no_color=True)

  assert django_user_model.objects.count() == user_count_before
  assert "User already exists." in output.getvalue()
