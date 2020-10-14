"""Base class algorithm."""

from abc import abstractmethod
from os.path import isfile

from qgis.core import Qgis, QgsProcessingAlgorithm
from qgis.PyQt.QtGui import QIcon

from .resources import resources_path


__copyright__ = "Copyright 2020, 3Liz"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = "$Format:%H$"


class BaseProcessingAlgorithm(QgsProcessingAlgorithm):

    def __init__(self):
        super().__init__()

    def createInstance(self):
        return type(self)()

    def flags(self):
        return super().flags() | QgsProcessingAlgorithm.FlagHideFromModeler

    def icon(self):
        icon = resources_path('icons', 'icon.png')
        if isfile(icon):
            return QIcon(icon)
        else:
            return super().icon()

    def parameters_help_string(self) -> str:
        """ Return a formatted help string for all parameters. """
        help_string = ''

        for param in self.parameterDefinitions():
            template = '{} : {}\n\n'
            if hasattr(param, 'tooltip_3liz'):
                info = param.tooltip_3liz
            else:
                info = ''

            if Qgis.QGIS_VERSION_INT >= 31500:
                info = param.help()

            if info:
                help_string += template.format(param.name(), info)

        return help_string

    @abstractmethod
    def shortHelpString(self):
        pass
