# CoreOS Clair

[CoreOS Clair](https://github.com/coreos/clair): Vulnerability Static Analysis
for Containers.

## Variables

* `clair_docker_image`: Name for the service docker image.
* `clair_db_image`: Postgres Docker image name for the database service.
* `clair_internal_ports`: (Default: `6060-6061`) Range of two ports for the
  service. The first one is for the HTTP API and the second one for health
  checks.
* `clair_db_service_name`: (Default: `clair-db`) Name for the database for this app.
* `clair_directory`:
   * `conf`: Path on the host for the configuration directory.
   * `db`: Path on the host for the database data directory.
* `clair_db_name`: (Default: `clair`) Name for the database of this app.
* `clair_db_user`: (Default: `clair`) Username for the database of this app.
* `clair_db_user_pass`: Password for that user.

## Ports

* **6060 tcp** for the HTTP API.
* **6061 tcp** for health checks.
