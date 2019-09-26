from os.path import abspath, join, pardir, dirname

from qgis.PyQt import uic


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
