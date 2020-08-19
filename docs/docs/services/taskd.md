# Taskd

The taskwarrior server.

## Ports

* **53589/tcp**.

## Setup

Open a shell in the container.

```bash
docker exec -it taskd /bin/sh
```

And then from inside the container run the commands from the
[taskwarrior docs](https://taskwarrior.org/docs/taskserver/user.html).

**Note**: The *pki* directory is in */var/taskd/pki/*
