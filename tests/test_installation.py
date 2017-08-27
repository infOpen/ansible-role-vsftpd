"""
Role tests
"""

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('name', [
    ('vsftpd'),
    ('db5.3-util'),
])
def test_installed_packages(host, name):
    """
    Test if packages installed
    """

    assert host.package(name).is_installed


def test_service(host):
    """
    Test service state
    """

    service = host.service('vsftpd')

    assert service.is_enabled
    assert service.is_running


def test_process(host):
    """
    Test process state
    """

    assert len(host.process.filter(comm='vsftpd')) == 1


def test_socket(host):
    """
    Test ports
    """

    assert host.socket('tcp://127.0.0.1:21').is_listening


def test_user(host):
    """
    Test ftp user exists
    """

    ftp_user = host.user('ftp')

    assert ftp_user.exists
    assert ftp_user.shell == '/bin/false'
