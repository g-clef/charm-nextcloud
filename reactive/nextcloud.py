
from charms.reactive import when, when_not, set_flag, hook

# from charmhelpers.core import unitdata
from charmhelpers.core.hookenv import open_port, status_set, config, unit_public_ip, log
from charmhelpers.core.host import chdir
# from charmhelpers.core.host import service_restart
# from charmhelpers.core.templating import render

from pathlib import Path
import subprocess


@hook("mysql-relation-joined")
def db_ready():
    status_set("blocked", "Database joined but not configured")
    set_flag("nextcloud.db_ready")


@when('nextcloud.db_ready', 'mysql.available')
@when_not('nextcloud.initdone')
def init_nextcloud(mysql):

    status_set('maintenance', "Initializing Nextcloud")

    ctxt = {'dbname': mysql.database(),
            'dbuser': mysql.user(),
            'dbpass': mysql.password(),
            'dbhost': mysql.host(),
            'dbport': mysql.port(),
            'dbtype': 'mysql',
            'admin_username': config().get('admin-username'),
            'admin_password': config().get('admin-password'),
            'data_dir': Path('/var/www/nextcloud/data'),
            }

    nextcloud_init = ("sudo -u www-data /usr/bin/php occ  maintenance:install "
                      "--database {dbtype} --database-name {dbname} "
                      "--database-host {dbhost} --database-pass {dbpass} "
                      "--database-user {dbuser} --admin-user {admin_username} "
                      "--admin-pass {admin_password} "
                      "--data-dir {data_dir} ").format(**ctxt)

    log(nextcloud_init)

    with chdir('/var/www/nextcloud'):
        subprocess.call("sudo chown -R www-data:www-data .".split())
        subprocess.call(nextcloud_init.split())

    Path('/var/www/nextcloud/config/config.php').write_text(
        Path('/var/www/nextcloud/config/config.php').open().read().replace(
            "localhost", config().get('fqdn') or unit_public_ip()))

    set_flag('nextcloud.initdone')

    status_set('active', "Nextcloud init complete")


@when('nextcloud.initdone', 'apache.available')
@when_not('nextcloud.serviceavailable')
def server_config():

    for module in ['rewrite', 'headers', 'env', 'dir', 'mime']:
        subprocess.call(['a2enmod', module])

    open_port(port='80')

    set_flag('nextcloud.serviceavailable')

    set_flag('apache.start')

    status_set('active', "Ready")


@when_not('nextcloud.db_ready')
def blocked_on_mysql():

    status_set('blocked', "Need connection to MySQL to continue")
    return
