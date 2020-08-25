# ShareLatex

[ShareLatex](https://github.com/overleaf/overleaf) A web-based collaborative
LaTeX editor.

## Variables

* `sharelatex_docker_image`: Name for the service docker image.
* `sharelatex_internal_web_port`: (Default: `3080`) Port on the host to bind the
   service to.
* `sharelatex_domain`: Domain/subdomain for the service.
* `sharelatex_network_name`: (Default: `sharelatex`) Name for the Docker
  network for the service and its required containers.
* `sharelatex_app_name`: (Default: `ShareLatex`) App name for the website.
* `sharelatex_directory_www_data`:
   * `data`: Path on the host for persistent data.
* `sharelatex_directory`:
   * `db`: Path on the host for the database data directory.
   * `redis`: Path on the host for persistent redis files.

### DB

* `sharelatex_db_image`: Mongo Docker image name for the database service.
* `sharelatex_db_service_name`: (Default: `sharelatex-db`) Name for the
   database service.
* `sharelatex_db_user`: (Default: `sharelatex`) Username for the database and
   the app.
* `sharelatex_db_user_pass`: Password for that user.
* `sharelatex_db_name`: (Default: `sharelatex`) Name for the database for this
   app.

### Redis

* `sharelatex_redis_image`: Redis Docker image name.

## LDAP support

Unfortunately, LDAP is not supported in the community version.

## Setup

1. Deploy the service.
1. Optionally, install all of TeXLive packages with:
   ```bash
   docker exec sharelatex tlmgr install scheme-full
   ```

   Alternatively you can install packages manually as you need by replacing
   `scheme-full` with the package name.
1. Create the admin user account by visiting `/launchpad` on the site or use
   the following command:
   ```bash
   docker exec sharelatex /bin/bash -c "cd /var/www/sharelatex; grunt user:create-admin --email=joe@example.com"

   ```

Once this is done, regular users can be created from `/admin/register`.

## Reference

* [Quick Start Guide · overleaf/overleaf Wiki](https://github.com/overleaf/overleaf/wiki/Quick-Start-Guide)
