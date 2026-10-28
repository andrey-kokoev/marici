"""Covariance of framed mathematical certificates, not native particle histories."""
from copy import deepcopy
from research.voevodsky.ramsey_certificate import keys, point, require, verify


def matrix(q):
    require(type(q) is list and len(q) == 3, 'matrix.shape')
    require(all(type(row) is list and len(row) == 3 for row in q), 'matrix.shape')
    require(all(type(x) is int and x in (-1, 0, 1) for row in q for x in row), 'matrix.entries')
    require(all(sum(abs(x) for x in row) == 1 for row in q), 'matrix.rows')
    require(all(sum(abs(q[i][j]) for i in range(3)) == 1 for j in range(3)), 'matrix.columns')
    return q


def vector(q, v):
    return [sum(q[i][j] * v[j] for j in range(3)) for i in range(3)]


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def transformation(q, b, colors):
    matrix(q)
    point(b, 'map.translation')
    require(type(colors) is list and bool(colors), 'color_permutation.list')
    require(all(type(x) is int and 0 <= x < len(colors) for x in colors), 'color_permutation.range')
    require(len(set(colors)) == len(colors), 'color_permutation.bijection')
    return {'Q': deepcopy(q), 'b': list(b), 'colors': list(colors)}


def checked_map(g):
    keys(g, ('Q', 'b', 'colors'), 'map')
    return transformation(g['Q'], g['b'], g['colors'])


def check_reference(ref):
    if ref is None:
        return
    keys(ref, ('label', 'point', 'direction'), 'reference')
    require(type(ref['label']) is str and bool(ref['label']), 'reference.label')
    point(ref['point'], 'reference.point')
    if ref['direction'] is not None:
        direction = point(ref['direction'], 'reference.direction')
        require(any(direction), 'reference.zero_direction')


def verify_framed(instance, certificate):
    """Validate a global-coordinate certificate in an L-centered integer box.

    Pattern coordinates remain global. Only the colored region, witness image
    and translation parameter are recentered for the existing strict verifier.
    """
    keys(instance, ('N', 'r', 'center', 'pattern', 'coloring', 'reference'), 'framed_instance')
    center = point(instance['center'], 'region.center')
    check_reference(instance['reference'])
    keys(certificate, ('a', 'm', 'color', 'image'), 'certificate')
    require(type(instance['coloring']) is list, 'coloring.list')
    require(type(certificate['image']) is list, 'image.list')
    colors, images = [], []
    for row in instance['coloring']:
        keys(row, ('point', 'color'), 'coloring.record')
        p = point(row['point'], 'coloring')
        colors.append({'point': [p[j] - center[j] for j in range(3)], 'color': row['color']})
    for row in certificate['image']:
        keys(row, ('label', 'point'), 'image.record')
        p = point(row['point'], 'image')
        images.append({'label': row['label'], 'point': [p[j] - center[j] for j in range(3)]})
    a = point(certificate['a'], 'translation')
    local = {'N': instance['N'], 'r': instance['r'], 'pattern': deepcopy(instance['pattern']), 'coloring': colors}
    witness = {'a': [a[j] - center[j] for j in range(3)], 'm': certificate['m'],
               'color': certificate['color'], 'image': images}
    return verify(local, witness)


def transport(instance, certificate, g):
    verify_framed(instance, certificate)
    g = checked_map(g)
    require(len(g['colors']) == instance['r'], 'color_permutation.size')
    q, b, colors = g['Q'], g['b'], g['colors']
    move = lambda p: add(vector(q, p), b)
    target = {'N': instance['N'], 'r': instance['r'], 'center': move(instance['center']),
              'pattern': [{'label': row['label'], 'point': move(row['point'])} for row in instance['pattern']],
              'coloring': [{'point': move(row['point']), 'color': colors[row['color']]} for row in instance['coloring']],
              'reference': deepcopy(instance['reference'])}
    if target['reference'] is not None:
        target['reference']['point'] = move(instance['reference']['point'])
        if target['reference']['direction'] is not None:
            target['reference']['direction'] = vector(q, instance['reference']['direction'])
    m = certificate['m']
    # Template points also move by b, so the offset is NOT the point g(a).
    witness = {'a': add(vector(q, certificate['a']), [(1 - m) * x for x in b]),
               'm': m, 'color': colors[certificate['color']],
               'image': [{'label': row['label'], 'point': move(row['point'])} for row in certificate['image']]}
    verify_framed(target, witness)
    return target, witness


def check_transport(instance, certificate, g, moved_instance, moved_certificate):
    expected_instance, expected_certificate = transport(instance, certificate, g)
    require(moved_instance == expected_instance, 'transport.instance_or_reference_mismatch')
    require(moved_certificate == expected_certificate, 'transport.certificate_mismatch')
    return verify_framed(moved_instance, moved_certificate)


def compose(outer, inner):
    outer, inner = checked_map(outer), checked_map(inner)
    require(len(outer['colors']) == len(inner['colors']), 'composition.color_size')
    q = [[sum(outer['Q'][i][k] * inner['Q'][k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    b = add(vector(outer['Q'], inner['b']), outer['b'])
    colors = [outer['colors'][x] for x in inner['colors']]
    return transformation(q, b, colors)


def inverse(g):
    g = checked_map(g)
    q = [[g['Q'][j][i] for j in range(3)] for i in range(3)]
    b = [-x for x in vector(q, g['b'])]
    colors = [0] * len(g['colors'])
    for i, image in enumerate(g['colors']):
        colors[image] = i
    return transformation(q, b, colors)
