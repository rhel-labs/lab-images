# hostinfo-bootc

RHEL 10 bootc image running the python-hostinfo Flask application as a systemd
service behind nginx. Built from `python-hostinfo` main branch app source — image
builds clone the app at CI time; no app code lives in this directory.

## Architecture

```
nginx (port 80)  →  unix socket  →  gunicorn  →  Flask app
                     /run/flask-app/flask-app.sock
```

The app runs as the `nginx` user via systemd. The venv lives at `/app/venv`.

## Configuration

`config.json` controls which Python and system packages are displayed by the app.
The app checks `/etc/hostinfo/config.json` first, falling back to the baked-in
`/app/config.json` if absent.

This image ships its package list to `/etc/hostinfo/config.json`. Because `/etc`
is preserved across `bootc upgrade`, the config can be edited on a running host
and takes effect after a service restart — no image rebuild required.

To change the default package list shipped with the image, update `config.json`
in this directory and rebuild.

This differs from the container deployment (`hostinfo-app`) where `config.json`
can be overridden at runtime via bind mount to either `/etc/hostinfo/config.json`
or `/app/config.json`.

## Build

CI clones `python-hostinfo` main, copies `app/` into the build context, then builds
with buildah inside a subscribed UBI container. Requires `RHT_ORGID`, `RHT_ACT_KEY`,
`RHT_REG_SVCUSER`, and `RHT_REG_SVCPASS` secrets in the repo.

Published to `ghcr.io/rhel-labs/hostinfo-bootc:latest` on merge to main.
