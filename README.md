# qgis_plugin_tools

Core tools for some QGIS plugins

## How to use it

The module is helping you with:
* fetching resources in `resources` folder
* fetching compiled UI file in `resources/ui` folder

## How to install it in an existing plugin

* Go to the root folder of your plugin
* `git submodule add git@github.com:3liz/qgis_plugin_tools.git`
* Update the makefile to use `git-archive-all`
