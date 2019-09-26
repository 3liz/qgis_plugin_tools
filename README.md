## QGIS Plugin core tools

### How to use it

The module is helping you with:
* fetching resources in `resources` folder
* fetching compiled UI file in `resources/ui` folder
* translate using the `i18n.tr` function.

To use the logging system:
```python
import logging
from .qgis_plugin_tools.resources import plugin_name

# Top of the file
LOGGER = logging.getLogger(plugin_name())

# Later in the code
LOGGER.error('Log an error here')
LOGGER.warning('Log a warning here')
LOGGER.critical('Log a critical error here')
LOGGER.info('Log some info here')
```

### How to install it in an existing plugin

* Go to the root folder of your plugin
* `git submodule add git@github.com:3liz/qgis_plugin_tools.git`
* Update the makefile to use `git-archive-all`

For setting up the logging:
```python
from .qgis_plugin_tools.resources import plugin_name
from .qgis_plugin_tools.custom_logging import setup_logger

setup_logger(plugin_name())
```