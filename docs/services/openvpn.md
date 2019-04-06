# OpenVPN

## Ports

* **1194/udp**.

## Usage

### Genereate new user keys

`docker exec -it openvpn easyrsa build-client-full [USERNAME] nopass`

### Get the configuration file for an existing user

`docker exec -it openvpn ovpn_getclient [USERNAME] > [USERNAME].ovpn`
