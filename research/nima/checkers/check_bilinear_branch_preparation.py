"""Single-product reachability of sibling detail in the declared path algebra.

Exact rational inputs are supplied, not physically prepared. Separate the
single bilinear image, its linear span, and the projection to branch detail.
"""
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

import check_natural_tower_return as algebra
from check_whole_seed_occurrence_spectrum import rank
from retained_path_successor import RetainedSuccessorLedger, coefficients, apply


def rejects(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError('Invalid bilinear preparation was accepted')


def main():
    ledger = RetainedSuccessorLedger(algebra.PACKETS)
    root = ledger.root
    child = ledger.successor(root)
    labels = ledger.labels
    index = {label: i for i, label in enumerate(labels)}
    words = tuple(tuple(edge[2] for edge in path) for path in child.paths)
    word_index = {word: i for i, word in enumerate(words)}
    branching = ('AB', 'CA', 'BA', 'DB')
    siblings = {label: tuple(i for i, word in enumerate(words) if word[0] == label) for label in labels}
    vertices = tuple(algebra.LABELS)
    blocks = {v: (tuple(label for label, _, target in ledger.packets if target == v),
                  tuple(label for label, source, _ in ledger.packets if source == v)) for v in vertices}
    assert {v: (len(a), len(b)) for v, (a, b) in blocks.items()} == {
        'A': (2, 2), 'B': (2, 2), 'C': (1, 1), 'D': (1, 1)}

    def compose(x, y):
        return ledger.compose_primitive_payloads(child, x, y)

    def detail_coordinates(payload):
        _, residual = ledger.split_payload(child, payload)
        return tuple(residual[siblings[label][0]] for label in branching)

    def detail_vector(c):
        result = [F(0)] * len(words)
        for label, value in zip(branching, c):
            first, second = siblings[label]
            result[first], result[second] = value, -value
        return tuple(result)

    def block_matrix(payload, vertex):
        incoming, outgoing = blocks[vertex]
        return tuple(tuple(payload[word_index[a, b]] for b in outgoing) for a in incoming)

    def factor_single(payload):
        # Each primitive input coordinate occurs in exactly one interface-vertex
        # block: x by target, y by source. Thus rank<=1 in every block is both
        # necessary and sufficient for a single global input pair.
        payload = coefficients(payload, len(words))
        left, right = [F(0)] * 6, [F(0)] * 6
        for vertex, (incoming, outgoing) in blocks.items():
            matrix = block_matrix(payload, vertex)
            if rank(matrix) > 1:
                raise ValueError('Interface block is not a single outer product')
            pivot = next(((i, j) for i in range(len(incoming)) for j in range(len(outgoing)) if matrix[i][j]), None)
            if pivot is None:
                continue
            i0, j0 = pivot
            for i, a in enumerate(incoming):
                left[index[a]] = matrix[i][j0]
            for j, b in enumerate(outgoing):
                right[index[b]] = matrix[i0][j] / matrix[i0][j0]
        left, right = tuple(left), tuple(right)
        assert compose(left, right) == payload
        return left, right

    basis = tuple(tuple(F(i == j) for j in range(6)) for i in range(6))
    x = tuple(F(i + 1, 7) for i in range(6))
    y = tuple(F(2 * i + 1, 11) for i in range(6))
    ones, zeros = (F(1),) * 6, (F(0),) * 6
    fixtures = ((x, y), (x, ones), (zeros, y), (x, zeros)) + tuple(product(basis, repeat=2))
    for left, right in fixtures:
        payload = compose(left, right)
        means, residual = ledger.split_payload(child, payload)
        delta_B = (right[index['BA']] - right[index['BC']]) / 2
        delta_A = (right[index['AB']] - right[index['AD']]) / 2
        expected = (left[index['AB']] * delta_B, left[index['CA']] * delta_A,
                    left[index['BA']] * delta_A, left[index['DB']] * delta_B)
        assert detail_coordinates(payload) == expected
        assert residual == detail_vector(expected)
        assert ledger.reassemble_payload(child, means, residual) == payload
        coarse = ledger.summarize(child, payload)
        assert coarse == tuple(a * b for a, b in zip(right, apply(ledger.continuation, left)))
        for v in vertices:
            assert rank(block_matrix(payload, v)) <= 1
        factor_single(payload)
        # Necessary full-output constraints, expressed in means/detail coords.
        m = dict(zip(labels, means))
        c = dict(zip(branching, expected))
        assert m['CA'] * c['BA'] == m['BA'] * c['CA']
        assert m['AB'] * c['DB'] == m['DB'] * c['AB']
    assert compose(x, ones) == ledger.encode(root, child, x)
    assert detail_coordinates(compose(x, ones)) == (F(0),) * 4

    # The fixed continuation profile below realizes ANY four rational detail
    # coordinates in ONE product. Singleton coefficients are deliberately zero.
    # This supplied signed profile is an existence witness, not a selected
    # physical preparation or an operation inferred from the seed.
    right_detail = tuple(F(label in ('AB', 'BA')) - F(label in ('AD', 'BC')) for label in labels)

    def prepare_pure_detail(c):
        c = coefficients(c, 4)
        left = tuple(c[branching.index(label)] if label in branching else F(0) for label in labels)
        payload = compose(left, right_detail)
        assert payload == detail_vector(c)
        assert ledger.split_payload(child, payload) == ((F(0),) * 6, payload)
        return left, right_detail, payload

    for c in tuple(tuple(F(i == j) for j in range(4)) for i in range(4)) + (
            (F(2, 3), F(-5, 7), F(11, 13), F(17, 19)),):
        prepare_pure_detail(c)
    residual_fixed_x = tuple(detail_coordinates(compose(x, e)) for e in basis)
    residual_fixed_y = tuple(detail_coordinates(compose(e, right_detail)) for e in basis)
    assert rank(residual_fixed_x) == 2
    assert rank(residual_fixed_y) == 4

    # Visibility is exactly the two sums, not the four independent details.
    for c in ((F(1), F(0), F(0), F(0)), (F(1), F(2), F(-2), F(-1))):
        _, _, payload = prepare_pure_detail(c)
        coarse = ledger.summarize(child, payload)
        expected = tuple((c[0] + c[3]) * (F(label == 'BA') - F(label == 'BC'))
                         + (c[1] + c[2]) * (F(label == 'AB') - F(label == 'AD')) for label in labels)
        assert coarse == expected
    _, _, hidden = prepare_pure_detail((F(1), F(2), F(-2), F(-1)))
    assert any(hidden) and ledger.summarize(child, hidden) == zeros
    # No right operand can make a left ker(K) input visible to this particular
    # final-occurrence summary: A B(x,y)=diag(y) Kx.
    for contrast in (tuple(F(label == 'CA') - F(label == 'BA') for label in labels),
                     tuple(F(label == 'AB') - F(label == 'DB') for label in labels)):
        for right in basis + (y, right_detail, ones):
            assert ledger.summarize(child, compose(contrast, right)) == zeros
        assert any(detail_coordinates(compose(contrast, right_detail)))

    # Single-product output versus its linear span.
    products = tuple(compose(a, b) for a, b in product(basis, repeat=2))
    output_basis = tuple(tuple(F(i == j) for j in range(10)) for i in range(10))
    assert all(vector in products for vector in output_basis)
    assert rank(products) == 10
    for v in ('A', 'B'):
        incoming, outgoing = blocks[v]
        bad = [F(0)] * 10
        bad[word_index[incoming[0], outgoing[0]]] = F(1)
        bad[word_index[incoming[1], outgoing[1]]] = F(1)
        rejects(lambda bad=bad: factor_single(tuple(bad)))
        assert rank(block_matrix(bad, v)) == 2
        # Both individual terms are admitted single products; their sum is not.
        single1 = compose(basis[index[incoming[0]]], basis[index[outgoing[0]]])
        single2 = compose(basis[index[incoming[1]]], basis[index[outgoing[1]]])
        assert tuple(a + b for a, b in zip(single1, single2)) == tuple(bad)

    # Generic local dimension: two 2x2 rank-one blocks (dimension three each)
    # plus two scalar blocks = eight. Verify the derivative rank and four
    # independent per-vertex rescaling directions exactly at a nonzero fixture.
    jacobian = tuple(tuple(F(i == index[a]) * y[index[b]] for i in range(6))
                     + tuple(F(j == index[b]) * x[index[a]] for j in range(6)) for a, b in words)
    assert rank(jacobian) == 8
    gauge_vectors = []
    for incoming, outgoing in blocks.values():
        gauge = tuple(x[i] if label in incoming else F(0) for i, label in enumerate(labels)) + tuple(
            -y[i] if label in outgoing else F(0) for i, label in enumerate(labels))
        assert apply(jacobian, gauge) == (F(0),) * 10
        gauge_vectors.append(gauge)
    assert rank(gauge_vectors) == 4

    # A generic fixed decoded-parent profile leaves one detail parameter per
    # branching vertex, rather than four independently selectable details.
    means, _ = ledger.split_payload(child, compose(x, y))
    mean = dict(zip(labels, means))
    compatibility = ((F(0), -mean['BA'], mean['CA'], F(0)),
                     (-mean['DB'], F(0), F(0), mean['AB']))
    assert rank(compatibility) == 2
    feasible_c = detail_coordinates(compose(x, y))
    assert apply(compatibility, feasible_c) == (F(0), F(0))
    bad_c = list(feasible_c)
    bad_c[0] += 1
    inconsistent = ledger.reassemble_payload(child, means, detail_vector(bad_c))
    rejects(lambda: factor_single(inconsistent))

    rejects(lambda: ledger.compose_primitive_payloads(root, x, y))
    later = ledger.successor(child)
    rejects(lambda: ledger.compose_primitive_payloads(later, x, y))
    rejects(lambda: ledger.compose_primitive_payloads(replace(child), x, y))
    rejects(lambda: ledger.compose_primitive_payloads(child, x[:-1], y))
    rejects(lambda: ledger.compose_primitive_payloads(child, x, (0.1,) * 6))

    report = {
        'status': 'passed', 'primitive_order': labels, 'detail_order': branching,
        'detail_formula': {'AB': 'x_AB (y_BA-y_BC)/2', 'DB': 'x_DB (y_BA-y_BC)/2',
                           'CA': 'x_CA (y_AB-y_AD)/2', 'BA': 'x_BA (y_AB-y_AD)/2'},
        'single_product_detail_image': 'all four rational sibling-detail coordinates; explicit pure-detail construction',
        'fixed_nonzero_left_detail_rank': 2, 'fixed_signed_right_detail_rank': 4,
        'coarse_detail': '(c_AB+c_DB)(BA-BC)+(c_CA+c_BA)(AB-AD)',
        'coarse_full_product': 'A B(x,y)=diag(y) K x',
        'single_product_full_output': {
            'block_shapes': {'A': [2, 2], 'B': [2, 2], 'C': [1, 1], 'D': [1, 1]},
            'necessary_and_sufficient': 'each endpoint-interface block has rank at most one',
            'two_determinant_constraints': True, 'generic_jacobian_rank': 8,
            'linear_span_rank': 10, 'rank_two_block_controls_rejected': True,
            'generic_fixed_parent_means_leave_two_detail_parameters': True},
        'unchanged_right_ones_gives_zero_detail': True,
        'nonzero_hidden_details_attainable': True,
        'left_K_kernel_invisible_for_every_right_operand_to_final_occurrence_summary': True,
        'scope': 'declared bilinear coefficient extension with independently supplied rational inputs; no physical preparation, normalization or probability assignment'}
    dest = Path(__file__).resolve().parents[1] / 'results' / 'bilinear-branch-preparation.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: one supplied bilinear pair can realize arbitrary four-dimensional pure sibling detail.')
    print('PASS: full single-product outputs obey two rank-one block constraints; generic dimension eight, span ten.')
    print('PASS: coarse detail has rank two; left K-zero inputs remain invisible for all right operands.')
    print('Report: research/nima/results/bilinear-branch-preparation.json')


if __name__ == '__main__':
    main()
