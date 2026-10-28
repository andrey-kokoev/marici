"""Classical Hales--Jewett word search and exact labelled lattice projection.

Finite resource refusals are not Ramsey counterexamples. None limits select
an idealized unbounded search, whose mathematical termination uses HJ.
"""
from itertools import product
from research.voevodsky.ramsey_certificate import integer, labelled, keys, point, region_size, require, verify


class ForcingResourceError(RuntimeError):
    pass


def power(base, exponent, limit):
    if limit is not None:
        integer(limit, 1, 'resource_limit')
        if base > 1 and exponent > limit.bit_length():
            raise ForcingResourceError('enumeration budget exceeded')
    value = base ** exponent
    if limit is not None and value > limit:
        raise ForcingResourceError('enumeration budget exceeded')
    return value


def words_and_lines(k, n, max_words=10000, max_templates=100000):
    integer(k, 1, 'alphabet_size')
    integer(n, 1, 'word_length')
    power(k, n, max_words)
    power(k + 1, n, max_templates)
    words = list(product(range(k), repeat=n))
    indices = {word: i for i, word in enumerate(words)}
    lines = []
    for pattern in product(range(k + 1), repeat=n):
        if k not in pattern:
            continue
        line = tuple(indices[tuple(letter if x == k else x for x in pattern)] for letter in range(k))
        lines.append((tuple(None if x == k else x for x in pattern), line))
    return words, lines


def certify_word_length(k, r, n, max_colorings=100000, max_words=10000, max_templates=100000):
    """Exhaust all word colorings, or return an explicit avoiding coloring.

    Resource limits are checked before enumeration, never reported as failure
    of the mathematical forcing property.
    """
    integer(k, 1, 'alphabet_size')
    integer(r, 1, 'color_count')
    integer(n, 1, 'word_length')
    word_count = power(k, n, max_words)
    color_count = power(r, word_count, max_colorings)
    words, lines = words_and_lines(k, n, max_words, max_templates)
    checked = 0
    for coloring in product(range(r), repeat=word_count):
        checked += 1
        if not any(all(coloring[i] == coloring[line[0]] for i in line) for _, line in lines):
            return {'k': k, 'r': r, 'n': n, 'forces': False,
                    'tested_colorings': checked, 'counterexample': list(coloring)}
    assert checked == color_count
    return {'k': k, 'r': r, 'n': n, 'forces': True, 'tested_colorings': checked,
            'line_templates': len(lines)}


def search_word_length(k, r, **limits):
    """Increasing finite tests; termination without resource caps uses classical HJ."""
    integer(k, 1, 'alphabet_size')
    integer(r, 1, 'color_count')
    n = 1
    while True:
        result = certify_word_length(k, r, n, **limits)
        if result['forces']:
            return result
        n += 1


def forcing_bound(pattern, r, **limits):
    """A computably specified bound, with proved trivial/binary shortcuts.

    For >=3 letters and >=2 colors, practical budgets can refuse before the
    HJ length is reached. No numeric radius is then returned.
    """
    points = list(labelled(pattern, 'pattern').values())
    integer(r, 1, 'color_count')
    k = len(points)
    radius = max(abs(x) for p in points for x in p)
    if k == 1 or r == 1:
        n, method = 1, 'singleton-or-one-color'
        certification = None
    elif k == 2:
        n, method = r, 'binary-maximal-chain'
        certification = None
    else:
        certification = search_word_length(k, r, **limits)
        n, method = certification['n'], 'exhaustive-word-forcing'
    return {'B': n * radius, 'n': n, 'M': radius, 'k': k, 'r': r,
            'method': method, 'word_length_certification': certification}


def find_certificate(instance, n, max_words=10000, max_templates=100000):
    """Find a word-line witness in a complete lattice coloring, or return None.

    None excludes word lines only at this tested length, not other lattice
    copies, larger lengths or Ramsey existence. The entire word cube must fit.
    """
    keys(instance, ('N', 'r', 'pattern', 'coloring'), 'instance')
    radius = integer(instance['N'], 0, 'N')
    r = integer(instance['r'], 1, 'r')
    alphabet = list(labelled(instance['pattern'], 'pattern').values())
    require(type(instance['coloring']) is list, 'coloring.list')
    colors = {}
    for row in instance['coloring']:
        keys(row, ('point', 'color'), 'coloring.record')
        p = point(row['point'], 'coloring')
        require(all(abs(x) <= radius for x in p), 'coloring.outside_region')
        require(p not in colors, 'coloring.duplicate_point')
        q = integer(row['color'], 0, 'coloring.color')
        require(q < r, 'coloring.color_range')
        colors[p] = q
    require(len(colors) == region_size(radius), 'coloring.incomplete_domain')
    words, lines = words_and_lines(len(alphabet), n, max_words, max_templates)
    images = [tuple(sum(alphabet[letter][j] for letter in word) for j in range(3)) for word in words]
    require(all(p in colors for p in images), 'word_cube.outside_region')
    pulled = [colors[p] for p in images]
    for template, line in lines:
        q = pulled[line[0]]
        if all(pulled[i] == q for i in line):
            return line_certificate(instance, list(template), q)
    return None


def line_certificate(instance, word_pattern, color):
    """Project a supplied homogeneous word line and independently verify its image.

    The alphabet is the supplied pattern-record order; None is a variable
    position, and every variable receives the same selected alphabet letter.
    """
    points = labelled(instance['pattern'], 'pattern')
    alphabet = list(points.values())
    if type(word_pattern) is not list or not word_pattern:
        raise ValueError('nonempty word pattern required')
    a, m = [0, 0, 0], 0
    for letter in word_pattern:
        if letter is None:
            m += 1
        else:
            integer(letter, 0, 'fixed_letter')
            if letter >= len(alphabet):
                raise ValueError('fixed letter outside alphabet')
            for j in range(3):
                a[j] += alphabet[letter][j]
    if not m:
        raise ValueError('at least one variable position required')
    certificate = {'a': a, 'm': m, 'color': color,
                   'image': [{'label': label, 'point': [a[j] + m * s[j] for j in range(3)]}
                             for label, s in points.items()]}
    verify(instance, certificate)
    return {'certificate': certificate, 'word_pattern': list(word_pattern),
            'variable_positions': [i for i, letter in enumerate(word_pattern) if letter is None],
            'alphabet_labels': list(points)}
