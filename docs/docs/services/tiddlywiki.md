# TiddlyWiki

[TiddlyWiki](https://tiddlywiki.com/) A non-linear personal web notebook.

## Variables

* `tiddlywiki_docker_image`: Name for the service docker image.
* `tiddlywiki_internal_web_port`: (Default: `3090`) Port on the host to bind the
   service to.
* `tiddlywiki_domain`: Domain/subdomain for the service.
* `tiddlywiki_user`: (Default: `tiddlywiki`) Default user for the web service.
* `tiddlywiki_pass`: Password for that user.
* `tiddlywiki_directory`:
   * `data`: Path on the host for the persistent data directory.

## Setup

1. Set, at least, the undefined variables and deploy the service.

   The data directory can be set to a `syncthing` folder for syncing it with
   other devices.
1. Optionally, modify the configuration file *mywiki/tiddlywiki.info*, where
   you can add plugins if needed.
