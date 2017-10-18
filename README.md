# vsftpd

[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-vsftpd/master.svg?label=travis_master)](https://travis-ci.org/infOpen/ansible-role-vsftpd)
[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-vsftpd/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/ansible-role-vsftpd)
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-vsftpd/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-vsftpd/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-vsftpd/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-vsftpd/)
[![Ansible Role](https://img.shields.io/ansible/role/7941.svg)](https://galaxy.ansible.com/infOpen/vsftpd/)

Install vsftpd package.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

It can work with older version but without garanty, due to minimal Ansible
version required by Molecule.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Manage virtual users

You can manage virtual users with a berkeleyDB.
- set "vsftpd_virtual_users_with_berkeleydb" to True
- set "vsftpd_virtual_users" with your user list
``` yaml
vsftpd_virtual_users:
  - username: my_account
    password: my_password
```
- change pam configuration with "vsftpd_pam_configuration_file_content"

If you want to reset database, set "vsftpd_virtual_users_clean_database" to
True

## Embed filter plugins

### vsftpd_boolean_render(arg)

This embed jinja filter used to set boolean values following VSFTPD rules :
  - YES for true values
  - NO for false values

Usage :

``` yaml
{{ my_string | vsftpd_boolean_render() }}
```

### vsftpd_positive_integer_validate(arg)

This embed jinja filter used to check if values are positive integer

Usage :

``` yaml
{{ my_string | vsftpd_positive_integer_validate() }}
```

### vsftpd_otcal_mode_validate(arg)

This embed jinja filter used to check if values are octal linux mode

Usage :

``` yaml
{{ my_string | vsftpd_octal_mode_validate() }}
```

## Role Variables

### Default role variables

``` yaml
# Package variables
vsftpd_package_state: 'present'
vsftpd_packages: "{{ _vsftpd_packages }}"

# Service variables
vsftpd_service_name: "{{ _vsftpd_service_name }}"
vsftpd_service_state: 'started'
vsftpd_service_enabled: True

# Configuration file variables
vsftpd_config_directory_name: '/etc/'
vsftpd_config_directory_mode: '0755'
vsftpd_config_directory_owner: 'root'
vsftpd_config_directory_group: 'root'
vsftpd_config_file_name: 'vsftpd.conf'
vsftpd_config_file_mode: '0644'
vsftpd_config_file_owner: 'root'
vsftpd_config_file_group: 'root'

# Additional PAM configuration
vsftpd_pam_configuration_file: '/etc/pam.d/vsftpd'
vsftpd_pam_configuration_file_content: |
  # Standard behaviour for ftpd(8).
  authrequiredpam_listfile.so item=user sense=deny file=/etc/ftpusers onerr=succeed
  # Note: vsftpd handles anonymous logins on its own. Do not enable pam_ftp.so.
  # Standard pam includes
  @include common-account
  @include common-session
  @include common-auth
  authrequiredpam_listfilepam_shells.so

# Virtual users management with BerkeleyDB
vsftpd_virtual_users_with_berkeleydb: False
vsftpd_virtual_users_clean_database: False
vsftpd_virtual_users_database_file_name: '/etc/vsftpd_users.db'
vsftpd_virtual_users_database_file_owner: 'root'
vsftpd_virtual_users_database_file_group: 'root'
vsftpd_virtual_users_database_file_mode: '0700'
vsftpd_virtual_users: []
vsftpd_virtual_user_root_directory: '/data/ftp'
vsftpd_virtual_user_directories:
  - path: '/'
    owner: 'ftp'
    group: 'ftp'
    mode: '0550'
  - path: '/in'
    owner: 'ftp'
    group: 'ftp'
    mode: '0770'
  - path: '/out'
    owner: 'ftp'
    group: 'ftp'
    mode: '0770'

# Additional config files
vsftpd_additional_directories_group: 'root'
vsftpd_additional_directories_owner: 'root'
vsftpd_additional_directories_mode: '0755'
vsftpd_additional_files_group: 'root'
vsftpd_additional_files_owner: 'root'
vsftpd_additional_files_mode: '0755'
vsftpd_ca_certs_file_content: ''
vsftpd_dsa_cert_file_content: ''
vsftpd_dsa_private_key_file_content: ''
vsftpd_rsa_cert_file_content: ''
vsftpd_rsa_private_key_file_content: ''
vsftpd_banned_email_file_content: ''
vsftpd_banner_file_content: ''
vsftpd_chroot_list_file_content: ''
vsftpd_email_password_file_content: ''
vsftpd_userlist_file_content: ''


# DEFAULT VALUES

# Each file must have a dedicated variable
# Difference
vsftpd_main_config: "{{ _vsftpd_main_config }}"
vsftpd_paths:
  files:
    banned_email:
      path: '/etc/vsftpd.banned_emails'
    banner: {}
    ca_certs: {}
    chroot_list:
      path: '/etc/vsftpd.chroot_list'
    deny: {}
    dsa_cert: {}
    dsa_private_key: {}
    email_password:
      path: '/etc/vsftpd.email_passwords'
    hide: {}
    init_d:
      path: '/etc/init.d/vsftpd'
    main_config:
      path: '/etc/vsftpd.conf'
    pam_configuration:
      path: '/etc/pam.d/vsftpd'
    message:
      path: '.message'
    rsa_cert:
      path: '/etc/ssl/certs/ssl-cert-snakeoil.pem'
    rsa_private_key:
      path: '/etc/ssl/private/ssl-cert-snakeoil.key'
    userlist:
      path: '/etc/vsftpd.user_list'
```

### Debian OS family role variables

``` yaml
_vsftpd_packages:
  - 'vsftpd'
  - 'db5.3-util'

_vsftpd_service_name: 'vsftpd'

_vsftpd_pam_config: |
  authrequiredpam_listfile.so item=user sense=deny file=/etc/ftpusers onerr=succeed
  @include common-account
  @include common-session
  @include common-auth
  authrequiredpam_listfilepam_shells.so

_vsftpd_main_config:
  boolean_options:
    allow_anon_ssl: NO
    anon_mkdir_write_enable: NO
    anon_other_write_enable: NO
    anon_upload_enable: NO
    anon_world_readable_only: YES
    anonymous_enable: NO
    ascii_download_enable: NO
    ascii_upload_enable: NO
    async_abor_enable: NO
    background: NO
    check_shell: YES
    chmod_enable: YES
    chown_uploads: NO
    chroot_list_enable: NO
    chroot_local_user: NO
    connect_from_port_20: YES
    debug_ssl: NO
    delete_failed_uploads: NO
    deny_email_enable: NO
    dirlist_enable: YES
    dirmessage_enable: YES
    download_enable: YES
    dual_log_enable: NO
    force_dot_files: NO
    force_anon_data_ssl: NO
    force_anon_logins_ssl: NO
    force_local_data_ssl: YES
    force_local_logins_ssl: YES
    guest_enable: NO
    hide_ids: NO
    implicit_ssl: NO
    listen: NO
    listen_ipv6: YES
    local_enable: YES
    lock_upload_files: YES
    log_ftp_protocol: NO
    ls_recurse_enable: NO
    mdtm_write: YES
    no_anon_password: NO
    no_log_lock: NO
    one_process_model: NO
    passwd_chroot_enable: NO
    pasv_addr_resolve: NO
    pasv_enable: YES
    pasv_promiscuous: NO
    port_enable: YES
    port_promiscuous: NO
    require_cert: NO
    require_ssl_reuse: YES
    run_as_launching_user: NO
    secure_email_list_enable: NO
    session_support: NO
    setproctitle_enable: NO
    ssl_enable: NO
    ssl_request_cert: YES
    ssl_sslv2: NO
    ssl_sslv3: NO
    ssl_tlsv1: YES
    strict_ssl_read_eof: NO
    strict_ssl_write_shutdown: NO
    syslog_enable: NO
    tcp_wrappers: NO
    text_userdb_names: NO
    tilde_user_enable: NO
    use_localtime: YES
    use_sendfile: YES
    userlist_deny: YES
    userlist_enable: NO
    validate_cert: NO
    virtual_use_local_privs: NO
    write_enable: NO
    xferlog_enable: YES
    xferlog_std_format: NO
  integer_options:
    accept_timeout: 60
    anon_max_rate: 0
    connect_timeout: 60
    data_connection_timeout: 300
    delay_failed_login: 1
    delay_successful_login: 0
    ftp_data_port: 20
    idle_session_timeout: 300
    listen_port: 21
    local_max_rate: 0
    max_clients: 0
    max_login_fails: 3
    max_per_ip: 0
    pasv_max_port: 0
    pasv_min_port: 0
    trans_chunk_size: 0
  octal_options:
    anon_umask: '0077'
    chown_upload_mode: '0600'
    file_open_mode: '0666'
    local_umask: '0077'
  string_options:
    anon_root: ''
    banned_email_file: '/etc/vsftpd.banned_emails'
    banner_file: ''
    ca_certs_file: ''
    chown_username: 'root'
    chroot_list_file: '/etc/vsftpd.chroot_list'
    cmds_allowed: ''
    cmds_denied: ''
    deny_file: ''
    dsa_cert_file: ''
    dsa_private_key_file: ''
    email_password_file: '/etc/vsftpd.email_passwords'
    ftp_username: 'ftp'
    ftpd_banner: ''
    guest_username: 'ftp'
    hide_file: ''
    listen_address: '127.0.0.1'
    listen_address6: '::1'
    local_root: ''
    message_file: '.message'
    nopriv_user: 'nobody'
    pam_service_name: 'vsftpd'
    pasv_address: ''
    rsa_cert_file: '/etc/ssl/certs/ssl-cert-snakeoil.pem'
    rsa_private_key_file: '/etc/ssl/private/ssl-cert-snakeoil.key'
    secure_chroot_dir: '/var/run/vsftpd/empty'
    ssl_ciphers: 'DES-CBC3-SHA'
    user_config_dir: ''
    user_sub_token: ''
    userlist_file: '/etc/vsftpd.user_list'
    vsftpd_log_file: '/var/log/vsftpd.log'
    xferlog_file: '/var/log/xferlog'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.vsftpd }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- achaussier [at] infopen.pro
