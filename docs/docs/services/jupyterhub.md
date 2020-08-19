# JupyterHub

[JupyterHub](https://jupyter.org/hub) A multi-user version of the notebook
designed for companies, classrooms and research labs.

## Variables

* `jupyterhub_docker_image`: Name for the service docker image.
* `jupyterhub_internal_web_port`: (Default: `8000`) Port on the host to bind the
   service to.
* `jupyterhub_domain`: Domain/subdomain for the service.
* `jupyterhub_directory`:
   * `data`: Path on the host for persistent data.
   * `user_data`: Path on the host for persistent user data.
* `jupyterhub_jupyter_docker_image`: Docker image to be spawned for the users.
* `jupyterhub_admin_users`: List of usernames that are admins of JupyterHub.
* `jupyterhub_user_container_mem_limit`: (Default: `2G`) Memoery limit for the
   spawned containers.
* `jupyterhub_nvidia_runtime`: Boolean value to enable nvidia runtime support
  for the spawned containers.
* `jupyterhub_ldap_hostname`: LDAP server hostname or IP.
* `jupyterhub_ldap_bind_dn`: Bind DN to use to login to the LDAP server.
* `jupyterhub_ldap_bind_credentials`: Password for that account.
* `jupyterhub_ldap_search_base`: Where to find the users for this service of the
   LDAP organization. (Example: `ou=users,dc=anarres,dc=local`)
* `jupyterhub_ldap_user_attribute`: (Default: `uid`) The LDAP field which is used
   in the login.
* `jupyterhub_ldap_user_dn_attribute`: (Default: `cn`) The LDAP field which is
   used for binding against the LDAP.
* `jupyterhub_bind_dn_template`: Template used to generate the full dn for a user
   from the human readable username.

## Reference

* [ldapauthenticator](https://github.com/jupyterhub/ldapauthenticator/)
