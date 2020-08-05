## Ansible playbook: Matrix-Synapse docker-compose

This playbook install Matrix-Synapse bundle with docker-compose.
Playbook contains following roles:
- Docker
- Matrix-Synaspse bundle
- Coturn server
- OpenLDAP with phpLDAPadmin
- Nginx proxy

All roles can be applied separately.

### Matrix-Synapse bundle contains
- Synapse
- PostgreSQL
- Coturn
- Element-web
- Nginx

By default Matrix-Synapse bundle installs PostgreSQL, Synapse and Nginx without TLS.

To install this role fill Matrix-Synapse server vars in inventory.

By design this role should be applied to server in local network with local domain.

### Coturn server

Coturn needs to allow users make calls with Matrix-Synapse. Coturn server should be available from internet.

To user Coturn server role you need to fill Coturn vars in inventory.

### OpenLDAP

OpenLDAP using to manage Matrix-Synaspse users.

By design this service should be installed at Matrix-Synapse bundle server.

To use this role fill OpenLDAP vars in inventory.

### Nginx nginx

Nginx proxy is the entry point of Matrix-Synapse. This role should be applied to the server that available from internet. To apply this role enter public address of Matrix-Synapse server to inventory.

### Installation

If you will use Wireguard, apply it first:

1. Edit inventory/hosts-wg-sample.yaml
2. run

		ansible-playbook -i inventory/hosts-wg-sample.yaml setup_wg.yaml  --ask-become-pass

Then apply Matrix-Synapse

1. Add hosts to inventory/hosts file
2. Edit vars in inventory/hosts file
3. Run

	    ansible-playbook -i inventory/hosts.yaml setup.yaml --ask-become-pass

All credentials will be shown after successful deployment. To run role again put creds to the inventory vars.
