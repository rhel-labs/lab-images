# Host Details Viewer

A simple Python Flask web application to display live host details like OS information, kernel version, and versions of configured Python and system packages.
Can show container or host details if appropriate mounts are added at runtime.

## Running with Podman

1.  **Run the Container**:
    ```bash
    podman run -d -p 8080:8000 --name my-host-details-instance host-details-app
    ```
    *(Optional) To enable the **Host View** feature in the container, mount the read-only paths relevant to your OS (e.g. omit dpkg on Fedora) and pass the hostname environment variable:*
    ```bash
    podman run -d -p 8080:8000 --name my-host-details-instance \
      -e HOST_HOSTNAME=$(hostname) \
      -v /usr/lib/os-release:/host/os-release:ro \
      -v /var/lib/rpm:/host/var/lib/rpm:ro \
      -v /usr/lib:/host/usr/lib:ro \
      host-details-app
    ```
2.  **Access**: Open `http://localhost:8080` in your browser.

---

## App info

This is copied from the [python-hostinfo](https://github.com/rhel-labs/python-hostinfo) repo as a point in time for lab use as a containerized application example.


