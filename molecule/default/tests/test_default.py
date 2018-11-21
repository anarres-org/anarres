import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize("service", [
    ("gitea"),
    ("transmission"),
    ("wallabag"),
    ("syncthing"),
    ("openvpn"),
    ("radicale")
])
def test_iptables_is_installed(host, service):
    service = host.service("docker." + service + ".service")
    assert service.is_enabled
    assert service.is_running
