# Anarres Full Playbook

An [ansible](https://github.com/ansible) playbook to set up a GNU/Linux server.
Services in [docker](https://www.docker.com/). Security by default.

## Compatibility

These are the tested GNU/Linux distributions. Maybe it works on some other
distributions too or just requieres a few changes.

* [debian](https://www.debian.org/)
  * stretch

## Requirements

`sudo` and `python`.

## Playbook Variables

## Dependencies

Included as submodules in *roles/*.

* [iptables_raw](https://github.com/Nordeus/ansible_iptables_raw)
* [anarres-common](https://github.com/anarres-org/anarres-common)
* [anarres-sec](https://github.com/anarres-org/anarres-sec)
* [letsencrypt-request](https://github.com/anarres-org/letsencrypt-request)
* [anarres-nginx](https://github.com/anarres-org/anarres-nginx)
* [generic_docker_systemd](https://github.com/anarres-org/generic_docker_systemd)
* [add_nginx_proxy_conf](https://github.com/anarres-org/add_nginx_proxy_conf)

## Setup

1. Install `sudo` and `python`.
1. Login as **root** and add your **user** to *sudoers* or to the **sudo**
   group with `usermod -a -G sudo [user]`.

The idea is that you run the playbooks with the tags of the services that you
want to setup. But, there are some steps that "must" be run first, before
deploying the actual services.

An example approach would be:

1. Deploy the basic stuff (dependencies, directory creation, security...):
   `-t init,common,sec`
1. If everything goes well, deploy the base web server: `-t web`
1. Now you are ready to deploy the desired services, for example gitea: `-t
   gitea`

### Tips

* You can check the available tags with:

   ```bash
   ansible-playbook --list-tags full.yml
   ```

* You can create a *custom/* folder in the playbook root directory. There you
  can save your inventory files with your chosen variables for each host. This
  folder will be ignored thanks to the *.gitignore* configuration.
* As some of the variables are passwords, you can encrypt them with
  [ansible-vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html)
* Before deploying anything, check the variables and their default values from
  *group_vars/all.yml*. Copy and change the required ones to your custom
  inventory file.
* Deploy only a few tags with:

   ```bash
   ansible-playbook -i custom/[project]/hosts.yml full.yml --extra-vars
   ansible_become_pass="[sudo_password]" --ask-vault-pass -t gitea
   ```

### Firewall

If you are behind some kind of firewall or you need to setup NAT, you should
add the following ports:

* **80** for HTTP connections, used for the `letsencrypt` verification
* **443** for HTTPs connections, used by the reverse proxy to serve access to
  the web services.
* The SSH port you choose, or **2222** by default.
* All the desired ports that some services have.

### Services

Their data and configuration files will be stored in your hosts `data_path`
directory, by default */data*.

* [Gitea](https://docs.gitea.io/): based on
  [gitea/gitea](https://github.com/go-gitea/gitea).

For more info about each service and how to set it up, go to
[docs/services](docs/services).

#### Letsencrypt

The main domain cert needs to be obtained using the **standalone** method since
we don't have a working webserver by this point (the server needs the cert). So
the webroot path will be empty in */etc/letsencrypt/renewal/{{ base_domain
}}.conf*. You should manually specify it adding:

```
authenticator = webroot
webroot_path = /var/www/letsencrypt,
```

#### Nextcloud

First user to register will be the admin user.

### NFS

Please refer to [ubunut-help](https://help.ubuntu.com/community/NFSv4Howto) to
see how NFSv4 works. Make sure to mount the directories you want to export
inside the */export* folder of the NFS container. Mount them with the `:ro`
option if you want them to be read-only (and configure them in the **exports**
conf accordingly).

*Ports*: **2049/tcp**.

#### OpenLDAP

An OpenLDAP server for the internal services.

*Ports*: **636/tcp**.

#### phpLDAPadmin

A web interface for managing OpenLDAP.

#### BIND DNS server

You need to specify the user with the `uid` **101** if it isn't
**systemd-network**. Check it in */etc/passwd*.

Refer to [ubuntu-help](https://help.ubuntu.com/community/BIND9ServerHowto) to
see how to configure it.

*Ports*: **53/tcp** and **53/udp**.

## Backup

Make sure to backup your `data_path` (by default */data*) and the docker
volumes (used by the databases) from */var/lib/docker/volumes*.

## License

GPLv3

## Author Information

m0wer: m0wer (at) autistici.org
