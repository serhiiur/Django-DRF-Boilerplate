import multiprocessing  # noqa: INP001
import os

bind = ":8000"

# number of worker processes to handle requests: (2 x $num_cores) + 1
workers = int(os.getenv("GUNICORN_WORKERS", multiprocessing.cpu_count() * 2 + 1))

# type of worker to use for handling requests
worker_class = os.getenv("GUNICORN_WORKER_CLASS", "gevent")

# maximum number of simultaneous clients
worker_connections = int(os.getenv("GUNICORN_WORKER_CONNECTIONS", "1000"))

# how long a worker waits before being forcibly restarted
timeout = int(os.getenv("GUNICORN_TIMEOUT", "30"))

# allows Gunicorn to shut down a worker more gently,
# giving it time to complete any ongoing tasks
graceful_timeout = int(os.getenv("GUNICORN_GRACEFUL_TIMEOUT", "30"))

# allows clients to reuse existing connections instead of opening
# new ones repeatedly
keepalive = int(os.getenv("GUNICORN_KEEPALIVE", "2"))

# ensure that workers don't run indefinitely, forcing them to restart
# after handling 1000 requests
max_requests = int(os.getenv("GUNICORN_MAX_REQUESTS", "1000"))

# ensure randomness, preventing all workers from restarting simultaneously
# and causing temporary downtime
max_requests_jitter = int(os.getenv("GUNICORN_MAX_REQUESTS_JITTER", "50"))
