# Registry

[Docker Registry](https://docs.docker.com/registry/): A stateless, highly scalable server side application that stores and lets you distribute Docker images.

## Variables

* `registry_domain`: Domain/subdomain for the service.
* `registry_docker_image`: Name for the service docker image.
* `registry_directory`:
   * `data`: Path on the host for persistent data.
* `registry_internal_web_port`: (Default: `5000`) Port on the host to bind the service to.
* `registry_user`: Username for HTTP auth.
* `registry_pass`: Password for that user.
