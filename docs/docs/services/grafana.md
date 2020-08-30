# Grafana

[Grafana](https://grafana.com/): The open platform for beautiful
analytics and monitoring.

## Variables

* `grafana_docker_image`: Name for the service docker image.
* `grafana_domain`: Domain/subdomain for the service.
* `grafana_image_renderer_docker_image`: (Default:
   `grafana/grafana-image-renderer:latest`) Name of the Docker image for the
   Grafana external image rendering.
* `grafana_directory`:
   * `conf`: Path on the host for persistent configurations.
   * `data`: Path on the host for persistent data.
* `grafana_internal_web_port`: (Default: `3070`) Port on the host to bind the service to.
* `grafana_admin_user`: Username for the admin user.
* `grafana_admin_password`: Password for the admin user.
* `grafana_allow_sign_up`: (Default `"false"`) Boolean ("true" or "false") to allow sign up.
