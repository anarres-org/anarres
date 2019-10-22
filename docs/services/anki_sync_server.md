# Anki sync server

[Anki sync server](https://github.com/tsudoko/anki-sync-server) This is a
personal Anki server, which you can sync against instead of AnkiWeb.

## Variables

* `anki_docker_image`: Name for the service docker image.
* `anki_domain`: Domain/subdomain for the service.
* `anki_internal_web_port`: (Default: `27701`) Port on the host to bind the
   service to.
* `anki_directory`:
   * `data`: Path on the host for persistent data.
