"""I18n tools."""

from qgis.PyQt.QtCore import QLocale, QFileInfo
from qgis.PyQt.QtWidgets import QApplication
from qgis.core import QgsSettings

from .resources import resources_path

__copyright__ = "Copyright 2019, 3Liz"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = '$Format:%H$'


def setup_translation(file_pattern='{}.qm'):
    """Find the translation file according to locale.

    :param file_pattern: Custom file pattern to use to find QM files.
    :type file_pattern: basestring

    :return: The file path to the QM file, or None.
    :rtype: basestring
    """
    locale = QgsSettings().value('locale/userLocale', QLocale().name())

    ts_file = QFileInfo(resources_path('i18n', file_pattern.format(locale)))
    if ts_file.exists():
        return ts_file.absoluteFilePath()

    ts_file = QFileInfo(resources_path('i18n', file_pattern.format(locale[0:2])))
    if ts_file.exists():
        return ts_file.absoluteFilePath()

    return None


def tr(text, context='@Default'):
    return QApplication.translate(context, text)
