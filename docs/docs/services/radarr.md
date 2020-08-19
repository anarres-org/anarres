# Radarr

[Radarr](https://github.com/Radarr/Radarr) A fork of Sonarr to work with movies
à la Couchpotato.

## Variables

* `radarr_docker_image`: Name for the service docker image.
* `radarr_internal_web_port`: (Default: `7878`) Port on the host to bind the
   service to.
* `radarr_domain`: Domain/subdomain for the service.
* `radarr_directory`:
   * `conf`: Path on the host for persistent configurations.
   * `movies`: Path on the host of the Movie library on disk.
   * `downloadclient`: Path on the host of the download managers output
     directory.

## Setup

1. Deploy the service.
1. Access it through its web interface and set the admin password without
   changing the port.
1. Configure it.

### Troubleshooting

#### Configuring Jackett

* [Reddit](https://www.reddit.com/r/radarr/comments/936s4n/cant_configure_jackett_in_radarr/)

#### Configuring Transmission as the download client

Since the route where Transmission downloads the files in its container might
not be the same as the mount point of that directory on the Radarr container,
you might have to specify a remote path mapping in the **Download Client** tab
in Radarr's settings such as:

| Host                  | Remote Path     | Local Path  |
| --------------------- | --------------- | ----------- |
| torrent.anarres.local | /data/complete/ | /downloads/ |

#### No root paths on Ombi

If no root paths appear on Ombi when trying to connect it to Radarr, try to
search for a movie on Radarr and add a path by browsing */movies*.

## Reference

* [Setup Guide](https://github.com/Radarr/Radarr/wiki/Setup-Guide)
