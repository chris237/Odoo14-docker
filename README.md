# Usage

Change the folder permission to make sure that the container is able to access the directory:
```
$ sudo chmod -R 777 addons
$ sudo chmod -R 777 etc
```

Start the container:
```
$ docker-compose up
```

* Then locate `localhost:8070` to access Odoo 14.0. If you want to start the server with a different port, change **8070** to another value:

```
ports:
 - "8070:8069"
```

* Log file is printed @ **etc/odoo-server.log**

To run in detached mode, execute this command:

```
$ docker-compose up -d
```

# Custom addons

The **addons** folder contains custom addons. Just put your custom addons if you have any.

# Odoo configuration

To change Odoo configuration, edit file: **etc/odoo.conf**.

# docker-compose.yml

* odoo:14.0
* postgres:10

# Screenshots

![odoo-14-welcome-docker](screenshots/odoo-14-welcome-screenshot.png)

![odoo-14-apps-docker](screenshots/odoo-14-apps-screenshot.png)
