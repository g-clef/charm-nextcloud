
Nextcloud

# Overview

This is a charm to install Nextcloud (https://nextcloud.com/)

# Bugs

On cosmic you may have to apply the misc/layersfix.patch to the (already built) charm before deploying.

# Usage

If you are building the charm from source:

```bash

charm build

```

If you are deplying it locally:

```bash

juju deploy /tmp/charm-builds/nextcloud

juju deploy mysql

juju relate mysql nextcloud

```

If you are deploying from the charmstore:


```bash
juju deploy cs:~andre-ruiz/nextcloud

juju deploy mysql

juju relate mysql nextcloud
```

Now you can access nextcloud service at 'http://<ipaddress-of-owncloud-instance>/'.

### Author
* Andre Ruiz <andre.ruiz (at) canonical.com>

