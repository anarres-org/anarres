# Sec

Ansible role for basic GNU/Linux server hardening.

* Sets up `iptables` for IPv4. **IPv6** will be disabled!!!
	* Will disable all incoming traffic by default except for established
	connectios, ICMP type 8 pings, the ssh_port and the **loopback** network
	traffic.
* Sets up `fail2ban` with alerts through XMPP.
	* With the SSHd jail.
* Hardens SSH.
	* Disables root login, password login...

It requires `iptables` to be flushed if already installed. This can be
achieved with:
```bash
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -t nat -F
iptables -t mangle -F
iptables -F
iptables -X
```

It is part of [anarres](https://git.hdg.sh/anarres/anarres), a playbook that
uses a collection of roles to deploy a full-featured server. But it can be used
and tested independently.

**Note**: This role is not idempotent but intends to be. We are waiting for the
new version of the `ipatbles_raw` asnible module. You can follow the updates
in this [pull request](https://github.com/ansible/ansible/pull/21054).

## Compatibility

These are the tested GNU/Linux distributions. Maybe it works on some other
distributions too or just requieres a few changes.

* [debian](https://www.debian.org/)
	* stretch

## Requirements

* [iptables_raw](https://github.com/Nordeus/ansible_iptables_raw)
* A configured `sendxmpp_config` file so `fail2ban` is able to send the alerts.

## Role Variables

### SSHd

* `ssh_port`: Port for `sshd` to bind to.

### sendxmpp

* `admin_xmpp`: Jabber account of an administrator. Will receive `fail2ban`
notifications.
* `sendxmpp_config`: `sendxmpp` configuration file path.

### fail2ban

* `fail2ban_trusted`: `fail2ban` trusted IPs, hosts or ranges.
* `fail2ban_xmpp_notify`: address used by `fail2ban` to send notifications to.
By default is the same as `admin_xmpp`.

### iptables

* `iptables_rules_general`: Default `iptables` rules.
* `iptables_policies_general`: Default `iptables` policies.
* `iptables_rules_logging`: Default `iptables` logging rules. They will be
placed at the end.

## Dependencies

None.

## Example playbook

```yaml
- hosts: all
  become: true
  vars:
  	admin_xmpp: admin@host.com
  roles:
    - anarres-sec
```

## Testing

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/)
.

```bash
molecule test
```

There is more documentation about the installation and configuration of the
required tools at
[wiki-testing](https://git.hdg.sh/anarres/anarres/wiki/testing).

## License

GPLv3

## Author Information

m0wer: m0wer (at) autistici.org
