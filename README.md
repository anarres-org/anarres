# Anarres Full Playbook

An [ansible](https://github.com/ansible) playbook to set up a GNU/Linux server.
Services in [docker](https://www.docker.com/). Security by default.

The goal is to have a server for a community or personal use that's easy to
maintain, secure and easy (and fast) to rebuild from scratch in case of data
loss or a migration.

The idea came from a great FLOSS project,
[sovereign](https://github.com/sovereign/sovereign), specially from [sovereign
2 issue](https://github.com/sovereign/sovereign/issues/667).

What you'll get with this repo is a recipe based in variables that will setup a
working server for your specific needs. You'll have the data stored only in one
or two directories depending on your choices, see [backup](#backup). The
docker containers will upgrade themselves automatically every time their
service restarts (you can do this periodically or it'll happen anyways when you
reboot).

Apart from this, it's easy to extend and doesn't prevent you from using other
playbooks apart from this one or installing things manually.

## Usage

Clone the repo and its submodules with:

```bash
git clone --recurse-submodules -j8 [repo]
```

Then follow the [Setup](#setup) section.

## Compatibility

These are the tested GNU/Linux distributions. Maybe it works on some other
distributions too or just requires a few changes.

* [debian](https://www.debian.org/)
  * stretch

## Requirements

`sudo` and `python`.

## Playbook Variables

TBD.

## Dependencies

Included as submodules in *roles/*.

* [iptables_raw](https://github.com/Nordeus/ansible_iptables_raw)
* [anarres-common](https://github.com/anarres-org/anarres-common)
* [anarres-sec](https://github.com/anarres-org/anarres-sec)
* [letsencrypt-request](https://github.com/anarres-org/letsencrypt-request)
* [anarres-nginx](https://github.com/anarres-org/anarres-nginx)
* [generic_docker_systemd](https://github.com/anarres-org/generic_docker_systemd)
* [add_nginx_proxy_conf](https://github.com/anarres-org/add_nginx_proxy_conf)

## Services

Their data and configuration files will be stored in your hosts `data_path`
directory, by default */data*.

* [Docker Registry](https://docs.docker.com/registry/): A stateless, highly
   scalable server side application that stores and lets you distribute Docker
   images. Using [library/registry](https://hub.docker.com/_/registry).
* [CoreOS Clair](https://github.com/coreos/clair): Vulnerability Static Analysis
   for Containers. Using
   [quay.io/coreos/clair](https://quay.io/repository/coreos/clair).
* [Jessfraz Docker registry web interface](https://github.com/genuinetools/reg):
   Docker registry v2 command line client and repo listing generator with
   security checks. Using
   [jessfraz/reg](https://hub.docker.com/r/jessfraz/reg).
* [OpenLDAP](http://www.openldap.org/): Using
   [osixia/openldap](https://github.com/osixia/docker-openldap).
* [phpLDAPadmin](http://phpldapadmin.sourceforge.net/):
   Using
   [osixia/phpldapadmin](https://github.com/osixia/docker-phpLDAPadmin).
* [Prosody IM](https://prosody.im/): A modern XMPP communication server. Using
  [unclev/prosody-docker-extended](https://github.com/unclev/prosody-docker-extended).
* [Gitea](https://docs.gitea.io/): Using
  [gitea/gitea](https://github.com/go-gitea/gitea).
* [Drone](https://drone.io/): Using
  [drone/drone](https://github.com/drone/drone). For the self hosted gitea and
  for GitHub.
* [CodiMD](https://github.com/hackmdio/codimd): [HackMD](https://hackmd.io/)
  like realtime collaborative markdown notes service. Using
  [docker-hackmd](https://github.com/hackmdio/docker-hackmd).
* [Transmission](https://transmissionbt.com/): Using
  [linuxserver/transmission](https://github.com/linuxserver/docker-transmission)
  or [docker-transmission-openvpn](https://github.com/haugene/docker-transmission-openvpn).
* [Wallabag](https://wallabag.org/): Using
  [wallabag/wallabag](https://github.com/wallabag/docker).
* [Syncthing](https://syncthing.net/): Using
  [syncthing/syncthing](https://github.com/syncthing/syncthing).
* [OpenVPN](https://openvpn.net/): Using
  [kylemanna/openvpn](https://github.com/kylemanna/docker-openvpn).
* [Radicale](https://radicale.org/): Using
  [tomsquest/docker-radicale](https://github.com/tomsquest/docker-radicale).
* [Taskwarrior Server](https://taskwarrior.org/): Using
  [andir/docker-taskd](https://github.com/andir/docker-taskd).
* [Nextcloud](https://nextcloud.com/): Using
  [nextcloud](https://github.com/nextcloud/docker).
* [Taiga](https://taiga.io/): Project management platform for agile developers
   & designers and project managers. Using
  [docker-taiga](https://github.com/m0wer/docker-taiga).
* [NFS Server](https://sourceforge.net/projects/nfs/): Using
  [erichough/nfs-server](https://github.com/ehough/docker-nfs-server).
* [BIND9](https://www.isc.org/bind/) Versatile, classic, complete name server
   software. Using [sameersbn/bind](https://github.com/sameersbn/docker-bind).
* [Murmur](https://wiki.mumble.info/wiki/Main_Page): Open source, low-latency,
   high quality voice chat software. Using
   [m0wer/murmur](https://hub.docker.com/r/m0wer/murmur).
* [InfluxDB](https://www.influxdata.com/): Scalable datastore for metrics,
   events, and real-time analytics. Using
   [influxdb](https://hub.docker.com/_/influxdb).
* [Grafana](https://grafana.com/): The open platform for beautiful
   analytics and monitoring. Using
   [grafana/grafana](https://hub.docker.com/r/grafana/grafana).
* [Home Assistant](https://www.home-assistant.io/) Open source home automation
   that puts local control and privacy first. Using
   [homeassistant/home-assistant](https://hub.docker.com/r/homeassistant/home-assistant)
* [RStudio](https://www.rstudio.com/) provides popular open source and
   enterprise-ready professional software for the R statistical computing
   environment. Using
   [rocker/rstudio](https://hub.docker.com/r/rocker/rstudio).
* [Jellyfin](https://jellyfin.media/) The Free Software Media System. Using
  [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin).
* [Portainer](https://www.portainer.io/) Making Docker management easy. Using
  [portainer/portainer](https://hub.docker.com/r/portainer/portainer).
* [Anki sync server](https://github.com/tsudoko/anki-sync-server) This is a
   personal Anki server, which you can sync against instead of AnkiWeb. Using
   [kuklinistvan/anki-sync-server](https://hub.docker.com/r/kuklinistvan/anki-sync-server/tags).
* [Moodle](https://moodle.org/) Open-source learning plataform. Using
  [moodlehq/moodle-php-apache](https://hub.docker.com/r/moodlehq/moodle-php-apache).
* [JupyterHub](https://jupyter.org/hub) A multi-user version of the notebook
   designed for companies, classrooms and research labs. Using
   [m0wer/jupyterhub](https://hub.docker.com/r/m0wer/jupyterhub).

For more info about each service and how to set it up, go to
[docs/services](docs/services).

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
* By default, the configuration files of the services won't be overridden in
  most cases, meaning that if they already existed they won't be modified, to
  preserve their possible manual modifications. To avoid this behaviour and
  overwrite them, pass the `override=True` extra var.

### Firewall

If you are behind some kind of firewall or you need to setup NAT, you should
add the following ports:

* **80** for HTTP connections, used for the `letsencrypt` verification
* **443** for HTTPs connections, used by the reverse proxy to serve access to
  the web services.
* The SSH port you choose, or **2222** by default.
* All the desired ports that some services have.

### Letsencrypt

The main domain cert needs to be obtained using the **standalone** method since
we don't have a working webserver by this point (the server needs the cert). So
the webroot path will be empty in */etc/letsencrypt/renewal/{{ base_domain
}}.conf*. You should manually specify it adding:

```
authenticator = webroot
webroot_path = /var/www/letsencrypt,
```

### Nvidia runtime support

Some services (such as jellyfin and jupyter) can benefit from GPU acceleration.
In order to generally enable nvdia runtime support for the services set the
variable `nvidia_runtime` to `true`. Note that the nvidia-container-toolkit
must be installed manually, check
[nvidia-docker](https://github.com/NVIDIA/nvidia-docker).

## Backup

Make sure to backup your `data_path` (by default */data*) and the docker
volumes (used by the databases) from */var/lib/docker/volumes* if used.

## License

GPLv3

## Author Information

m0wer: m0wer (at) autistici.org
