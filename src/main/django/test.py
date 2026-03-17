from .base import *

CACHES = {
  "default": {
    "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
  },
}

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": ":memory:",
  },
}
