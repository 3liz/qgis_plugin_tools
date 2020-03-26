from qgis.core import QgsProcessingFeedback

from .custom_logging import setup_logger, plugin_name

__copyright__ = "Copyright 2019, 3Liz"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = "$Format:%H$"

LOGGER = setup_logger(plugin_name())


class LoggerProcessingFeedBack(QgsProcessingFeedback):
    def __init__(self, use_logger=True):
        super().__init__()
        self._last = None
        self.use_logger = use_logger
        self.last_progress_text = None
        self.last_push_info = None
        self.last_command_info = None
        self.last_debug_info = None
        self.last_console_info = None
        self.last_report_error = None

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, text):
        self._last = text

    def setProgressText(self, text):
        self._last = text
        self.last_progress_text = text
        if self.use_logger:
            LOGGER.info(text)

    def pushInfo(self, text):
        self._last = text
        self.last_push_info = text
        if self.use_logger:
            LOGGER.info(text)

    def pushCommandInfo(self, text):
        self._last = text
        self.last_command_info = text
        if self.use_logger:
            LOGGER.info(text)

    def pushDebugInfo(self, text):
        self._last = text
        self.last_debug_info = text
        if self.use_logger:
            LOGGER.warning(text)

    def pushConsoleInfo(self, text):
        self._last = text
        self.last_console_info = text
        if self.use_logger:
            LOGGER.info(text)

    def reportError(self, text, fatalError=False):
        self._last = text
        self.last_report_error = text
        if self.use_logger:
            LOGGER.critical(text)
