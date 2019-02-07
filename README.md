# Anarres Full Playbook

## Compatibility

These are the tested GNU/Linux distributions. Maybe it works on some other
distributions too or just requieres a few changes.

* [debian](https://www.debian.org/)
  * stretch

## Requirements

`sudo` and `python`.

## Playbook Variables

## Dependencies

* [iptables_raw](https://github.com/Nordeus/ansible_iptables_raw)
* [anarres-common]
* [anarres-sec]
* [letsencrypt-request]
* [anarres-nginx]
* [generic_docker_systemd]
* [add_nginx_proxy_conf]

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
   ansible-playbook -i custom/[project]/hosts.yml full.yml --extra-vars ansible_become_pass="[sudo_password]" --ask-vault-pass -t gitea
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

#### Letsencrypt

The main domain cert needs to be obtained using the **standalone** method since
we don't have a working webserver by this point (the server needs the cert). So
the webroot path will be empty in */etc/letsencrypt/renewal/{{ base_domain
}}.conf*. You should manually specify it adding:

```
authenticator = webroot
webroot_path = /var/www/letsencrypt,
```

#### Gitea

First user to register will be the admin user.

*Ports*: **22/tcp** for SSH.

#### OpenVPN

Once installed, from the server's command line.

*Ports*: **1194/udp**.

##### Genereate new user keys

`docker exec -it openvpn easyrsa build-client-full [USERNAME] nopass`

##### Get the configuration file for an existing user

`docker exec -it openvpn ovpn_getclient [USERNAME] > [USERNAME].ovpn`

#### Syncthing

Make sure to set up a user and password for the web GUI. You can do that by
accesing it ang going to settings.

*Ports*: **22000/tcp** as the listening address and **21027/udp** for local
discovery.

#### Tranmission

It's recommended to enable port forwarding in your router as explained in
[superuser](https://superuser.com/questions/1053414/how-does-port-forwarding-help-in-torrents). The default port is **51413** but you can change this from the
web configurations.

If you don't set `tranmission_user` and `transmission_pass` you'll need to edit
**settings.json** as explained in
[hub.docker.com](https://hub.docker.com/r/linuxserver/transmission/)

*Ports*: **51413/udp** for p2p connections.

#### Radicale

You must set `radicale_pass` with your bcrypted password. Yo can get the hash
by running:

```bash
htpasswd -B /tmp/radicale [user]
```

Get it from */tmp/radicale*.

#### Taskd

The taskwarrior server.

*Ports*: **53589/tcp**.

Open a shell in the container.

```bash
docker exec -it taskd /bin/sh
```

And then from inside the container run the commands from the
[taskwarrior docs](https://taskwarrior.org/docs/taskserver/user.html).

**Note**: The *pki* directory is in */var/taskd/pki/*

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

## License

GPLv3

## Author Information

m0wer: m0wer (at) autistici.org
