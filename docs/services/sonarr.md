# Sonarr

[Sonarr](https://github.com/Sonarr/Sonarr) API Support for your favorite
torrent trackers.

## Variables

* `sonarr_docker_image`: Name for the service docker image.
* `sonarr_internal_web_port`: (Default: `8989`) Port on the host to bind the
   service to.
* `sonarr_domain`: Domain/subdomain for the service.
* `sonarr_directory`:
   * `conf`: Path on the host for persistent configurations.
   * `tvseries`: Path on the host of the TV library on disk.
   * `downloadclient`: Path on the host of the download managers output
     directory.

## Setup

1. Deploy the service.
1. Access it through its web interface and set the admin password without
   changing the port.
1. Configure it.

### Troubleshooting

#### Configuring Jackett

* [Reddit](https://www.reddit.com/r/sonarr/comments/936s4n/cant_configure_jackett_in_sonarr/)
