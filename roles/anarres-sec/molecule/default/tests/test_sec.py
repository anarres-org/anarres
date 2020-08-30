import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_install_iptables_persistent(host):
    iptables_package = host.package("iptables-persistent")
    assert iptables_package.is_installed


def test_install_fail2ban(host):
    f2b_package = host.package("fail2ban")
    assert f2b_package.is_installed


def test_fail2ban_action_conf(host):
    fail2ban_action_conf = host.file("/etc/fail2ban/action.d/xmpp.conf")
    assert fail2ban_action_conf.exists
    assert fail2ban_action_conf.contains("sendxmpp")
    assert fail2ban_action_conf.user == "root"
    assert fail2ban_action_conf.group == "root"
    assert fail2ban_action_conf.mode == 0o600


def test_fail2ban_conf(host):
    fail2ban_conf = host.file("/etc/fail2ban/jail.local")
    assert fail2ban_conf.exists
    assert fail2ban_conf.contains("[sshd]")
    assert fail2ban_conf.user == "root"
    assert fail2ban_conf.group == "root"


def test_sshd_conf(host):
    sshd_conf = host.file("/etc/ssh/sshd_config")
    assert sshd_conf.exists
    assert sshd_conf.contains("^PasswordAuthentication no$")
    assert sshd_conf.user == "root"
    assert sshd_conf.group == "root"
