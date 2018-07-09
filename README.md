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

## Usage

1. Install `sudo` and `python`.
2. Login as **root** and add your **user** to *sudoers* or to the **sudo**
group with `usermod -a -G sudo [user]`.

### Gitea

First user to register will be the admin user.

### Tranmission

It's recommended to enable port forwarding in your router as explained in
[superuser](https://superuser.com/questions/1053414/how-does-port-forwarding-help-in-torrents). The default port is **51413** but you can change this from the
web configurations.

If you don't set `tranmission_user` and `transmission_pass` you'll need to edit
**settings.json** as explained in
[hub.docker.com](https://hub.docker.com/r/linuxserver/transmission/)

## License

GPLv3

## Author Information

m0wer: m0wer (at) autistici.org
