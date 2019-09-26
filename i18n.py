"""I18n tools."""

from qgis.PyQt.QtWidgets import QApplication

__copyright__ = "Copyright 2019, 3Liz"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = '$Format:%H$'


def tr(text, context='@Default'):
    return QApplication.translate(context, text)
