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

## Documentation

[Anarres documentation](https://anarres-org.github.io/anarres/).

## Compatibility

These are the tested GNU/Linux distributions. Maybe it works on some other
distributions too or just requires a few changes.

* [debian](https://www.debian.org/)
  * buster

## Requirements

`sudo` and `python`.

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

Check the full list at [Supported services list - Anarres
documentation](https://anarres-org.github.io/anarres/supported_services_list/).

For more info about each service and how to set it up, refer to the
documentation.

## Setup

Refer to [Setup - Anarres
documentation](https://anarres-org.github.io/anarres/setup/).

## Backup

Make sure to backup your `data_path` (by default */data*).

## License

GPLv3

## Author Information

* m0wer: m0wer (at) autistici (dot) org
* acien101: amil101ftw (at) gmail (dot) com
