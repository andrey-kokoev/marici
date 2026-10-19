"""Exact global port-binding screen and faithful indexed direct-sum package.

No cross-source relation or physical common witness is invented.
"""
from itertools import product
from fractions import Fraction as F
from exchange_source_bridge import identity, zeros, add, scale, mul, transpose, block_diagonal, source_model, outer
from pilot_carrier import Operation, native_permutation


def nullspace(rows):
    a = [[F(value) for value in row] for row in rows]
    columns = len(a[0]) if a else 0
    pivots = []
    for column in range(columns):
        found = next((r for r in range(len(pivots), len(a)) if a[r][column]), None)
        if found is None:
            continue
        row = len(pivots)
        a[row], a[found] = a[found], a[row]
        divisor = a[row][column]
        a[row] = [value / divisor for value in a[row]]
        for r in range(len(a)):
            if r != row and a[r][column]:
                factor = a[r][column]
                a[r] = [value - factor * known for value, known in zip(a[r], a[row])]
        pivots.append(column)
        if len(pivots) == len(a):
            break
    result = []
    for free in range(columns):
        if free in pivots:
            continue
        vector = [F(0)] * columns
        vector[free] = F(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -a[row][free]
        result.append(vector)
    return result


def native_characters():
    return {(left, right): [F((left if i // 2 else 1) * (right if i % 2 else 1)) for i in range(4)]
            for left, right in product((-1, 1), repeat=2)}


def joint_target_space(a, b, signs):
    first = add(a, scale(-signs[0], identity(len(a))))
    second = add(b, scale(-signs[1], identity(len(b))))
    return nullspace(first + second)


def fixed_port_bindings():
    model = source_model()
    characters = native_characters()
    pl = [list(row) for row in native_permutation(Operation.LEFT)]
    pr = [list(row) for row in native_permutation(Operation.RIGHT)]
    reports = []
    for label_a, label_b in product(model['labels'], repeat=2):
        a, b = model['reduced'][label_a], model['reduced'][label_b]
        spaces = {signs: joint_target_space(a, b, signs) for signs in characters}
        for signs, vectors in spaces.items():
            for vector in vectors:
                # A complete source character basis determines every L.
                # These basis maps witness T_a L=L P_L and T_b L=L P_R.
                l = scale(F(1, 4), outer(vector, characters[signs]))
                if mul(a, l) != mul(l, pl) or mul(b, l) != mul(l, pr):
                    raise ValueError('global intertwiner basis identity failed')
        active = [signs for signs, vectors in spaces.items() if vectors]
        if label_a != label_b:
            if active != [(1, 1)] or len(spaces[(1, 1)]) != 4:
                raise ValueError('distinct-port eigenspace structure changed')
            rank_cap = 1
        else:
            if set(active) != {(-1, -1), (1, 1)} or len(spaces[(-1, -1)]) != 1 or len(spaces[(1, 1)]) != 5:
                raise ValueError('same-port eigenspace structure changed')
            rank_cap = 2
        reports.append({'ports': [label_a, label_b], 'mismatch_intertwiner_space_dimension': sum(map(len, spaces.values())),
                        'full_anchor_plus_mismatch_intertwiner_space_dimension': 16 + sum(map(len, spaces.values())),
                        'maximum_map_rank': rank_cap, 'faithful_four_dimensional_map': False})
    return reports


def bounded_typed_loop_screen(max_length=12):
    if type(max_length) is not int or not 1 <= max_length <= 12:
        raise ValueError('declared loop horizon must be between one and twelve')
    model = source_model()
    vertices = sorted({vertex for pair in model['ports'].values() for vertex in pair})
    counts = {vertex: {} for vertex in vertices}
    negative_dimensions = {}

    def visit(start, current, word, operator):
        if word and current == start:
            dimension = len(nullspace(add(operator, identity(6))))
            negative_dimensions[dimension] = negative_dimensions.get(dimension, 0) + 1
            counts[start][len(word)] = counts[start].get(len(word), 0) + 1
        if len(word) == max_length:
            return
        for label, (source, target) in model['ports'].items():
            if source == current:
                visit(start, target, word + (label,), mul(model['reduced'][label], operator))

    for vertex in vertices:
        visit(vertex, vertex, (), identity(6))
    return {'maximum_word_length': max_length, 'base_vertices': vertices,
            'closed_nonempty_word_count': sum(negative_dimensions.values()),
            'counts_by_base_vertex_and_length': {vertex: {str(length): count for length, count in sorted(rows.items())}
                                                for vertex, rows in counts.items()},
            'negative_eigenspace_dimension_counts': {str(dimension): count for dimension, count in sorted(negative_dimensions.items())},
            'minimum_negative_dimension_needed_for_native_flip': 2,
            'faithful_fixed_fibre_native_flip_candidates': sum(count for dimension, count in negative_dimensions.items() if dimension >= 2),
            'scope': 'Discrete source updates in nonempty typed closed words through length twelve; no new continuous durations, all-word or endpoint-dependent no-go.'}


def packaged_sources():
    model = source_model()
    injections = {'bool': zeros(26, 4), 'exchange': zeros(26, 22)}
    for i in range(4):
        injections['bool'][i][i] = F(1)
    for i in range(22):
        injections['exchange'][i + 4][i] = F(1)
    operations = {('bool', operation.value): block_diagonal([list(row) for row in native_permutation(operation)], identity(22))
                  for operation in Operation}
    operations.update({('exchange', label): block_diagonal(identity(4), matrix) for label, matrix in model['raw'].items()})
    return {'dimension': 26, 'metric': block_diagonal(identity(4), model['raw_metric']),
            'injections': injections, 'operations': operations, 'exchange_model': model}


def tag_record(component, record):
    if component not in {'bool', 'exchange'}:
        raise ValueError('unknown source component')
    # A lossless wrapper, not a replacement for the owning source validator.
    return component, record


def restore_record(tagged, component):
    if tagged[0] != component:
        raise ValueError('record/source component mismatch')
    return tagged[1]


def validate_indexed_word(word):
    if not word or any(not isinstance(item, tuple) or len(item) != 2 for item in word):
        raise ValueError('nonempty indexed operation word required')
    components = {component for component, _ in word}
    if len(components) != 1 or not components <= {'bool', 'exchange'}:
        raise ValueError('cross-source arrow not supplied')
    labels = tuple(label for _, label in word)
    if components == {'bool'}:
        if any(label not in {operation.value for operation in Operation} for label in labels):
            raise ValueError('unknown Bool operation')
    else:
        from exchange_source_bridge import validate_word, actual_ports
        validate_word(labels, actual_ports())
    return next(iter(components)), labels
