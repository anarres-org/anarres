# Wiki.js

[Wiki.js](https://wiki.js.org/): A modern, lightweight and powerful wiki app
built on Node.js.

## Variables

* `wikijs_domain`: Domain/subdomain for the service.
* `wikijs_network_name`: Name for the docker network between the service and
  its database.
* `wikijs_docker_image`: (Default: `requarks/wiki`) Name for the local service
  docker image.
* `wikijs_internal_web_port`: (Default: `3060`) Internal port on the host to
   bind the web interface to.
* `wikijs_directory.conf:` Path on the host for configuration files.
* `wikijs_directory.db`: Path on the host for the database data directory.
* `wikijs_db_image`: Mongo Docker image name for the database service.
* `wikijs_db_service_name`: (Default: `wikijs-db`) Name for the database
  service.
* `wikijs_db_name`: (Default: wikijs`) Name for the database for this app.
* `wikijs_db_user`: (Default: `wikijs`) Username for the database and the
  app.
* `wikijs_db_user_pass`: Password for that user.
* `wikijs_enable_ldap`: (Default: `true`) Boolean to enable or disable
  the LDAP logging ability.
* `wikijs_ldap_url`: LDAP server address. Include `ldaps://` at the
  begining and the port at the end. (Example: `ldaps://anarres.local:636`)
* `wikijs_ldap_bind_dn`: Bind DN to use to login to the LDAP server.
* `wikijs_ldap_bind_credentials`: Password for that account.
* `wikijs_ldap_search_base`: Where to find the users for this service of the
   LDAP organization. (Example: `ou=users,dc=anarres,dc=local`)
