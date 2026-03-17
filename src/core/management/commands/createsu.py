from typing import Any

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
  """Custom command to create a superuser with default credentials."""

  def handle(self, *args: Any, **options: Any) -> None:
    """Create a superuser with the provided username and email.

    NOTE: password is optional and read from DJANGO_ADMIN_PASSWORD
          environment variable. If it isn't set, a random password
          will be generated.
    """
    user_model = get_user_model()
    username: str = settings.DJANGO_ADMIN_USERNAME
    if user_model.objects.filter(username=username).exists():
      self.stdout.write(self.style.WARNING("User already exists."))
    else:
      email: str = settings.DJANGO_ADMIN_EMAIL
      password: str = settings.DJANGO_ADMIN_PASSWORD
      user_model.objects.create_superuser(username, email, password)
      self.stdout.write(self.style.SUCCESS(f"Created superuser. Password: {password}"))
