
## Ansible role: Coturn

Install coturn from system package manager and add it to firewall.

#### Role vars:

`coturn_secret: <RANDOM>` — Coturn static secret. Used by Synapse server.

`nginx_tls_cert_path: "/etc/letsencrypt/live/{{ nginx_proxy_server_name }}/fullchain.pem"` — TLS cert path. By default using Certbot certs

`nginx_tls_key_path: "/etc/letsencrypt/live/{{ nginx_proxy_server_name }}/privkey.pem"` — TLS key path. By default using Certbot certs
