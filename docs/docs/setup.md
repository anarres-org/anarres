# Setup

Clone the repo and its submodules with:

```bash
git clone --recurse-submodules -j10 [repo]
```

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

## Tips

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

## Firewall

If you are behind some kind of firewall or you need to setup NAT, you should
add the following ports:

* **80** for HTTP connections, used for the `letsencrypt` verification
* **443** for HTTPs connections, used by the reverse proxy to serve access to
  the web services.
* The SSH port you choose, or **2222** by default.
* All the desired ports that some services have.

## Letsencrypt

The main domain cert needs to be obtained using the **standalone** method since
we don't have a working webserver by this point (the server needs the cert). So
the webroot path will be empty in */etc/letsencrypt/renewal/{{ base_domain
}}.conf*. You should manually specify it adding:

```
authenticator = webroot
webroot_path = /var/www/letsencrypt,
```

## Nvidia runtime support

Some services (such as jellyfin and jupyter) can benefit from GPU acceleration.
In order to generally enable nvdia runtime support for the services set the
variable `nvidia_runtime` to `true`. Note that the nvidia-container-toolkit
must be installed manually, check
[nvidia-docker](https://github.com/NVIDIA/nvidia-docker).
