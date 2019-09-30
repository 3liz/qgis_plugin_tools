"""I18n tools."""

from qgis.core import QgsSettings
from qgis.PyQt.QtCore import QLocale, QTranslator, QFileInfo, QCoreApplication
from qgis.PyQt.QtWidgets import QApplication

from .resources import resources_path

__copyright__ = "Copyright 2019, 3Liz"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = '$Format:%H$'


def setup_translation():

    locale = QgsSettings().value('locale/userLocale', QLocale().name())

    ts_file = QFileInfo(resources_path('i18n', '{}.qm'.format(locale)))
    if ts_file.exists():
        return ts_file.absoluteFilePath()

    ts_file = QFileInfo(resources_path('i18n', '{}.qm'.format(locale[0:2])))
    if ts_file.exists():
        return ts_file.absoluteFilePath()

    return None


def tr(text, context='@Default'):
    return QApplication.translate(context, text)
