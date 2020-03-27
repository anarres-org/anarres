# Murmur

[Murmur](https://wiki.mumble.info/wiki/Main_Page): Open source, low-latency,
high quality voice chat software.

## Variables

* `murmur_docker_image`: Name for the service docker image.
* `murmur_domain`: Domain/subdomain for the service.
* `murmur_port`: (Default: `64738`) Port on the host to bind the service to.
* `murmur_directory`:
   * `conf`: Path on the host for configuration files.
   * `data`: Path on the host for persistent data.
   * `log`: Path on the host for logss.

## Ports (by default)

* **64738/tcp** for the client connections.

## Configuration

Murmur is configured via [Mumble Client](https://www.mumble.info/downloads/).

1. Connect to your server.

2. Enable `Advanced options` in `Config > Settings` in the lower left corner.

3. Apply changes, close and right click on your user. Register yourself.

4. Disconnect from the server and reconnect with `SuperUser` as user and  its
password.

5. > The password is generated on the server creation. You can see it on the
logs or recreate it by deleting the database and restarting the service.

6. Now, as `SuperUser` you can create permanent channels, sub-channels and edit
ACLs.
7. Once you finish, disconnect and reconnect as your normal user.
