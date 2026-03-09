import os

from pythonjsonlogger.jsonlogger import JsonFormatter

from main.constants import DjangoSettingsModule
from main.env import env

formatter = (
  "verbose"
  if os.environ["DJANGO_SETTINGS_MODULE"] == DjangoSettingsModule.DEVELOPMENT
  else "json"
)
LOG_LEVEL = env.str("DJANGO_LOG_LEVEL", default="INFO").upper()
LOGGING = {
  "version": 1,
  "disable_existing_loggers": False,
  "handlers": {
    "console": {
      "level": LOG_LEVEL,
      "class": "logging.StreamHandler",
      "formatter": formatter,
    },
  },
  "loggers": {
    "": {
      "handlers": ["console"],
      "level": LOG_LEVEL,
    },
  },
  "formatters": {
    "json": {
      "()": JsonFormatter,
      "format": "%(asctime)s %(levelname)s %(message)s %(module)s",
    },
    "verbose": {
      "format": "{asctime} {levelname} - {name}.{module}.py (line {lineno:d}). {message}",  # noqa: E501
      "style": "{",
    },
  },
}
