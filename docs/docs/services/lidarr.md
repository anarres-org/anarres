# Lidarr

[Lidarr](https://github.com/lidarr/Lidarr) Looks and smells like Sonarr but
made for music.

## Variables

* `lidarr_docker_image`: Name for the service docker image.
* `lidarr_internal_web_port`: (Default: `8686`) Port on the host to bind the
   service to.
* `lidarr_domain`: Domain/subdomain for the service.
* `lidarr_directory`:
   * `conf`: Path on the host for persistent configurations.
   * `music`: Path on the host of the Music library on disk.
   * `downloadclient`: Path on the host of the download managers output
     directory.

## Setup

1. Deploy the service.
1. Access it through its web interface and set the admin password without
   changing the port.
1. Configure it.

### Troubleshooting

#### Configuring Jackett

* [Reddit](https://www.reddit.com/r/lidarr/comments/936s4n/cant_configure_jackett_in_lidarr/)

#### Configuring Transmission as the download client

Since the route where Transmission downloads the files in its container might
not be the same as the mount point of that directory on the Lidarr container,
you might have to specify a remote path mapping in the **Download Client** tab
in Lidarr's settings such as:

| Host                  | Remote Path     | Local Path  |
| --------------------- | --------------- | ----------- |
| torrent.anarres.local | /data/complete/ | /downloads/ |

#### No root paths on Ombi

If no root paths appear on Ombi when trying to connect it to Lidarr, add them
on Lidarr > Settings > Media Management > Root Folders.
