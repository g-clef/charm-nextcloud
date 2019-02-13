
Nextcloud

# Overview

This is a charm to install Nextcloud (https://nextcloud.com/)

# Bugs

If you are building from sources on cosmic you may have to apply the misc/layersfix.patch to the (already built) charm before deploying.

```bash
patch -p0 < nextcloud/misc/apache-php-nameclash-fix.patch
patch -p0 < nextcloud/misc/basic-cfg-python-packages-fix.patch
```

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

Note: the charm is temporarily revoked from the charmstore until patches can be integrated in the buildsystem.

Now you can access nextcloud service at 'http://ipaddress-of-instance/'.

### Author
* Andre Ruiz <andre.ruiz (at) canonical.com>

Sources at https://github.com/token47/charm-nextcloud

