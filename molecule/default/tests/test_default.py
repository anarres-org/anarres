import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("service", [
    ("gitea"),
    ("drone"),
    ("transmission"),
    ("wallabag"),
    ("syncthing"),
    ("openvpn"),
    ("radicale"),
    ("taskd"),
    ("nextcloud"),
    ("nfs"),
    ("openldap"),
    ("phpldapadmin"),
    ("bind_dns_server")
])
def test_services_are_enabled_and_running(host, service):
    service = host.service("docker." + service + ".service")
    assert service.is_enabled
    assert service.is_running
