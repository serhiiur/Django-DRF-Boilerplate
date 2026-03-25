from typing import TYPE_CHECKING

from django.conf import settings
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from rest_framework import status

if TYPE_CHECKING:
  from django.test.client import Client


def test_health(client: "Client") -> None:
  url = reverse("health")
  resp = client.get(url)
  assert resp.status_code == status.HTTP_200_OK
  assert resp.json() == {"response": "ok"}


def test_version(client: "Client") -> None:
  url = reverse("version")
  resp = client.get(url)
  assert resp.status_code == status.HTTP_200_OK
  assert resp.json() == {"version": settings.SPECTACULAR_SETTINGS["VERSION"]}


def test_index(client: "Client") -> None:
  url = reverse("index")
  resp = client.get(url)
  assert resp.status_code == status.HTTP_200_OK
  assertTemplateUsed(resp, "index.html")

