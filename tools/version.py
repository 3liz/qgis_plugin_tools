"""Tools about version."""

from .resources import metadata_config


def format_version_integer(version_string: str):
    """Transform version string to integers to allow comparing versions.

    Transform "0.1.2" into "000102"
    Transform "10.9.12" into "100912"
    """
    return int(''.join([a.zfill(2) for a in version_string.strip().split('.')]))


def version() -> str:
    """Return the version defined in metadata.txt."""
    return metadata_config()['general']['version']


def is_dev_version() -> bool:
    """Return if the plugin is in a dev version."""
    is_dev = version().find('-beta') != -1
    return is_dev
