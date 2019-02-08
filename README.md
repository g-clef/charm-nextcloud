
Nextcloud

# Overview

This is a charm to install Nextcloud (https://nextcloud.com/)

# Bugs

On cosmic you may have to apply the misc/layersfix.patch to the (already built) charm before deploying.

# Usage

```bash
juju deploy nextcloud

juju deploy mysql

juju relate mysql nextcloud

juju expose nextcloud
```

Now you can access nextcloud service at 'http://<ipaddress-of-owncloud-instance>/'.

### Author
* Andre Ruiz <andre.ruiz (at) canonical.com>

