# vsftpd

[![Build Status](https://travis-ci.org/infOpen/ansible-role-vsftpd.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-vsftpd)

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
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

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
#------------------
vsftpd_package_state: present

# Service variables
#------------------
vsftpd_service_state: started
vsftpd_service_enabled: True

# Configuration file variables
#-----------------------------
vsftpd_config_directory_name: /etc/
vsftpd_config_directory_mode: '0755'
vsftpd_config_directory_owner: root
vsftpd_config_directory_group: root

vsftpd_config_file_name: vsftpd.conf
vsftpd_config_file_mode: '0644'
vsftpd_config_file_owner: root
vsftpd_config_file_group: root

# Additional PAM configuration
#-----------------------------
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
#-----------------------------------------
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
    owner: ftp
    group: ftp
    mode: '0550'
  - path: '/in'
    owner: ftp
    group: ftp
    mode: '0770'
  - path: '/out'
    owner: ftp
    group: ftp
    mode: '0770'

# Additional config files
#------------------------
vsftpd_additional_directories_group: root
vsftpd_additional_directories_owner: root
vsftpd_additional_directories_mode: '0755'
vsftpd_additional_files_group: root
vsftpd_additional_files_owner: root
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

# Default values
#---------------

# Listen
vsftpd_listen: True
vsftpd_listen_address: '127.0.0.1'
vsftpd_listen_address6: '::1'
vsftpd_listen_ipv6: False
vsftpd_one_process_model: False
vsftpd_run_as_launching_user: False

# SSL
vsftpd_ssl_enable: False
vsftpd_allow_anon_ssl: False
vsftpd_ca_certs_file: ''
vsftpd_dsa_cert_file: ''
vsftpd_dsa_private_key_file: "{{ vsftpd_dsa_cert_file }}"
vsftpd_force_anon_data_ssl: False
vsftpd_force_anon_logins_ssl: False
vsftpd_force_local_data_ssl: False
vsftpd_force_local_logins_ssl: False
vsftpd_implicit_ssl: False
vsftpd_require_cert: False
vsftpd_require_ssl_reuse: True
vsftpd_rsa_cert_file: '/etc/ssl/certs/ssl-cert-snakeoil.pem'
vsftpd_rsa_private_key_file: "{{ vsftpd_rsa_cert_file }}"
vsftpd_ssl_ciphers: 'HIGH'
vsftpd_ssl_request_cert: True
vsftpd_ssl_sslv2: False
vsftpd_ssl_sslv3: False
vsftpd_ssl_tlsv1: True
vsftpd_strict_ssl_read_eof: False
vsftpd_strict_ssl_write_shutdown: False
vsftpd_validate_cert: False
vsftpd_debug_ssl: False

# Anonymuos management
vsftpd_anonymous_enable: False
vsftpd_anon_max_rate: 0
vsftpd_anon_umask: '0077'
vsftpd_anon_mkdir_write_enable: False
vsftpd_anon_other_write_enable: False
vsftpd_anon_root: ''
vsftpd_anon_upload_enable: False
vsftpd_anon_world_readable_only: False
vsftpd_guest_enable: False
vsftpd_no_anon_password: False

# Transfert and right management
vsftpd_accept_timeout: 60
vsftpd_ascii_download_enable: False
vsftpd_ascii_upload_enable: False
vsftpd_async_abor_enable: False
vsftpd_check_shell: True
vsftpd_chmod_enable: True
vsftpd_chown_upload_mode: '0600'
vsftpd_chown_uploads: False
vsftpd_chown_username: 'root'
vsftpd_chroot_list_enable: False
vsftpd_chroot_local_user: False
vsftpd_cmds_allowed: []
vsftpd_cmds_denied: []
vsftpd_connect_from_port_20: False
vsftpd_connect_timeout: 60
vsftpd_data_connection_timeout: 300
vsftpd_delay_failed_login: 1
vsftpd_delay_successful_login: 0
vsftpd_deny_file: ''
vsftpd_download_enable: True
vsftpd_dirlist_enable: True
vsftpd_dirmessage_enable: False
vsftpd_file_open_mode: '0666'
vsftpd_ftp_data_port: 20
vsftpd_ftp_username: 'ftp'
vsftpd_guest_username: 'ftp'
vsftpd_hide_file: ''
vsftpd_idle_session_timeout: 300
vsftpd_listen_port: 21
vsftpd_local_enable: False
vsftpd_local_max_rate: 0
vsftpd_local_umask: '0077'
vsftpd_local_root: ''
vsftpd_lock_upload_files: True
vsftpd_ls_recurse_enable: False
vsftpd_max_clients: 0
vsftpd_max_login_fails: 3
vsftpd_max_per_ip: 0
vsftpd_nopriv_user: 'nobody'
vsftpd_pam_service_name: 'vsftpd'
vsftpd_passwd_chroot_enable: False
vsftpd_port_enable: True
vsftpd_port_promiscuous: False
vsftpd_secure_chroot_dir: '/var/run/vsftpd/empty'
vsftpd_tilde_user_enable: False
vsftpd_trans_chunk_size: 0
vsftpd_use_localtime: False
vsftpd_use_sendfile: True
vsftpd_user_config_dir: ''
vsftpd_user_sub_token: ''
vsftpd_write_enable: False

# Misc
vsftpd_background: False
vsftpd_banned_email_file: '/etc/vsftpd.banned_emails'
vsftpd_banner_file: ''
vsftpd_delete_failed_uploads: False
vsftpd_force_dot_files: False
vsftpd_ftpd_banner: ''
vsftpd_hide_ids: False
vsftpd_mdtm_write: False
vsftpd_message_file: '.message'
vsftpd_session_support: False
vsftpd_setproctitle_enable: False
vsftpd_tcp_wrappers: False
vsftpd_text_userdb_names: False
vsftpd_virtual_use_local_privs: False

# Logging
vsftpd_dual_log_enable: True
vsftpd_log_ftp_protocol: True
vsftpd_no_log_lock: False
vsftpd_syslog_enable: False
vsftpd_vsftpd_log_file: '/var/log/vsftpd.log'
vsftpd_xferlog_enable: True
vsftpd_xferlog_file: '/var/log/xferlog'
vsftpd_xferlog_std_format: False

# Passive mode options
vsftpd_pasv_address: ''
vsftpd_pasv_addr_resolve: False
vsftpd_pasv_enable: True
vsftpd_pasv_max_port: 60010
vsftpd_pasv_min_port: 60000
vsftpd_pasv_promiscuous: False

# List management
vsftpd_chroot_list_file: '/etc/vsftpd.chroot_list'
vsftpd_deny_email_enable: False
vsftpd_email_password_file: '/etc/vsftpd.email_passwords'
vsftpd_secure_email_list_enable: False
vsftpd_userlist_deny: True
vsftpd_userlist_enable: False
vsftpd_userlist_file: '/etc/vsftpd.user_list'
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
