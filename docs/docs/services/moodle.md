# Moodle

[Moodle](https://moodle.org/) Open-source learning plataform.

## Variables

* `moodle_docker_image`: Name for the service docker image.
* `moodle_domain`: Domain/subdomain for the service.
* `moodle_internal_web_port`: (Default: `8082`) Port on the host to bind the
   service to.
* `moodle_git_repo`: (Default: `git://git.moodle.org/moodle.git`) Git repo to
  get Moodle from.
* `moodle_git_repo_version`: (Default: `MOODLE_37_STABLE`) Release tag from the
  Moodle git repo.
* `moodle_db_image`: Postgres Docker image name for the database service.
* `moodle_db_name:` (Default: `moodle`) Name for the database for this app.
* `moodle_db_user`: (Default: `moodle`) Username for the database and the
  app.
* `moodle_db_user_pass`: Password for that user.
* `moodle_directory`:
   * `data`: Path on the host for persistent data.
   * `db`: Path on the host for persistent database data.
   * `html`: Path on the host for persistent html data.

## Setup

You must access the Moodle domain to configure it manually for the first time.
The database host is `moodle-db` and uses the default Postgres port (5432).
