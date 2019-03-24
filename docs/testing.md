# Testing

The testing process consists in deploying the complete playbook (**full.yml**)
to a fresh virtual machine using
[molecule](https://github.com/metacloud/molecule) and `vagrant`.

Steps that will be made:

1. Destroy pre-existing instances.
2. **Not used**. Fetch dependencies (git or ansible-galaxy).
3. Syntax check.
4. Create instances.
5. Prepare instances (install python).
5. Converge: deploy the playbook.
6. Idempotence: re-run the playbook.
7. Lint: ansible good practices.
8. **Not used**. Side effects.
9. Verify: run tests.
10. Destroy instances.

```
└── default
    ├── destroy
    ├── dependency
    ├── syntax
    ├── create
    ├── prepare
    ├── converge
    ├── idempotence
    ├── lint
    ├── side_effect
    ├── verify
    └── destroy
```

**Note:** you can run a step individually: `molecule [step]`.

You will need:

* `virtualbox`
* `vagrant`
	* [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest)
	* [vagrant-cachier](https://github.com/fgrehm/vagrant-cachier) (optional).
	* Used `vagrant` boxes. Example: `vagrant box add debian/stretch64`.
* Python tools: `pip install molecule testinfra python-vagrant ansible yamllint ansible-lint`
**Note:** a `virtualenv` (python2) is recommended. You can use
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).
* A docker registry mirror in your local machine (optional).

	You can install it following this guide: [docker-doc](https://docs.docker.com/registry/recipes/mirror/).
	TL;DR: `docker run -d -p 5000:5000 --restart always --name registry -e "REGISTRY_DELETE_ENABLED=true" -e "REGISTRY_PROXY_REMOTEURL=https://registry-1.docker.io" registry:2`

	If you don't want to use it, comment or delete `docker_registry_mirror: http://172.16.100.1:5000`
	in *molecule/default/molecule.yml*.

	If you use `iptables` on your host machine:
	`iptables -A INPUT -s 172.16.100.0/24 -i vboxnet0 -p tcp -m tcp --dport 5000 -j ACCEPT`.

## Configuration

The main configuration file is *molecule/default/molecule.yml*.

## Process

To run every step mentioned above: `molecule test`.

That's all.

## Workflow

1. Change stuff and write its tests.
2. `molecule test`
3. Correct the errors.
4. Re run only the failing part. E.g. `molecule idempotence`.

## Tips

* You can connect to the virtual machine with: `molecule login`. This is really useful for debugging.
* You can run only the tests with `molecule verify`.
* It is useful to add this lines to your local */etc/hosts* file, so that you can access the testing virtual machine via web:
```
## anarres
172.16.100.12	anarres.local
172.16.100.12	git.anarres.local
172.16.100.12	cloud.anarres.local
172.16.100.12	drone-github.anarres.local
```
* You can get more information from `molecule` running it in **debug** mode: `molecule --debug test`.
* Be careful for not adding folders like `.venv`. **Virtualenv must be outside**.
