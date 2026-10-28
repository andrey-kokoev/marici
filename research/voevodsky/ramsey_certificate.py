"""Exact finite vertex-coloring certificates on the candidate even-sum lattice.

This verifies a supplied witness. It neither searches for one nor admits a
native Marici source/history. Only ordinary JSON-shaped built-in values enter
this interface; booleans are not integers here.
"""


class CertificateError(ValueError):
    """An input or certificate violates the declared finite interface."""


def require(condition, reason):
    if not condition:
        raise CertificateError(reason)


def keys(value, expected, name):
    require(type(value) is dict and set(value) == set(expected), name + '.keys')


def integer(value, minimum, name):
    require(type(value) is int and value >= minimum, name + '.integer')
    return value


def point(value, name):
    require(type(value) is list and len(value) == 3, name + '.triple')
    require(all(type(x) is int for x in value), name + '.integer_coordinates')
    require(sum(value) % 2 == 0, name + '.lattice')
    return tuple(value)


def labelled(records, name):
    require(type(records) is list and bool(records), name + '.nonempty_list')
    result, used = {}, set()
    for record in records:
        keys(record, ('label', 'point'), name + '.record')
        label = record['label']
        require(type(label) is str and bool(label), name + '.label')
        require(label not in result, name + '.duplicate_label')
        p = point(record['point'], name)
        require(p not in used, name + '.duplicate_point')
        result[label] = p
        used.add(p)
    return result


def region_size(n):
    """Number of even-sum integer triples in [-n,n]^3, for n >= 0."""
    integer(n, 0, 'N')
    return ((2 * n + 1) ** 3 + (-1) ** n) // 2


def verify(instance, certificate):
    """Return True exactly for valid complete-domain homogeneous-copy records.

    Raise CertificateError on any malformed/invalid input. Coordinates and
    scales use exact Python integers; no numeric tolerances or float coercion.
    Template and image order may differ, but labels must agree exactly.
    """
    keys(instance, ('N', 'r', 'pattern', 'coloring'), 'instance')
    n = integer(instance['N'], 0, 'N')
    r = integer(instance['r'], 1, 'r')
    pattern = labelled(instance['pattern'], 'pattern')
    records = instance['coloring']
    require(type(records) is list, 'coloring.list')
    colors = {}
    for record in records:
        keys(record, ('point', 'color'), 'coloring.record')
        p = point(record['point'], 'coloring')
        require(all(abs(x) <= n for x in p), 'coloring.outside_region')
        require(p not in colors, 'coloring.duplicate_point')
        color = integer(record['color'], 0, 'coloring.color')
        require(color < r, 'coloring.color_range')
        colors[p] = color
    # All entries are distinct members of L_N. Equal finite cardinality is
    # therefore equivalent to completeness; no enormous region enumeration.
    require(len(colors) == region_size(n), 'coloring.incomplete_domain')

    keys(certificate, ('a', 'm', 'color', 'image'), 'certificate')
    a = point(certificate['a'], 'translation')
    m = integer(certificate['m'], 1, 'scale')
    q = integer(certificate['color'], 0, 'certificate.color')
    require(q < r, 'certificate.color_range')
    image = labelled(certificate['image'], 'image')
    require(set(image) == set(pattern), 'image.labels')
    for label, s in pattern.items():
        expected = tuple(a[j] + m * s[j] for j in range(3))
        require(image[label] == expected, 'image.not_declared_homothety')
        require(expected in colors, 'image.outside_region')
        require(colors[expected] == q, 'image.not_monochromatic')
    return True
