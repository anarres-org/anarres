# Jackett

[Jackett](https://github.com/Jackett/Jackett) API Support for your favorite
torrent trackers.

## Variables

* `jackett_docker_image`: Name for the service docker image.
* `jackett_internal_web_port`: (Default: `9117`) Port on the host to bind the
   service to.
* `jackett_domain`: Domain/subdomain for the service.
* `jackett_directory`:
   * `conf`: Path on the host for persistent configurations.

## Setup

1. Deploy the service.
1. Access it through its web interface and set the admin password without
   changing the port.
1. Add trackers.
