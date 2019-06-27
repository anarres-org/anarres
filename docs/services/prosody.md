# Prosody

[Posody IM](https://prosody.im/): A modern XMPP communication server.

## Variables

* `prosody_docker_image`: Name for the local service docker image.
* `prosody_domain: Domain/subdomain for the service.
* `prosody_domain_muc`: Domain for the Multi User Chatrooms.
* `prosody_enable_muc`: Boolean to enable or disable Multi User Chatrooms.
* `prosody_enable_tor`: Boolean to enable or disable connection through TOR.
* `prosody_tor_hostname`: TOR domain (.onion).
* `prosody_directory`:
   * `conf`: Path on the host for configurations.
   * `data`: Path on the host for data.
   * `modules_community`: Path on the host for community modules.
   * `modules_custom`: Path on the host for custom modules.
* `prosody_cert_path`:
   * `privkey`: Path on the host for the SSL/TLS private key.
   * `cert`: Path on the host for the SSL/TLS certificate.
* `prosody_port_c2s`: Port for client to client connections.
* `prosody_port_s2s`: Port for server to server connections.
* `prosody_iptables_c2s_rule`: Iptables rule for the c2c connections.
* `prosody_iptables_s2s_rule`: Iptables rule for the s2s connections.
* `prosody_admins_xmpp`: List of admins of the XMPP server.
* `prosody_allow_remote_registration`: Boolean to enable or disable remote
  registration.
* `prosody_users`: List of dictionaries with `jid` and `pass` values for the
  users to register.

## Ports (by default)

* **5222/tcp** for c2c connections.
* **5269/tcp** for s2s connections.
