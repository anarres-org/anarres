import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "service",
    [
        ("registry"),
        ("clair"),
        ("registry_web_interface"),
        ("prosody"),
        ("gitea"),
        ("drone"),
        ("drone_docker_runner"),
        ("drone_ssh_runner"),
        ("drone_github"),
        ("codimd"),
        ("transmission"),
        ("wallabag"),
        ("syncthing"),
        ("openvpn"),
        ("radicale"),
        ("taskd"),
        ("nextcloud"),
        ("taiga"),
        ("nfs"),
        ("openldap"),
        ("phpldapadmin"),
        ("bind_dns_server"),
        ("murmur"),
        ("influxdb"),
        ("grafana"),
        ("rstudio"),
        ("jellyfin"),
        ("portainer"),
        ("anki"),
        ("moodle"),
        ("jupyterhub"),
        ("jackett"),
        ("sonarr"),
        ("radarr"),
        ("lidarr"),
        ("bazarr"),
        ("ombi"),
        ("sharelatex"),
        ("tiddlywiki"),
        ("pihole"),
        ("grocy"),
        ("home_assistant"),
    ],
)
def test_services_are_enabled_and_running(host, service):
    service = host.service("docker." + service + ".service")
    assert service.is_enabled
    assert service.is_running
