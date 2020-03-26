"""Base class algorithm."""

from qgis.core import QgsProcessingAlgorithm

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

    def shortHelpString(self):
        raise NotImplementedError
