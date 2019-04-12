# CodiMD

Realtime collaborative markdown notes on all platforms. Like
[HackMD](https://hackmd.io/). Based on
[CodiMD](https://github.com/hackmdio/codimd).

## Variables

```yaml
* **`codimd_docker_image`**: (Default: `hackmdio/hackmd:1-alpine`) Docker image
   name for the service.
* **`codimd_domain`**: Domain/subdomain for the service.
* **`codimd_web_port`**: Internal port on the host to bind the web interface
  to.
* **`codimd_network_name`**: (Default: `codimd`) Name of the doker network for
  the service and its database.
* **`codimd_directory.db`**: Path on the host for the database data directory.
* **`codimd_directory.uploads`**: Path on the host for the image uploads
  directory.
* **`codimd_db_image`**: Postgres Docker image name for the database service.
* **`codimd_db_service_name`**: (Default: `codimd-db`) Name for the database
  service.
* **`codimd_db_user`**: (Default: `codimd`) Username for the database and the
  app.
* **`codimd_db_user_pass`**: Password for that user.
* **`codimd_db_name`**: (Default: codimd`) Name for the database for this app.
* **`codimd_enable_ldap`**: (Default: `true`) Boolean to enable or disable
  the LDAP logging ability.
* **`codimd_ldap_url`**: LDAP server address. Include `ldaps://` at the
  begining and `:[port]` at the end. (Example: `ldaps://anarres.local:636`)
* **`codimd_ldap_binddn`**: Bind DN to use to login to the LDAP server.
* **`codimd_ldap_bindcredentials`**: Password for that account.
* **`codimd_ldap_searchbase`**: Where to find the users for this service of the
   LDAP organization. (Example: `ou=users,dc=anarres,dc=local`)
* **`codimd_ldap_searchfilter`**: (Default:`(uid={{username}})`) LDAP filter to
  verify the users's identification.
* **`codimd_ldap_searchattributes`**: (Default: `uid, mail`) Attributes to
  search with the LDAP query.
* **`codimd_ldap_userfield`**: (Default: `uid`) The LDAP field which is used
   uniquely identify a user on CodiMD.
* **`codimd_ldap_usernamefield`**: (Default: `uid`) The LDAP field which is
   used as the username on CodiMD.
```
