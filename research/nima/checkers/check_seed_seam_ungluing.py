"""Matched ungluing control for the retained six-plus-three coefficient law.

Only cross-context vertex identification changes. Occurrence IDs, local orders,
coefficient inputs and address readers stay fixed. No missing reciprocal marker
is replaced by an externally chosen reference.
"""
from itertools import permutations, product
from fractions import Fraction as F
from pathlib import Path
import json
import check_record4_spectral_promotion as sp
import check_spectral_successor_many_many as rec
import check_spectral_invariant_path_algebra as alg


def main():
    words = alg.WORDS
    glued = tuple(tuple(sp.TwoPacket(e, e[0], e[1]) for e in word) for word in words)
    # Preserve every label. Endpoint identities carry context tags only in the
    # unglued fixture; no later calculation may parse endpoints from the label.
    unglued = tuple(tuple(sp.TwoPacket(p.label, (side, p.source), (side, p.target))
                          for p in triangle) for side, triangle in enumerate(glued))
    manifest = tuple(product(*words))
    slots = alg.SLOTS

    def source_marker(triangles):
        return tuple(rec.ONE if a.source == b.target and a.target == b.source else rec.Z
                     for a in triangles[0] for b in triangles[1])

    def automorphisms(triangles):
        vertices = tuple(dict.fromkeys(p.source for triangle in triangles for p in triangle))
        edges = {(p.source, p.target) for triangle in triangles for p in triangle}
        count = 0
        for image in permutations(vertices):
            rename = dict(zip(vertices, image))
            count += {(rename[a], rename[b]) for a, b in edges} == edges
        return count

    def fixture(triangles):
        cycles = tuple(sp.cycle_from_packets(triangle) for triangle in triangles)
        # Derive tuple endpoint matching directly, independent of the cyclic
        # matrix implementation. The 9x9 mask acts on the 81 candidate products.
        pairs = tuple(product(*triangles))
        sources = tuple(tuple(p.source for p in pair) for pair in pairs)
        targets = tuple(tuple(p.target for p in pair) for pair in pairs)
        M = tuple(tuple(rec.ONE if t == s else rec.Z for s in sources) for t in targets)
        assert M == rec.kron(sp.zreal(cycles[0]), sp.zreal(cycles[1]))
        P_modes = {(a, b): rec.kron(sp.spectral_projector(cycles[0], a)[1],
                                     sp.spectral_projector(cycles[1], b)[1]) for a, b in rec.KEYS}
        D = rec.matrix_sum(P_modes[m, m] for m in rec.MODES)
        return cycles, M, P_modes, D

    before = fixture(glued)
    after = fixture(unglued)
    assert before == after
    cycles, M, projectors, D = before
    marker_before, marker_after = source_marker(glued), source_marker(unglued)
    assert marker_before == (rec.ONE,) + (rec.Z,) * 8
    assert marker_after == (rec.Z,) * 9
    assert sum(z == rec.ONE for z in marker_before) == 1
    assert sum(z == rec.ONE for z in marker_after) == 0
    assert automorphisms(glued) == 2 and automorphisms(unglued) == 18

    W = tuple(tuple(rec.ONE if row == 3 * (col % 3) + col // 3 else rec.Z
                    for col in range(9)) for row in range(9))
    P = sp.zmscale(sp.zmadd(rec.IDENTITY, W), (F(1, 2), F(0)))
    Q = sp.zmadd(rec.IDENTITY, sp.zmscale(P, (F(-1), F(0))))
    # The SAME role-aligned exchange is still an automorphism after ungluing,
    # but is no longer the unique nonidentity graph automorphism.
    vertex_swap = dict(zip('ABCD', 'BADC'))
    def swapped(vertex, split):
        if split:
            side, label = vertex
            return (1 - side, vertex_swap[label])
        return vertex_swap[vertex]
    for triangles, split in ((glued, False), (unglued, True)):
        edges = {(p.source, p.target) for triangle in triangles for p in triangle}
        assert {(swapped(a, split), swapped(b, split)) for a, b in edges} == edges

    def path_rows(triangles, length):
        return tuple((tuple(triangles[side][start].source for side, start in enumerate((i, j))),
                      tuple(triangles[side][(start + length) % 3].source for side, start in enumerate((i, j))),
                      tuple(tuple(triangles[side][(start + k) % 3].label for k in range(length))
                            for side, start in enumerate((i, j)))) for i, j in slots)

    def coefficient_product(triangles, x, y, left_length, right_length):
        left = path_rows(triangles, left_length)
        right = path_rows(triangles, right_length)
        output = path_rows(triangles, left_length + right_length)
        values = []
        for row, (source, target, histories) in enumerate(left):
            matches = [j for j, (s, _, _) in enumerate(right) if target == s]
            assert len(matches) == 1
            j = matches[0]
            assert output[row] == (source, right[j][1], tuple(a + b for a, b in zip(histories, right[j][2])))
            values.append(sp.zmul(x[row], y[j]))
        return tuple(values)

    basis = tuple(tuple(rec.ONE if i == j else rec.Z for j in range(9)) for i in range(9))
    for length, i, j in product(range(3), range(9), range(9)):
        x, y = basis[i], basis[j]
        result_before = coefficient_product(glued, x, y, length, 1)
        result_after = coefficient_product(unglued, x, y, length, 1)
        assert result_before == result_after == alg.multiply(x, y, length)
        s1, s2 = rec.apply(P, x), rec.apply(P, y)
        a1, a2 = rec.apply(Q, x), rec.apply(Q, y)
        ss = coefficient_product(unglued, s1, s2, length, 1)
        aa = coefficient_product(unglued, a1, a2, length, 1)
        sa = coefficient_product(unglued, s1, a2, length, 1)
        ass = coefficient_product(unglued, a1, s2, length, 1)
        assert rec.apply(P, result_after) == alg.add(ss, aa)
        assert rec.apply(Q, result_after) == alg.add(sa, ass)
        assert aa == coefficient_product(glued, a1, a2, length, 1)
        assert all(aa[3 * k + k] == rec.Z for k in range(3))

    x = tuple((F(i - 4, 7), F(i % 3 - 1, 5)) for i in range(9))
    y = tuple((F(i + 1, 11), F(i % 2, 3)) for i in range(9))
    for m, n in product(range(7), repeat=2):
        assert coefficient_product(glued, x, y, m, n) == coefficient_product(unglued, x, y, m, n)
        g, u = path_rows(glued, m + n), path_rows(unglued, m + n)
        assert tuple(r[2] for r in g) == tuple(r[2] for r in u)
        assert tuple(r[:2] for r in g) != tuple(r[:2] for r in u)

    # Nonzero AA effect survives with the same role-addressed preparation and
    # reader. It therefore does not demonstrate response to seam identification.
    hidden = rec.subtract(basis[1], basis[3])
    partner = alg.shift(hidden, -1)
    hidden_outputs = tuple(coefficient_product(t, hidden, partner, 1, 1) for t in (glued, unglued))
    assert hidden_outputs[0] == hidden_outputs[1] != (rec.Z,) * 9
    assert rec.apply(P, hidden_outputs[0]) == hidden_outputs[0]
    assert rec.apply(D, hidden_outputs[0]) != (rec.Z,) * 9

    # Static address remains a valid retained ID, but its source role changes.
    # The source-extracted reference query is now unavailable, NOT a measurement
    # of zero. Refuse to select an arbitrary replacement.
    def unique_reference(marker):
        choices = [manifest[i] for i, value in enumerate(marker) if value == rec.ONE]
        if len(choices) != 1:
            raise ValueError('No unique reciprocal reference address')
        return choices[0]

    assert unique_reference(marker_before) == ('AB', 'BA')
    rec.reject(lambda: unique_reference(marker_after))
    # Guard against reverting to string-parsed endpoints in the split fixture.
    by_label = {p.label: p for triangle in unglued for p in triangle}
    assert by_label['AB'].source != by_label['BA'].target
    assert by_label['AB'].target != by_label['BA'].source

    report = {
        'status': 'passed',
        'intervention': 'split all shared vertex identities between the two triangle contexts; keep occurrence IDs/order/coefficients fixed',
        'vertices': {'glued': 4, 'unglued': 6},
        'reciprocal_cross_context_pairs': {'glued': 1, 'unglued': 0},
        'directed_graph_automorphisms': {'glued': 2, 'unglued': 18},
        'unchanged': ['local cyclic operators', 'all nine mode-pair projectors',
                      'product-category endpoint mask', 'D/P/Q coefficient operations under fixed role alignment',
                      'graded multiplication', 'six-plus-three update', 'nonzero AA correction',
                      'fixed occurrence-addressed numerical readings', 'ordered primitive histories'],
        'changed': ['cross-context shared endpoints', 'source reciprocal seam predicate',
                    'availability of unique source-derived reciprocal reference', 'uniqueness of chosen exchange symmetry'],
        'basis_pair_length_controls': 243,
        'complex_path_length_fixtures': 49,
        'conclusion': 'Current response law is generic to the declared two-cycle product representation; seed seam selects a reference address but does not enter this coefficient dynamics.',
        'not_claimed': ['all possible source-derived laws ignore the seam', 'an unavailable reference has zero physical response',
                        'the retained AB/BA labels remain reciprocal after ungluing', 'this representation is physically selected'],
    }
    dest = Path(__file__).resolve().parents[1] / 'results' / 'seed-seam-ungluing.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: splitting shared vertices leaves the declared coefficient algebra and nonzero AA correction unchanged.')
    print('PASS: reciprocal seam disappears; source-selected reference query is unavailable, not zero.')
    print('PASS: graph automorphism count grows 2 -> 18; the tracked role alignment is no longer unique.')
    print('BOUNDARY: generic two-cycle response algebra, not demonstrated seam-generated dynamics.')
    print('Report: research/nima/results/seed-seam-ungluing.json')


if __name__ == '__main__':
    main()
