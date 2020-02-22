# Drone

Needs Gitea to be deployed. Authenticates against the Gitea itself.

In order to deploy Drone against Gitea, you must set up some variables. Follow the next steps:

### Create an OAuth Application

Create a Gitea OAuth application. The Consumer Key and Consumer Secret are used to authorize access to Gitea resources.

The authorization callback URL must match the below format and path, and must use your exact server scheme and host.

![](https://docs.drone.io/screenshots/gitea_application_create.png)

![](https://docs.drone.io/screenshots/gitea_application_created.png)


Copy the content of *Client ID* field on `gitea_oauth_client_id` variable.

Copy the content of *Client Secret* field on `gitea_oauth_client_secret` variable.

### Create a Shared Secret

Create a shared secret to authenticate communication between runners and your central Drone server.

You can use openssl to generate a shared secret:

```
$ openssl rand -hex 16
bea26a2221fd8090ea38720fc445eca6
```
The output of this command is the content of the variable `drone_rpc_scret`

### Deploy Drone with Anarres

```
$ ansible-playbook --ask-vault-pass -i custom/KLK/hosts.yml --tags "drone" full.yml
```
