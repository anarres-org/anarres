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

## Setup

1. Install `sudo` and `python`.
1. Login as **root** and add your **user** to *sudoers* or to the **sudo**
group with `usermod -a -G sudo [user]`.

### Gitea

First user to register will be the admin user.

### OpenVPN

Once installed, from the server's command line.

#### Genereate new user keys

`docker exec -it openvpn easyrsa build-client-full [USERNAME] nopass`

#### Get the configuration file for an existing user

`docker exec -it openvpn ovpn_getclient [USERNAME] > [USERNAME].ovpn`

### Syncthing

Make sure to set up a user and password for the web GUI. You can do that by
accesing it ang going to settings.

### Tranmission

It's recommended to enable port forwarding in your router as explained in
[superuser](https://superuser.com/questions/1053414/how-does-port-forwarding-help-in-torrents). The default port is **51413** but you can change this from the
web configurations.

If you don't set `tranmission_user` and `transmission_pass` you'll need to edit
**settings.json** as explained in
[hub.docker.com](https://hub.docker.com/r/linuxserver/transmission/)

### Radicale

You must set `radicale_pass` with your bcrypted password. Yo can get the hash
by running:

```bash
htpasswd -B /tmp/radicale [user]
```

Get it from */tmp/radicale*.

## Taskd

The taskwarrior server.

Open a shell in the container.

```bash
docker exec -it taskd /bin/sh
```

And then from inside the container run the commands from the
[taskwarrior docs](https://taskwarrior.org/docs/taskserver/user.html).

**Note**: The *pki* directory is in */var/taskd/pki/*

## Nextcloud

First user to register will be the admin user.

## License

GPLv3

## Author Information

m0wer: m0wer (at) autistici.org
