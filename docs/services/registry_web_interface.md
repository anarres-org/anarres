# Registry web interface

[Jessfraz Docker registry web interface](https://github.com/genuinetools/reg):
Docker registry v2 command line client and repo listing generator with security
checks.

## Variables

* `registry_web_interface_domain`: Domain/subdomain for the service.
* `registry_web_interface_docker_image`: Name for the service docker image.
* `registry_web_interface_internal_web_port`: (Default: `4080`) Port on the host to bind the service to.
* `registry_web_interface_registry_url`: URL of the Docker registry.
* `registry_web_interface_registry_user`: Username for HTTP auth of the Docker
  registry.
* `registry_web_interface_registry_pass`: Password for that user.
