# Portainer

[Portainer](https://www.portainer.io/) Making Docker management easy.

## Variables

* `portainer_docker_image`: Name for the service docker image.
* `portainer_domain`: Domain/subdomain for the service.
* `portainer_internal_web_port`: (Default: `3060`) Port on the host to bind the
   service to.
* `portainer_directory`:
   * `data`: Path on the host for persistent data.
