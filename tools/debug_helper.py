from qgis.core import QgsFeatureRequest, QgsWkbTypes


def pretty_table(iterable, header):
    """Copy/paste from http://stackoverflow.com/a/40426743/2395485"""
    max_len = [len(x) for x in header]
    for row in iterable:
        row = [row] if type(row) not in (list, tuple) else row
        for index, col in enumerate(row):
            if max_len[index] < len(str(col)):
                max_len[index] = len(str(col))
    output = '-' * (sum(max_len) + 1) + '\n'
    output += '|' + ''.join(
        [h + ' ' * (l - len(h)) + '|' for h, l in zip(header, max_len)]) + '\n'
    output += '-' * (sum(max_len) + 1) + '\n'
    for row in iterable:
        row = [row] if type(row) not in (list, tuple) else row
        output += '|' + ''.join(
            [
                str(c) + ' ' * (
                    l - len(str(c))) + '|' for c, l in zip(
                    row, max_len)]) + '\n'
    output += '-' * (sum(max_len) + 1) + '\n'
    return output


def print_attribute_table(layer, limit=-1):
    """Print the attribute table in the console.

    :param layer: The layer to print.
    :type layer: QgsVectorLayer
    :param limit: The limit in the query.
    :type limit: integer
    """
    if layer.wkbType() in [QgsWkbTypes.NullGeometry,
                           QgsWkbTypes.UnknownGeometry]:
        geometry = False
    else:
        geometry = True

    headers = []
    if geometry:
        headers.append('geom')
    headers.extend(
        [f.name() + ' : ' + str(f.type()) for f in layer.fields().toList()])

    request = QgsFeatureRequest()
    request.setLimit(limit)
    data = []
    for feature in layer.getFeatures(request):
        attributes = []
        if geometry:
            attributes.append(feature.geometry().type())
        attributes.extend(feature.attributes())
        data.append(attributes)

    print((pretty_table(data, headers)))
