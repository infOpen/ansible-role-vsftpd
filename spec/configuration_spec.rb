require 'serverspec'

# Configuration file
describe file('/etc/vsftpd.conf') do

    # File properties
    it { should be_file }
    it { should exist }

    # File content
    its(:content) {

        # LISTEN
        should match /^listen=YES$/
        should match /^listen_address=127.0.0.1$/
        should match /^listen_address6=::1$/
        should match /^listen_ipv6=NO$/
        should match /^one_process_model=NO$/
        should match /^run_as_launching_user=NO$/

        # SSL
        should match /^ssl_enable=NO$/
        should match /^allow_anon_ssl=NO$/
        should match /^ca_certs_file=$/
        should match /^debug_ssl=NO$/
        should match /^dsa_cert_file=$/
        should match /^dsa_private_key_file=$/
        should match /^force_anon_data_ssl=NO$/
        should match /^force_anon_logins_ssl=NO$/
        should match /^force_local_data_ssl=NO$/
        should match /^force_local_logins_ssl=NO$/
        should match /^implicit_ssl=NO$/
        should match /^require_cert=NO$/
        should match /^require_ssl_reuse=YES$/
        should match /^rsa_cert_file=\/etc\/ssl\/certs\/ssl-cert-snakeoil.pem$/
        should match /^rsa_private_key_file=\/etc\/ssl\/certs\/ssl-cert-snakeoil.pem$/
        should match /^ssl_ciphers=HIGH$/
        should match /^ssl_request_cert=YES$/
        should match /^strict_ssl_read_eof=NO$/
        should match /^strict_ssl_write_shutdown=NO$/
        should match /^validate_cert=NO$/

        # ACCESS RULES
        # Anonymous management
        should match /^anonymous_enable=NO$/
        should match /^anon_max_rate=0$/
        should match /^anon_umask=0077$/
        should match /^anon_mkdir_write_enable=NO$/
        should match /^anon_other_write_enable=NO$/
        should match /^anon_root=$/
        should match /^anon_upload_enable=NO$/
        should match /^anon_world_readable_only=NO$/
        should match /^guest_enable=NO$/
        should match /^no_anon_password=NO$/

        # Transfert and rigths management
        should match /^accept_timeout=60$/
        should match /^ascii_download_enable=NO$/
        should match /^ascii_upload_enable=NO$/
        should match /^async_abor_enable=NO$/
        should match /^check_shell=YES$/
        should match /^chmod_enable=YES$/
        should match /^chown_upload_mode=0600$/
        should match /^chown_uploads=NO$/
        should match /^chown_username=root$/
        should match /^chroot_list_enable=NO$/
        should match /^chroot_local_user=NO$/
        should match /^cmds_allowed=$/
        should match /^cmds_denied=$/
        should match /^connect_from_port_20=NO$/
        should match /^connect_timeout=60$/
        should match /^data_connection_timeout=300$/
        should match /^delay_failed_login=1$/
        should match /^delay_successful_login=0$/
        should match /^deny_file=$/
        should match /^download_enable=YES$/
        should match /^dirlist_enable=YES$/
        should match /^dirmessage_enable=NO$/
        should match /^file_open_mode=0666$/
        should match /^ftp_data_port=20$/
        should match /^ftp_username=ftp$/
        should match /^guest_username=ftp$/
        should match /^hide_file=$/
        should match /^idle_session_timeout=300$/
        should match /^listen_port=21$/
        should match /^local_enable=NO$/
        should match /^local_max_rate=0$/
        should match /^local_root=$/
        should match /^local_umask=0077$/
        should match /^lock_upload_files=YES$/
        should match /^ls_recurse_enable=NO$/
        should match /^max_clients=0$/
        should match /^max_login_fails=3$/
        should match /^max_per_ip=0$/
        should match /^nopriv_user=nobody$/
        should match /^pam_service_name=vsftpd$/
        should match /^passwd_chroot_enable=NO$/
        should match /^port_enable=YES$/
        should match /^port_promiscuous=NO$/
        should match /^secure_chroot_dir=\/var\/run\/vsftpd\/empty$/
        should match /^tilde_user_enable=NO$/
        should match /^trans_chunk_size=0$/
        should match /^use_localtime=NO$/
        should match /^use_sendfile=YES$/
        should match /^user_config_dir=$/
        should match /^user_sub_token=$/
        should match /^write_enable=NO$/

        # Misc
        should match /^background=NO$/
        should match /^banned_email_file=\/etc\/vsftpd.banned_emails$/
        should match /^banner_file=$/
        should match /^delete_failed_uploads=NO$/
        should match /^force_dot_files=NO$/
        should match /^ftpd_banner=$/
        should match /^hide_ids=NO$/
        should match /^mdtm_write=NO$/
        should match /^message_file=.message$/
        should match /^session_support=NO$/
        should match /^setproctitle_enable=NO$/
        should match /^tcp_wrappers=NO$/
        should match /^text_userdb_names=NO$/
        should match /^virtual_use_local_privs=NO$/

        # Logging
        should match /^dual_log_enable=YES$/
        should match /^log_ftp_protocol=YES$/
        should match /^no_log_lock=NO$/
        should match /^syslog_enable=NO$/
        should match /^vsftpd_log_file=\/var\/log\/vsftpd.log$/
        should match /^xferlog_enable=YES$/
        should match /^xferlog_file=\/var\/log\/xferlog$/
        should match /^xferlog_std_format=NO$/

        # Passive mode options
        should match /^pasv_addr_resolve=NO$/
        should match /^pasv_enable=YES$/
        should match /^pasv_max_port=0$/
        should match /^pasv_min_port=0$/
        should match /^pasv_promiscuous=NO$/

        # List management
        should match /^chroot_list_file=\/etc\/vsftpd.chroot_list$/
        should match /^deny_email_enable=NO$/
        should match /^email_password_file=\/etc\/vsftpd.email_passwords$/
        should match /^secure_email_list_enable=NO$/
        should match /^userlist_deny=YES$/
        should match /^userlist_enable=NO$/
        should match /^userlist_file=\/etc\/vsftpd.user_list$/
    }
end


