# BIND DNS server

[BIND9](https://www.isc.org/bind/) Versatile, classic, complete name server
software.

You need to specify the user with the `uid` **101** if it isn't
**systemd-network**. Check it in */etc/passwd*.

Refer to [ubuntu-help](https://help.ubuntu.com/community/BIND9ServerHowto) to
see how to configure it.

## Ports

* **53/tcp and udp**.
