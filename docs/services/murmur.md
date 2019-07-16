# Murmur

[Murmur](https://wiki.mumble.info/wiki/Main_Page): Open source, low-latency,
high quality voice chat software.

## Variables

* `murmur_docker_image`: Name for the service docker image.
* `murmur_domain`: Domain/subdomain for the service.
* `murmur_port`: (Default: `64738`) Port on the host to bind the service to.
* `murmur_directory`:
   * `conf`: Path on the host for configuration files.
   * `data`: Path on the host for persistent data.
   * `log`: Path on the host for logss.

## Ports (by default)

* **64738/tcp** for the client connections.
