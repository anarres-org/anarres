# Ombi

[Ombi](https://github.com/tidusjar/Ombi) Want a Movie or TV Show on Plex or
Emby? Use Ombi!

## Variables

* `ombi_docker_image`: Name for the service docker image.
* `ombi_internal_web_port`: (Default: `3579`) Port on the host to bind the
   service to.
* `ombi_domain`: Domain/subdomain for the service.
* `ombi_directory`:
   * `conf`: Path on the host for persistent configurations.

## Setup

1. Deploy the service.
1. Access it through its web interface and set the admin password without
   changing the port.

### Troubleshooting

#### Jellyfin connection

* [Issue](https://github.com/tidusjar/Ombi/issues/3245#issuecomment-573049587)
