## Ansible role: Synapse with docker

This role install Synapse server with PostgreSQL.

### Role vars:
#### Install options

`services_dir: /opt/matrix` — Directory witch contains docker-compose file and services data
`start_services_after_install: true` — Start services after deploy

#### Postgres
`psql_pass: <RANDOM>` — Postgree root password. By default role generates random password and print at the end of ansible log.

`synapse_db_pass: <RANDOM>` — Postgree Synapse user password. By default role generates random password and print at the end of ansible log.

 Default synapse user and db: `synapse`

#### Synapse
```
`synapse_server_name: matrix.local` — Used in matrix users name, e.g @user:matrix.local

`synapse_registration_enabled: false` —  Allow public registration.

`synapse_create_admin_user: true` — Create user with admin privilege while deployment.

`synapse_admin_user: synapse_admin` — Admin user name

`synapse_admin_pass: <RANDOM>` — Admin user password. By default role generates random password and print at the end of ansible log.

`synapse_cleanup_enabled: true` — Enable chat history purge script. Admin user creation is required to use chat history purge script.

`synapse_clear_history_oncalendar: hourly` — Frequency of chat history purging. In Systemd OnCalendar format.

`synapse_coturn_address: ''` — Set to coturn server address. Set synapse public ip if blank.

`coturn_secret: <RANDOM>` — Coturn API secret. Random by default.

`synapse_registration_shared_secret: <RANDOM>` — Key used to register when public registration is disabled. Random by default.

`synapse_macaroon_secret_key: <RANDOM>` — Random by default

`synapse_form_secret: <RANDOM>` — Random by default
```

#### LDAP

`synapse_ldap_enabled: true` — Use LDAP instead of local password storage.

`synapse_ldap_server: matrix.local:389` — LDAP server address and port.

`synapse_ldap_base: dc=matrix` — LDAP domain

`synapse_ldap_bind_dn: cn=admin,dc=matrix` — Bind user

`synapse_ldap_bind_pass: "{{LDAP_ADMIN_PASSWORD}}"` — Bind password. By default using admin password from LDAP role.
