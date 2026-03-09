## About

Production-ready Django + Django REST Framework boilerplate focused on fast API bootstrapping, predictable environment-based configuration, and container-first deployment.


## Features
- Environment-based settings (*development*, *stage*, *production*, *test*) according to the [Django Styleguide](https://github.com/HackSoftware/Django-Styleguide?tab=readme-ov-file#settings)
- Environment-based deployment using Docker Compose [profiles](https://docs.docker.com/reference/compose-file/profiles/)
- Integration with Nginx for reverse proxying and static file serving
- Integration with Redis using [django-redis](https://github.com/jazzband/django-redis) package for caching
- Integration with PostgreSQL using [psycopg](https://github.com/psycopg/psycopg) adapter
- Integration with [uv](https://github.com/astral-sh/uv) for dependency management
- Integration with [ruff](https://github.com/astral-sh/ruff) and [mypy](https://github.com/python/mypy) for linting and type checking
- Integration with [django-debug-toolbar](https://github.com/django-commons/django-debug-toolbar), [django-silk](https://github.com/jazzband/django-silk) and [django-extensions](https://github.com/django-extensions/django-extensions) for smooth development experience
- Integration with [drf-spectacular](https://github.com/tfranzel/drf-spectacular) for OpenAPI schema generation and interactive API docs
- Integration with [django-unfold](https://github.com/unfoldadmin/django-unfold) for a modernized admin UI
- Integration with [Gunicorn](https://github.com/benoitc/gunicorn) for production-ready WSGI server
- Integration with [Python-Json-Logger](https://github.com/madzak/python-json-logger) for structured logging in JSON format
- Integration with [Faker](https://github.com/joke2k/faker) to ensure random data generation for testing
- Basic CI pipeline using on Github Actions
- Basic logging configuration with console and file handlers
- Custom `User` model


## Requirements

- Python: *>=3.12*
- Package/dependency manager: *uv*
- Container runtime (optional): Docker + Docker Compose


## Settings and configuration

Configuration of the entire stack is primarily based on the environment variables. The right way would be to declare them in the <ins>./config/.env</ins> file that can be generated from the template [template](./config/.env.example) like that:

```bash
cp ./config/.env.example ./config/.env
```

Once the <ins>./config/.env</ins> file is created, you can adjust the values of the variables as needed. Some parameters have default values, so you can omit them from the file if the defaults work for you.


### Key variables

| Variable | Default | Description |
| --- | --- | --- |
| DJANGO_SETTINGS_MODULE | `main.django.development` | Active settings module |
| DJANGO_SECRET_KEY | statically set random string | Django secret key |
| DJANGO_DEBUG | `1` | Whether to enable Django debug mode or not |
| DJANGO_ALLOWED_HOSTS | `['localhost', '127.0.0.1']` | Extra allowed hosts list |
| DJANGO_ADMIN_EMAIL | `admin@example.com` | Default email for Django admin UI |
| DJANGO_ADMIN_USERNAME | `admin` | Default username for Django admin UI |
| DJANGO_ADMIN_PASSWORD | randomly generated at runtime if missing | Default password for Django admin UI |
| DJANGO_LOG_LEVEL | `INFO` | Global log level |
| DJANGO_ADMIN_UI_TITLE | `Django Admin Title` | Admin UI title |
| DJANGO_ADMIN_UI_HEADER | `Django Admin Header` | Admin UI header |
| POSTGRES_USER | `django` | Database username |
| POSTGRES_PASSWORD | `django` | Database password |
| POSTGRES_DB | `django` | Database name |
| DATABASE_URL | `sqlite:///db.sqlite3` | Database connection URL |
| REDIS_PASSWORD | - | Password for Redis |
| CACHE_URL | `http://localhost:6379` | Cache connection URL |
| OPENAPI_TITLE | `Django Boilerplate` | title of the application for OpenAPI documentation |
| OPENAPI_DESCRIPTION | `Django Boilerplate Application` | description of the application for OpenAPI documentation |
| OPENAPI_VERSION | `0.5.0` | Version of the application for OpenAPI documentation |
| GUNICORN_WORKERS | *(2 x $num_cores) + 1* | Number of worker processes |
| GUNICORN_WORKER_CLASS | `gevent` | Worker class type |
| GUNICORN_WORKER_CONNECTIONS | `1000` | Maximum number of simultaneous clients |
| GUNICORN_TIMEOUT | `30` | Worker timeout in seconds |
| GUNICORN_GRACEFUL_TIMEOUT | `30` | Timeout for graceful workers restart in seconds |
| GUNICORN_KEEPALIVE | `2` | Keep-alive duration in seconds |
| GUNICORN_MAX_REQUESTS | `1000` | Maximum number of requests a worker will process before restarting |
| GUNICORN_MAX_REQUESTS_JITTER | `50` | Maximum jitter for the max requests setting |


#### Notes:

- by default the application is running in the **development** environment. To switch to another environment, change the value of `DJANGO_SETTINGS_MODULE` accordingly (e.g. `main.django.production` for production mode);

- `GUNICORN_WORKERS` is explicitly set to 1 for `backend-dev` service in [docker-compose.yml](docker-compose.yml) file to prevent multi-workers issue with the *Django Debug Toolbar* and *Django Silk* profiler;

- once the application is running, make sure to change the default admin credentials using *Django Admin UI*.


## Installation
Step 1: clone the repository and navigate to the project directory:

```bash
git clone git@github.com:serhiiur/Django-DRF-Boilerplate.git
cd Django-DRF-Boilerplate/
```

Step 2: install dependencies using *uv*:

```bash
uv sync --all-groups
```

Step 3: set up the configuration by creating a `.env` file and adjust values as needed:

```bash
cp ./config/.env.example ./config/.env
```

Step 4: create a new Django app and add it to the `INSTALLED_APPS` list in the settings [module](src/main/django/base.py):

```bash
uv run src/manage.py startapp myapp src/myapp/
```

At this point you can run the application locally or using Docker Compose.


## Running
For running the application locally, you need to apply the database migrations, run the script to create a superuser, and then start the development server. For example:

```bash
uv run src/manage.py migrate
uv run src/manage.py createsu
uv run src/manage.py runserver
```

**Note**: [createsu](src/core/management/commands/createsu.py) is a custom management command that creates a superuser with the credentials specified in the environment variables (`DJANGO_ADMIN_USERNAME`, `DJANGO_ADMIN_EMAIL`, `DJANGO_ADMIN_PASSWORD`). If the password variable is not set, it will generate a random password and print it in the console.

Then Navigate to `http://localhost:8000` to access the application in your browser.

When using Docker Compose, everything will be provisioned and set up for you, so you can just run the appropriate command for the specified profile (see below) and access the app at `http://localhost`.

There are 3 profiles available:
- `dev` for development (with debug toolbar, silk profiler, django_extensions package, etc.)
- `prod` for production-like environment
- `stage` for stage-like environment (same as prod but with different environment variables, e.g. `BACKEND_HOSTNAME`)

Example of running the application in production mode:

```bash
docker compose --env-file ./config/.env --profile prod up --build 
```

If there's a need to build the backend or Nginx service image (e.g. after making changes to the Dockerfile), you can do it with the following command:

```bash
docker compose build backend-prod
```


## Usage

After running the application, you can access the following endpoints:
- `/` - index HTML page
- `/admin/` - Django admin UI
- `/api/schema/` - OpenAPI schema (JSON)
- `/api/schema/docs/` - interactive API docs (Swagger UI)
- `/api/schema/redoc/` - interactive API docs (Redoc)
- `/version/` - exposed API version (defined by `OPENAPI_VERSION` environment variable)
- `/silk/` - Django Silk profiler UI (only in development mode)

**Tip**: use the admin credentials defined in the <ins>.env</ins> file to log in to the Django admin UI.


## References

- [Django](https://github.com/django/django)
- [Django REST Framework](https://github.com/encode/django-rest-framework)
- [Django Styleguide](https://github.com/HackSoftware/Django-Styleguide?tab=readme-ov-file#settings)
- [Gunicorn Settings](https://gunicorn.org/reference/settings/)
