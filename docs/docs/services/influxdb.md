# InfluxDB

[InfluxDB](https://www.influxdata.com/): Scalable datastore for metrics,
events, and real-time analytics.

## Variables

* `influxdb_docker_image`: Name for the service docker image.
* `influxdb_directory`:
   * `data`: Path on the host for persistent data.
* `influxdb_port`: (Default: `8086`) Port on the host to bind the service to.
* `influxdb_open_port`: Boolean value to open `influxdb_port` in the firewall.
* `influxdb_db`: Name of the database to create.
* `influxdb_admin_user`: Username for the admin user.
* `influxdb_admin_password`: Password for the admin user.
* `influxdb_user`: Username for the unprivileged user (with access to
  `influxdb_db`).
* `influxdb_user_password`: Password for that user.

## Ports

If `influxdb_open_port` is set to `true`, the `influxdb_port` will be accesible
from outside the server.
