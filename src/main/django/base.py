from pathlib import Path

from main.env import env

BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = [
  "localhost",
  "127.0.0.1",
  *env.list("DJANGO_ALLOWED_HOSTS", default=[]),
]
DEBUG = env.bool("DJANGO_DEBUG", default=True)
SECRET_KEY = env.str(
  "DJANGO_SECRET_KEY",
  default="qGb8aeJj3aG8_JT1JCFtborb1l-Sg1JDhiZsqeLk2fo",
)

INSTALLED_APPS = [
  "unfold",
  "unfold.contrib.filters",
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",
  "rest_framework",
  "drf_spectacular",
  "core",
]

MIDDLEWARE = [
  "django.middleware.security.SecurityMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
  {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [],
    "APP_DIRS": True,
    "OPTIONS": {
      "context_processors": [
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
      ],
    },
  },
]

WSGI_APPLICATION = "main.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
  {
    "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
  },
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

AUTH_USER_MODEL = "core.User"

from main.settings.cache import *
from main.settings.custom import *
from main.settings.db import *
from main.settings.drf import *
from main.settings.logging import *
from main.settings.unfold import *
