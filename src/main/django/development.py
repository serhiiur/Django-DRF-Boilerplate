from main.settings.debug_toolbar import *

from .base import *

INSTALLED_APPS.extend(
  [
    "silk",
    "debug_toolbar",
    "django_extensions",
  ]
)

# DebugToolbarMiddleware should be placed as early as possible
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
MIDDLEWARE.append("silk.middleware.SilkyMiddleware")
