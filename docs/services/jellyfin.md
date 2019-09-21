# Jellyfin

[Jellyfin](https://jellyfin.media/) The Free Software Media System.

## Variables

* `jellyfin_docker_image`: Domain/subdomain for the service.
* `jellyfin_domain`: Domain/subdomain for the service.
* `jellyfin_internal_web_port`: (Default: `8096`) Port on the host to bind the
   service to.
* `jellyfin_directory`:
   * `cache`: Path on the host for persistent cache.
   * `config`: Path on the host for persistent configurations.
   * `media`: Path on the host to get the media from..
