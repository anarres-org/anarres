# Bazarr

[Bazarr](https://github.com/morpheus65535/bazarr) is a companion application to
Sonarr and Radarr. It manages and downloads subtitles based on your requirements.

## Variables

* `bazarr_docker_image`: Name for the service docker image.
* `bazarr_internal_web_port`: (Default: `7878`) Port on the host to bind the
   service to.
* `bazarr_domain`: Domain/subdomain for the service.
* `bazarr_directory`:
   * `conf`: Path on the host for persistent configurations.
   * `movies`: Path on the host of the Movie library on disk.
   * `tv`: Path on the host of the TV library on disk.

## Setup

1. Deploy the service.
1. Access it through its web interface and set the admin password without
   changing the port.
1. Configure it.

## Reference

* [Setup Guide](https://github.com/morpheus65535/bazarr/wiki/Wizard-General)
