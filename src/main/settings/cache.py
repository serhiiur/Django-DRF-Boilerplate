from main.env import env

CACHES = {
  "default": {
    **env.cache(
      default="redis://localhost:6379",
      backend="django_redis.cache.RedisCache",
    ),
    "OPTIONS": {
      "CLIENT_CLASS": "django_redis.client.DefaultClient",
    },
  },
}
