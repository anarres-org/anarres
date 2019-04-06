# LDAP configuration

By default, if you deploy the **openldap** and **phpldapadmin** tags to a
server, a basic LDAP scheme will be created:

* **dc=domain,dc=tld**
   * **cn=admin** the LDAP admin user.
   * **cn=readonly** a read only user.
   * **ou=groups** an organizational unit for groups.
      * **cn=users** a group for users.
   * **ou=users** an organizational unit for users.

Now, we can use this structure for PAM login or for services (gitea,
nextcloud..) for example. This is convenient because once we register a user,
that user will be able to login using the same credentials for all the services
(that authenticate against LDAP).

## phpLDAPadmin

It's a web interface for our LDAP server. Here you can register, modify and
delete users.

Register the user with the email attribute, because some services will need it.
If you are planning to use this users for PAM login (linux login), add them to
the users group, so they have the same **gid**.

## Services

To setup services to authenticate against our LDAP server, we'll have to
configure them with the following parameters:

* Authentication Type: LDAP via BindDN
* Security protocol: LDAPS
* Host: our openLDAP IP or domain/subdomain
* Port: `636`
* Bind DN: `cn=readonly,dc=anarres,dc=local`
* Bind password: the value of *openldap_readonly_password*.
* User search base: `ou=users,dc=anarres,dc=local`
* User filter: `(&(objectClass=posixAccount)(|(uid=%[1]s)(mail=%[1]s)))`
* Email Attribute: `mail`

Optionally, we can also add:

* Admin filter: `(&(uid=admin))` or whatever the admin's uid is.
* First Name Attribute: `givenName`
* Surname Attribute: `sn`

### Configuration guides

* [gitea](https://docs.gitea.io/en-us/authentication/)
* [nextcloud](https://docs.nextcloud.com/server/14/admin_manual/configuration_user/user_auth_ldap.html)
