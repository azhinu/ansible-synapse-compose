
## Ansible role: LDAP

This role based on osixia/openldap docker image.

More info can be found here: https://github.com/osixia/docker-openldap#administrate-your-ldap-server

###Role vars:

`services_dir: /opt/matrix` — This directory will be used to place `/ldap/docker-compose.yaml` file.

`LDAP_PHP_ADMIN: True` — Deploy LDAP PHP Admin.

`LDAP_ORGANISATION: "Matrix-Synapse"` — LDAP Organisation.

`LDAP_DOMAIN: "matrix"` — LDAP DN.

`LDAP_ADMIN_PASSWORD: <RANDOM>` — LDAP Admin user password. Random by default.

All credentials will be shown as debug msg after deployment.
