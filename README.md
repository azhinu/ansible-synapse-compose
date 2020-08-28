## Ansible playbook: Matrix-Synapse docker-compose

This playbook install Matrix-Synapse bundle with docker-compose.
Playbook contains following roles:
- Docker
- Matrix-Synaspse with PostgreSQL
- Coturn server
- OpenLDAP with phpLDAPadmin
- Nginx proxy

All roles can be applied separately.

### Coturn server

Coturn needs to allow users make calls with Element through internet. Coturn server should be available from internet. If all users will be in same private network, you shouldn't use Coturn.

To use coturn set `coturn_enabled: true`

Coturn will be installed at Nginx host.

### OpenLDAP

OpenLDAP using to manage Matrix-Synaspse users.

To use this role fill OpenLDAP vars in inventory and use `ldap_enabled: true`

### Nginx

Nginx provide a secure access to Synapse and phpLDAPadmin and Element as an option.
Nginx role can automatically obtain TLS certs with Certbot or use existing certs.

### Installation

1. Prepair your servers. Synapse, OpenLDAP and Nginx should be in a same secure network (e.g VPN). Synapse required 5432 (psql) and 8008 port available. LDAP required 381 and 8110 ports available. Nginx required 80 and 443 ports available.
2. Fill inventory, using `inventory/hosts_sample.yaml` as example. (Example inventory contains default variables.)
3. Run Ansible-Playbook with setup.yaml

All credentials will be shown after successful deployment. To run role again put creds to the inventory vars.

Run Ansible-Playbook with update.yaml to update services.
