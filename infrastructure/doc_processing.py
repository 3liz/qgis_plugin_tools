#!/usr/bin/env python3
from os.path import join, basename, dirname

from qgis.core import QgsProcessingParameterDefinition
from qgis.PyQt.QtCore import QRect, QPoint, QSize
from processing import createAlgorithmDialog

from qgis.utils import plugins

plugin_name = basename(dirname(dirname(dirname(__file__))))
provider = plugins[plugin_name].provider


PATH = '/processing'

TEMPLATE = '''---
Title: {title}
Favicon: ../icon.png
...

[TOC]

# {title}
'''

TEMPLATE_GROUP = '''
## {group}

'''

TEMPLATE_ALGORITHM = '''
### {title}

{help_string}

![algo_id]({img})

#### Parameters

| ID | Description | Type | Info | Required | Advanced |
|:-:|:-:|:-:|:-:|:-:|:-:|
{parameters}

#### Outputs

| ID | Description | Type | Info |
|:-:|:-:|:-:|:-:|
{outputs}

***

'''

TEMPLATE_PARAMETERS = '{id}|{description}|{type}|{info}|{required}|{advanced}|\n'

TEMPLATE_OUTPUT = '{id}|{description}|{type}|{info}|\n'


def format_type(class_name):
    class_name = class_name.replace('QgsProcessingParameter', '')
    class_name = class_name.replace('QgsProcessingOutput', '')
    return class_name


def generate_processing_doc():
    global TEMPLATE

    markdown_all = TEMPLATE.format(title=provider.name())
    algorithms_markdown = {}

    for alg in provider.algorithms():

        output_screen = join(PATH, '{}.png'.format(alg.id().replace(':', '-')))
        r = createAlgorithmDialog(alg.id())
        r.resize(1100, 800)
        screen = r.grab(QRect(QPoint(0, 0), QSize(-1, -1)))
        screen.save(output_screen)

        param_markdown = ''
        for param in alg.parameterDefinitions():
            if hasattr(param, 'tooltip_3liz'):
                info = param.tooltip_3liz
            else:
                info = ''
            param_markdown += TEMPLATE_PARAMETERS.format(
                id=param.name(),
                type=format_type(param.__class__.__name__),
                description=param.description(),
                info=info,
                required='' if param.flags() & QgsProcessingParameterDefinition.FlagOptional else '✓',
                advanced='✓' if param.flags() & QgsProcessingParameterDefinition.FlagAdvanced else ''
            )

        output_markdown = ''
        for output in alg.outputDefinitions():
            if hasattr(output, 'tooltip_3liz'):
                info = output.tooltip_3liz
            else:
                info = ''
            output_markdown += TEMPLATE_OUTPUT.format(
                id=output.name(),
                type=format_type(output.__class__.__name__),
                description=output.description(),
                info=info,
            )

        markdown = TEMPLATE_ALGORITHM.format(
            title=alg.displayName(),
            help_string=alg.shortHelpString(),
            parameters=param_markdown,
            outputs=output_markdown,
            img='./{}'.format(basename(output_screen)),
            algo_id=alg.id(),
        )

        if alg.group() not in algorithms_markdown.keys():
            algorithms_markdown[alg.group()] = []

        algorithms_markdown[alg.group()].append(markdown)

    for group in algorithms_markdown.keys():
        markdown_all += TEMPLATE_GROUP.format(group=group)
        for alg in algorithms_markdown[group]:
            markdown_all += alg

    output_file = join(PATH, 'README.md')
    text_file = open(output_file, "w+")
    text_file.write(markdown_all)
    text_file.close()


generate_processing_doc()
