# WebCounter

A minimal Python WSGI web application that counts page views in a valkey data store.
Written as the two-container application for the Podman pods lab: a web frontend and
a data store that need to communicate.

## Configuration

- `STORE_HOST` — the host the store is reachable at. Defaults to `localhost`, the
  frontend's own container.

## Running with Podman

Run the store and the frontend on a user-defined network:

```bash
podman network create app-net
podman run -d --rm --name store --network app-net registry.access.redhat.com/hi/valkey:latest
podman run -d --rm --name web -p 8000:8000 --network app-net -e STORE_HOST=store webcounter-app
```

Then open `http://localhost:8000`.

## Behavior

- `GET /` increments the `hits` counter in the store and renders
  `Page views: N, served from store at <STORE_HOST>:6379`.
- If the store is unreachable, the page renders
  `Page views: —, store unreachable at <STORE_HOST>:6379` with HTTP 200.
- At startup the frontend pings the store and logs `store reached at <addr>` or
  `[store unreachable] <error>` to stdout.
