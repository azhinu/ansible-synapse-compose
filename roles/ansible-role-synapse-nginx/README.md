
## Ansible role: Matrix-Synapse Nginx proxy
This role install Nginx as Synapse proxy and optionaly Element Matrix client.

#### Role vars and options:

`nginx_proxy_server_name: "matrix.example.com"` — Matrix hostname.

`nginx_use_certbot: true` — Use Certbot to automatically obtain certs.

`nginx_tls_cert_path: "/etc/letsencrypt/live/{{ nginx_proxy_server_name }}/fullchain.pem"` — TLS cert path. By default using Certbot certs

`nginx_tls_key_path: "/etc/letsencrypt/live/{{ nginx_proxy_server_name }}/privkey.pem"` — TLS key path. By default using Certbot certs

`element_enabled: false` — Install Element matrix client. It will be available at `nginx_proxy_server_name`.

`element_version: v1.7.3` — Element version that should be installed.

`element_install_path: "/var/www/element-web"` — Directory to install Element.

`element_default_hs: "{{ nginx_proxy_server_name }}"` — Default HomeServer that Element use.

`synapse_internal_ip: 127.0.0.1` — Internal address of synapse server (Upstream).

`ldap_internal_ip: 127.0.0.1` — Internal address of LDAP server (Upstream).

`LDAP_PHP_ADMIN: false` — Enable PHP LDAP Admin reverse proxy.
