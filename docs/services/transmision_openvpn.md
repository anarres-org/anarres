# Transmission-OpenVPN

[docker-transmission-openvpn](https://github.com/haugene/docker-transmission-openvpn)
Docker container running Transmission torrent client with WebUI over an OpenVPN
tunnel.

## Variables

* `transmission_openvpn_domain`: Domain/subdomain for the service.
* `transmission_openvpn_docker_image`: Name for the local service docker image
   (default: `haugene/transmission-openvpn:[version]`).
* `transmission_openvpn_internal_web_port`: Internal port on the host to bind
   the web interface to (default: `9091`).
* `transmission_openvpn_peer_port:` Openvpn p2p port (default: `51413`).
* `transmission_openvpn_dns`: DNS server to use inside the container (default:
   `1.1.1.1`).
* `transmission_openvpn_vpn`:
   * `provider`: Provider name.
   * `conf`: Sets the OpenVPN endpoint to connect to.
   * `user`: Your OpenVPN username.
   * `pass`: Your OpenVPN password.
* `transmission_openvpn_rpc`:
   * `user:` User for the web interface.
   * `pass`: Password for the web interface.
* `transmission_openvpn_directory`:
   * `data`: Path on the host for the downloads.

For more info about how to choose the variables, please refer to the
[docs](https://haugene.github.io/docker-transmission-openvpn/).
