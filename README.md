## Ansible playbook: Matrix-Synapse docker-compose

This role install Matrix-Synapse bundle with docker-compose.

### Bundle contains
- Synapse
- PostgreSQL
- Coturn
- ma1sd
- Riot-web
- Nginx


### Installation

1. Add hosts to inventory/hosts file
2. Edit vars in inventory/hosts_vars/'host name'/vars.yml
3. Run 

	    ansible-playbook -i inventory/hosts setup.yml

All credentials will be showen after successful deployment. To run role again put creds to the inventory vars.

### External coturn serve r

This playbook can install dedicated coturn server. Set [coturn_servers] in 'hosts' file and 'coturn_enabled' to 'false' to setup dedicated coturn server. 
