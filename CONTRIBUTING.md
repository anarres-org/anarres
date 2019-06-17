# Contributing

Forks and pull request is the preferred method. Issues are welcome too.

If you are going to collaborate, check:

* [docs/testing](https://github.com/anarres-org/anarres/blob/master/docs/testing.md)

## Decisions

### General

* One service per role (except for **common** and **sec**).
* Use variables.

### Variables

#### **group_vars/all.yml**

Default variables and empty placeholders for variables that always need to be
set by the user.

#### **custom/project_name/hosts.yml**

This is the inventory file for an specific server or group of servers, it's not
part of the code (custom/ is ignored by git) and it contains the variables for
an specific deploy.

### Services

* Own database for each.
* Use a external database whenever possible (performance and scaling).
* Own network for the service dockers and the database.

#### Networking

* Web services should bind a host port for the reverse proxy (`nginx-light`) to
   connect to.
   This port shouldn't be open in the firewall. Only local connections.
   Example: `gitea` binds the host port **3000** for its web interface.
* Other services should directly bind the host port.
   Example: `gitea` directly binds the host port **22** for SSH connections.

### Style

* Break things up, ansible module parameters in new lines.
* Single quotes for strings, double quotes for variables.
* YAMLlint, ansible LINT... Check it with `molecule lint`.

## New feature

Modify:

* **full.yml**: Add the functionality.
* **group_vars/all.yml**: Set the variables.
* **molecule/default/molecule.yml**: set the variables for testing.
* **molecule/default/tests/test_default.py**: Add the tests for the new
  service.
* **docs/services/service_name.yml**: Add a description and the service
  variables.
* **README.md**: Add the service to the services list.

### New role

#### Create a new role

Requirements:

* README.md about the role.
* Tests.

Tasks:

* Add the role as a git submodule in *roles/*.
* Use the new role in the playbook.
* Add the new role name, source and description to *README.md*.
