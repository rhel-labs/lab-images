import os

import redis

STORE_HOST = os.environ.get("STORE_HOST", "localhost")
STORE_PORT = 6379

PAGE = """<!DOCTYPE html>
<html>
<head><title>WebCounter</title></head>
<body>
<h1>WebCounter</h1>
<p>{line}</p>
</body>
</html>"""


def connect():
    return redis.Redis(host=STORE_HOST, port=STORE_PORT, socket_connect_timeout=2)


def ping_store():
    try:
        connect().ping()
        print(f"store reached at {STORE_HOST}:{STORE_PORT}", flush=True)
    except Exception as err:
        print(f"[store unreachable] {err}", flush=True)


ping_store()


def app(environ, start_response):
    try:
        views = connect().incr("hits")
        line = f"Page views: {views}, served from store at {STORE_HOST}:{STORE_PORT}"
    except Exception:
        line = f"Page views: —, store unreachable at {STORE_HOST}:{STORE_PORT}"
    start_response("200 OK", [("Content-Type", "text/html")])
    return [PAGE.format(line=line).encode()]
