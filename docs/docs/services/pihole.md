# PiHole

[Pi-hole](https://pi-hole.net/) Netrwork-wide protection.

## Variables

* `pihole_docker_image`: Name for the service docker image.
* `pihole_internal_web_port`: (Default: `5010`) Port on the host to bind the service to.
* `pihole_domain`: Domain/subdomain for the service.
* `pihole_pass`: Password for the admin user.
* `pihole_directory`:
   * `conf`: Path on the host for the persistent configuration directory.
   * `dnsmasq`: Path on the host for the persistent dnsmasq configuration directory.
* `pihole_lan_ip`: Host's IP in the LAN.
* `pihole_dns1`: (Default: `1.1.1.1`) Main DNS server 1.
* `pihole_dns2`: (Default: `8.8.8.8`) Main DNS server 2.

## Setup

1. Set, at least, the undefined variables and deploy the service.
