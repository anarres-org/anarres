# RStudio

[RStudio](https://www.rstudio.com/) provides popular open source and
enterprise-ready professional software for the R statistical computing
environment.

## Variables

* `rstudio_domain`: Domain/subdomain for the service.
* `rstudio_docker_image`: Name for the service docker image.
* `rstudio_user`: (Default: `rstudio`) Default user for the web service.
* `rstudio_pass`: Password for that user.
* `rstudio_directory`:
   * `data`: Path on the host for persistent data.
* `rstudio_cpus_limit`: (Default: `2`) Limit of the CPUs used by the container.
* `rstudio_memory_limit`: (Default: `3gb`) Limit of the memory available to the
  container.
* `rstudio_internal_web_port`: (Default: `8787`) Port on the host to bind the
   service to.
