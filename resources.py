"""Tools to work with resource files."""

import configparser
from os.path import abspath, join, pardir, dirname

from qgis.PyQt import uic

__copyright__ = "Copyright 2019, 3Liz"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = '$Format:%H$'


def plugin_name():
    """Return the plugin name according to metadata.txt.

    :return: The plugin name.
    :rtype: basestring
    """
    metadata = metadata_config()
    name = metadata['general']['name']
    return name


def metadata_config():
    """Get the INI config parser for the metadata file.

    :return: The config parser object.
    :rtype: configparser
    """
    path = dirname(__file__)
    path = abspath(abspath(join(path, pardir, 'metadata.txt')))
    config = configparser.ConfigParser()
    config.read(path)
    return config


def plugin_test_data_path(*args):
    """Get the path to the plugin test data path.

    :param args List of path elements e.g. ['img', 'logos', 'image.png']
    :type args: str

    :return: Absolute path to the resources folder.
    :rtype: str
    """
    path = dirname(__file__)
    path = abspath(abspath(join(path, pardir, 'test', 'data')))
    for item in args:
        path = abspath(join(path, item))

    return path


def resources_path(*args):
    """Get the path to our resources folder.

    :param args List of path elements e.g. ['img', 'logos', 'image.png']
    :type args: str

    :return: Absolute path to the resources folder.
    :rtype: str
    """
    path = dirname(__file__)
    path = abspath(abspath(join(path, pardir, 'resources')))
    for item in args:
        path = abspath(join(path, item))

    return path


def load_ui(*args):
    """Get compile UI file.

    :param args List of path elements e.g. ['img', 'logos', 'image.png']
    :type args: str

    :return: Compiled UI file.
    """
    ui_class, _ = uic.loadUiType(resources_path('ui', *args))
    return ui_class
