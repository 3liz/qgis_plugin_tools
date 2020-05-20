__copyright__ = "Copyright 2020, 3Liz"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = "$Format:%H$"

import os

from .resources import plugin_path
from .version import format_version_integer


def available_migrations(minimum_version: int):
    """Get all the upgrade SQL files since the provided version."""
    upgrade_dir = plugin_path("install", "sql", "upgrade")
    get_files = [
        f for f in os.listdir(upgrade_dir) if os.path.isfile(os.path.join(upgrade_dir, f))
    ]
    files = []

    for f in get_files:
        k = format_version_integer(f.replace("upgrade_to_", "").replace(".sql", "").strip())
        if k > minimum_version:
            files.append([k, f])

    def getKey(item):
        return item[0]

    sfiles = sorted(files, key=getKey)
    sql_files = [s[1] for s in sfiles]
    return sql_files
