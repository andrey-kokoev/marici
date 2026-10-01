"""Relative-slot invariants form a graded subalgebra of the declared path model.

Two retained triangle contexts are followed separately in the product category.
This is not the unrestricted seed path language or an admitted physical dynamics.
Grade is actual path length, never reduced modulo the coefficient period.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json
import check_record4_spectral_promotion as sp
import check_spectral_successor_many_many as rec

WORDS = (('AB', 'BC', 'CA'), ('BA', 'AD', 'DB'))
SLOTS = tuple(product(range(3), repeat=2))


def shift(vector, steps):
    return tuple(vector[3 * ((i + steps) % 3) + (j + steps) % 3] for i, j in SLOTS)


def multiply(left, right, left_length):
    return tuple(sp.zmul(x, y) for x, y in zip(left, shift(right, left_length)))


def add(a, b):
    return tuple(sp.zadd(x, y) for x, y in zip(a, b))


def paths(length):
    if not isinstance(length, int) or length < 0:
        raise ValueError('Nonnegative integer path length required')
    return tuple((tuple(WORDS[side][start][0] for side, start in enumerate((i, j))),
                  tuple(WORDS[side][(start + length) % 3][0] for side, start in enumerate((i, j))),
                  tuple(tuple(WORDS[side][(start + k) % 3] for k in range(length))
                        for side, start in enumerate((i, j)))) for i, j in SLOTS)


@dataclass(frozen=True)
class Packet:
    length: int
    coefficients: tuple
    rows: tuple
    parents: tuple = ()


def packet(length, coefficients):
    if len(coefficients) != 9:
        raise ValueError('Nine pair coefficients required')
    return Packet(length, coefficients, paths(length))


def validate(p):
    if len(p.coefficients) != 9 or p.rows != paths(p.length):
        raise ValueError('Forged graded path packet')


def compose(a, b):
    validate(a)
    validate(b)
    result = Packet(a.length + b.length, multiply(a.coefficients, b.coefficients, a.length),
                    paths(a.length + b.length), (a, b))
    for index, (i, j) in enumerate(SLOTS):
        next_index = 3 * ((i + a.length) % 3) + (j + a.length) % 3
        source, middle, awords = a.rows[index]
        bsource, target, bwords = b.rows[next_index]
        assert middle == bsource
        assert result.rows[index] == (source, target, tuple(x + y for x, y in zip(awords, bwords)))
    return result


def main():
    cycles = tuple(sp.cycle_from_packets(tuple(sp.TwoPacket(e, e[0], e[1]) for e in word))
                   for word in WORDS)
    G = rec.kron(sp.zreal(cycles[0]), sp.zreal(sp.transpose(cycles[1])))
    G2 = sp.zmm(G, G)
    assert sp.zmm(G2, G) == rec.IDENTITY
    D = rec.matrix_sum(rec.kron(sp.spectral_projector(cycles[0], mode)[1],
                               sp.spectral_projector(cycles[1], mode)[1]) for mode in rec.MODES)
    average = sp.zmscale(rec.matrix_sum((rec.IDENTITY, G, G2)), (F(1, 3), F(0)))
    assert D == average
    R = sp.zmadd(rec.IDENTITY, sp.zmscale(D, (F(-1), F(0))))
    assert sp.zmm(G, D) == D
    assert sp.ztrace(D) == (F(3), F(0))

    # Basis action moves (i,j) to (i-1,j+1); its three orbits are i+j mod 3.
    orbits = tuple(tuple(index for index, (i, j) in enumerate(SLOTS) if (i + j) % 3 == q)
                   for q in range(3))
    basis = tuple(tuple(rec.ONE if j == i else rec.Z for j in range(9)) for i in range(9))
    for q, orbit in enumerate(orbits):
        for index in orbit:
            v = basis[index]
            support = set()
            for _ in range(3):
                support.add(v.index(rec.ONE))
                v = rec.apply(G, v)
            assert support == set(orbit)
            assert rec.apply(D, basis[index]) == tuple((F(1, 3), F(0)) if k in orbit else rec.Z for k in range(9))

    def lift(values):
        return tuple(values[(i + j) % 3] for i, j in SLOTS)

    def quotient(vector):
        if rec.apply(D, vector) != vector:
            raise ValueError('Only invariant vectors have exact three-orbit coordinates')
        return tuple(vector[orbit[0]] for orbit in orbits)

    def orbit_product(a, b, left_length):
        return tuple(sp.zmul(a[q], b[(q + 2 * left_length) % 3]) for q in range(3))

    # General identity check on all basis pairs and all coefficient-period
    # length residues. Arbitrary nonnegative lengths follow from the formula;
    # the actual grade is still retained separately without periodic quotient.
    for length, i, j in product(range(3), range(9), range(9)):
        x, y = basis[i], basis[j]
        dx, dy, rx, ry = (rec.apply(D, x), rec.apply(D, y), rec.apply(R, x), rec.apply(R, y))
        output = multiply(x, y, length)
        assert rec.apply(G, output) == multiply(rec.apply(G, x), rec.apply(G, y), length)
        invariant_output = multiply(dx, dy, length)
        assert rec.apply(D, invariant_output) == invariant_output
        assert invariant_output == lift(orbit_product(quotient(dx), quotient(dy), length))
        # Conditional-expectation identities (with invariant operand).
        assert rec.apply(D, multiply(dx, y, length)) == invariant_output
        assert rec.apply(D, multiply(x, dy, length)) == invariant_output
        assert rec.apply(D, multiply(dx, ry, length)) == (rec.Z,) * 9
        assert rec.apply(D, multiply(rx, dy, length)) == (rec.Z,) * 9
        assert rec.apply(D, output) == add(invariant_output, rec.apply(D, multiply(rx, ry, length)))

    x = tuple((F(i - 4, 7), F(i % 3 - 1, 5)) for i in range(9))
    y = tuple((F(i + 1, 11), F(i % 2, 3)) for i in range(9))
    z = tuple((F(2 * i - 3, 13), F(i % 4 - 2, 9)) for i in range(9))
    # Operator proof of the shift/product identities used by associativity.
    for m, n in product(range(3), repeat=2):
        assert shift(shift(x, m), n) == shift(x, m + n)
        assert shift(multiply(x, y, 0), m) == multiply(shift(x, m), shift(y, m), 0)
    for m, n, k in product(range(4), repeat=3):
        a, b, c = packet(m, x), packet(n, y), packet(k, z)
        left = compose(compose(a, b), c)
        right = compose(a, compose(b, c))
        assert left.length == right.length == m + n + k
        assert left.coefficients == right.coefficients
        assert left.rows == right.rows
        assert left.parents != right.parents  # retain both construction trees
        for original in (a, b, c):
            assert original.rows == paths(original.length)
    unit = packet(0, (rec.ONE,) * 9)
    a = packet(2, x)
    for result in (compose(unit, a), compose(a, unit)):
        assert result.length == a.length and result.rows == a.rows and result.coefficients == a.coefficients
    loop = packet(3, (rec.ONE,) * 9)
    with_loop = compose(loop, a)
    assert with_loop.coefficients == a.coefficients
    assert tuple((r[0], r[1]) for r in with_loop.rows) == tuple((r[0], r[1]) for r in a.rows)
    assert with_loop.length == 5 and with_loop.rows != a.rows

    # Invariant product is graded and generally noncommutative.
    u, v = (rec.ONE, rec.Z, rec.Z), (rec.Z, rec.Z, rec.ONE)
    uv = compose(packet(1, lift(u)), packet(1, lift(v)))
    vu = compose(packet(1, lift(v)), packet(1, lift(u)))
    assert uv.coefficients != vu.coefficients
    assert rec.apply(D, uv.coefficients) == uv.coefficients

    # Projection is not an algebra homomorphism: hidden*hidden can be visible.
    hidden = rec.apply(R, basis[0])
    other_hidden = shift(hidden, -1)
    assert rec.apply(D, hidden) == rec.apply(D, other_hidden) == (rec.Z,) * 9
    hidden_product = compose(packet(1, hidden), packet(1, other_hidden))
    recovered_visible = rec.apply(D, hidden_product.coefficients)
    assert recovered_visible == lift(((F(2, 9), F(0)), rec.Z, rec.Z))
    assert recovered_visible != multiply(rec.apply(D, hidden), rec.apply(D, other_hidden), 1)
    aggregate = rec.Z
    for value in hidden_product.coefficients:
        aggregate = sp.zadd(aggregate, value)
    assert sp.zscale(aggregate, F(1, 81)) == (F(2, 243), F(0))
    rec.reject(lambda: quotient(hidden))
    rec.reject(lambda: packet(-1, x))

    # Source-derived seam marker: extract reciprocity from actual endpoints,
    # not from a numerical eigenmode or from labels assumed to be inverses.
    edge_packets = {e: sp.TwoPacket(e, e[0], e[1]) for word in WORDS for e in word}
    pair_manifest = tuple((WORDS[0][i], WORDS[1][j]) for i, j in SLOTS)

    def reciprocal_pairs(endpoints):
        labels = tuple(endpoints)
        return {frozenset((a, b)) for a in labels for b in labels if a != b
                and endpoints[a] == tuple(reversed(endpoints[b]))}

    def seam_marker(endpoints):
        return tuple(rec.ONE if endpoints[a] == tuple(reversed(endpoints[b])) else rec.Z
                     for a, b in pair_manifest)

    endpoints = {e: (p.source, p.target) for e, p in edge_packets.items()}
    reciprocal = reciprocal_pairs(endpoints)
    assert reciprocal == {frozenset(('AB', 'BA'))}
    marker = seam_marker(endpoints)
    seam_index = marker.index(rec.ONE)
    assert seam_index == 0 and sum(z == rec.ONE for z in marker) == 1
    # The defining predicate is covariant under all vertex renamings, with
    # occurrence labels retained as IDs. Removing either occurrence removes it.
    for image in permutations('ABCD'):
        rename = dict(zip('ABCD', image))
        renamed = {e: (rename[s], rename[t]) for e, (s, t) in endpoints.items()}
        assert reciprocal_pairs(renamed) == reciprocal
        assert seam_marker(renamed) == marker
    for deleted in ('AB', 'BA'):
        assert reciprocal_pairs({e: st for e, st in endpoints.items() if e != deleted}) == set()

    marker_images = (marker, rec.apply(G, marker), rec.apply(G2, marker))
    marker_pairs = tuple(pair_manifest[v.index(rec.ONE)] for v in marker_images)
    assert marker_pairs == (('AB', 'BA'), ('CA', 'AD'), ('BC', 'DB'))
    assert all(seam_marker(endpoints)[v.index(rec.ONE)] == rec.Z for v in marker_images[1:])
    assert rec.vector_sum(marker_images) == tuple(sp.zscale(z, 3) for z in rec.apply(D, marker))
    # In contrast, the genuine seed automorphism exchanges triangle factors.
    flip = tuple(tuple(rec.ONE if row == 3 * (col % 3) + col // 3 else rec.Z
                       for col in range(9)) for row in range(9))
    swap = dict(zip('ABCD', 'BADC'))
    for pair in pair_manifest:
        transported = tuple(swap[e[0]] + swap[e[1]] for e in reversed(pair))
        i, j = WORDS[0].index(pair[0]), WORDS[1].index(pair[1])
        assert transported == pair_manifest[3 * j + i]
    assert rec.apply(flip, marker) == marker

    # Conditional amplitude adapter: use the retained address to read a
    # coefficient. This is NOT asserted to be the source's physical reader.
    h = (marker,)
    assert sp.zmm(h, D) != h
    assert sp.zmm(h, R) != ((rec.Z,) * 9,)
    marked = marker
    unmarked_same_orbit = marker_images[1]
    assert rec.apply(D, marked) == rec.apply(D, unmarked_same_orbit)
    assert marked[seam_index] == rec.ONE and unmarked_same_orbit[seam_index] == rec.Z
    assert rec.apply(R, marked)[seam_index] == (F(2, 3), F(0))
    # Restricting PREPARATION to invariant states remains consistent: the
    # seam value is then the orbit-0 coefficient. It is not arbitrary-state recovery.
    invariant = rec.apply(D, x)
    assert invariant[seam_index] == quotient(invariant)[0]
    assert invariant[seam_index] == rec.apply(D, invariant)[seam_index]

    # Also reuse the already declared endpoint-comparison reader with the
    # actual seam address as probe: J(v,marker)=v^T M marker/81. No new weights.
    M = rec.kron(sp.zreal(cycles[0]), sp.zreal(cycles[1]))
    predecessor = rec.apply(M, marker)
    predecessor_index = predecessor.index(rec.ONE)
    assert pair_manifest[predecessor_index] == ('CA', 'DB')

    def seam_probe_response(v):
        total = rec.Z
        for a, b in zip(v, predecessor):
            total = sp.zadd(total, sp.zmul(a, b))
        return sp.zscale(total, F(1, 81))

    coarse_predecessor = rec.apply(D, predecessor)
    assert rec.apply(D, predecessor) == rec.apply(D, coarse_predecessor)
    assert seam_probe_response(predecessor) == (F(1, 81), F(0))
    assert seam_probe_response(coarse_predecessor) == (F(1, 243), F(0))
    # Exact seam metadata is recoverable from the retained endpoints, even
    # when D-state alone cannot reconstruct its coefficient or probe response.
    retained_endpoints = dict(endpoints)
    assert seam_marker(retained_endpoints) == marker

    report = {
        'status': 'passed',
        'scope': 'declared two-context product path model; not unrestricted seed paths or source-selected physical quotient',
        'group_average_identity': 'D=(I+G+G^2)/3; G=C_left tensor C_right^-1',
        'orbits': [[tuple(WORDS[side][SLOTS[index][side]] for side in range(2)) for index in orbit] for orbit in orbits],
        'invariant_dimension_per_grade': 3,
        'full_dimension_per_grade': 9,
        'graded_product': '(x_m*y_n)(i,j)=x(i,j)*y(i+m,j+m), length m+n',
        'orbit_coordinate_product': '(u_m*v_n)(q)=u(q)*v(q+2m mod 3), length m+n',
        'basis_pair_identity_checks': 243,
        'path_associativity_fixtures': 64,
        'invariant_subalgebra': True,
        'conditional_expectation_bimodule_identities': True,
        'projection_is_algebra_homomorphism': False,
        'kernel_is_two_sided_ideal': False,
        'hidden_product_visible_orbit_value': '2/9',
        'hidden_product_fixed_aggregate': '2/243',
        'full_path_length_and_parenthesization_retained': True,
        'seam_reference_audit': {
            'source_reciprocal_pair': ['AB', 'BA'],
            'all_vertex_renamings_checked': 24,
            'deletion_controls': 2,
            'relative_rotation_marker_orbit': marker_pairs,
            'marker_fixed_by_relative_rotation': False,
            'marker_preserved_by_seed_factor_exchange': True,
            'seam_coordinate_reader_factors_through_D': False,
            'same_D_coordinate_hostile_readings': ['1', '0'],
            'seam_probe_under_existing_join': ['1/81', '1/243'],
            'invariant_preparations_remain_consistent': True,
            'source_marker_retained_as_metadata': True,
            'scope': 'source marker extraction; conditional coefficient reading/probe, not admitted physical measurement'}, 
        'not_claimed': ['physical gauge equivalence', 'erasure of history under period three',
                        'admitted preparation of invariant states', 'new traversal events'],
    }
    dest = Path(__file__).resolve().parents[1] / 'results' / 'spectral-invariant-path-algebra.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: same-mode projection is relative-slot group averaging over three size-three orbits.')
    print('PASS: invariant graded composition closes; three-orbit product and conditional-expectation identities agree.')
    print('PASS: path concatenation is associative with grade and parent trees retained; a three-step loop is not empty.')
    print('PASS: hidden*hidden has nonzero visible component; projection is not an algebra quotient.')
    print('PASS: reciprocal seam is source-defined and relabelling-covariant, but not fixed by relative rotation.')
    print('PASS: seam coefficient/probe readings do not factor through D for arbitrary states; metadata alone is insufficient.')
    print('Report: research/nima/results/spectral-invariant-path-algebra.json')


if __name__ == '__main__':
    main()
