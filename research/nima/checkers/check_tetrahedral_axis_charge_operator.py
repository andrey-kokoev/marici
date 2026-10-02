"""Exact axis-charge candidate scan, with counterexamples to the old no-go.

This checks a bounded family, not a classification of physical charge.
Dependency-free; expectation, spectrum and eigenstate status are distinct.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json

from check_twelve_triangle_positive_geometry import (
    I, ONE, ZERO, OMEGA, POINTS, compose, rotation, mean, transpose,
    mm, zmv, zadd, zmul, zscale, zconj, znorm, projector,
)


def inner(a, b):
    out = ZERO
    for x, y in zip(a, b):
        out = zadd(out, zmul(zconj(x), y))
    return out


def apply(m, v):
    return tuple(inner(tuple(zconj(z) for z in row), v) for row in m)


def main():
    seeds = ((1, 2, 0, 3), (3, 0, 2, 1))
    group, front = {tuple(range(4))}, [tuple(range(4))]
    while front:
        q = front.pop()
        for g in seeds:
            p = compose(g, q)
            if p not in group:
                group.add(p)
                front.append(p)
    rotations = [rotation(p) for p in sorted(group)]
    assert len(rotations) == 12
    centre = mean([POINTS[a] for a in 'ABC'])
    x0 = transpose((centre, POINTS['A'], POINTS['B']))
    v0 = zmv(x0, (ONE, OMEGA, zmul(OMEGA, OMEGA)))
    vectors = [zmv(r, v0) for r in rotations]
    u = tuple(z for v in vectors for z in v)
    norm0, norm = sum(map(znorm, v0)), sum(map(znorm, u))
    assert norm0 == F(20, 3) and norm == 80
    axis_norms = [sum(znorm(v[i]) for v in vectors) for i in range(3)]
    assert axis_norms == [F(80, 3)] * 3

    # Correct axis labels: Rx preserves x, etc.
    diagonals = {'axis1': (1, 0, 0), 'axis1_minus_axis2': (1, -1, 0),
                 'flipped_axes_by_h1': (0, 1, 1), 'identity': (1, 1, 1),
                 'scaled_Rx': (-3, 3, 3)}
    halves = {}
    for axis, label in enumerate(('Rx', 'Ry', 'Rz')):
        h = tuple(1 if i == axis else -1 for i in range(3))
        halves[label] = h
        diagonals[f'V4_{label}_as_charge'] = h
        diagonals[f'V4_{label}_positive_eigenspace'] = tuple(F(1+a, 2) for a in h)
    assert tuple(-sum(h[i] for h in halves.values()) for i in range(3)) == (1, 1, 1)
    results = {}
    for name, diagonal in sorted(diagonals.items()):
        diagonal = tuple(map(F, diagonal))
        acted = tuple(zscale(z, diagonal[i % 3]) for i, z in enumerate(u))
        expectation = zscale(inner(u, acted), 1/norm)
        second = sum(diagonal[i % 3]**2 * znorm(z) for i, z in enumerate(u))/norm
        assert expectation[1] == 0 and expectation[0] == sum(diagonal)/3
        variance = second - expectation[0]**2
        is_eigenstate = acted == tuple(zscale(z, expectation[0]) for z in u)
        assert is_eigenstate == (variance == 0)
        block = tuple(tuple(diagonal[i] if i == j else F(0) for j in range(3)) for i in range(3))
        commutes = all(mm(block, r) == mm(r, block) for r in rotations)
        results[name] = {
            'per_fiber_diagonal': list(map(str, diagonal)),
            'eigenvalues': list(map(str, sorted(set(diagonal)))),
            'eigenvalue_multiplicities': {str(a): n for a, n in sorted(Counter(diagonal).items())},
            'expectation_on_collective_mode': str(expectation[0]),
            'variance_on_collective_mode': str(variance),
            'collective_mode_is_eigenstate': is_eigenstate,
            'commutes_with_combined_A4_action': commutes,
        }
    assert results['scaled_Rx']['expectation_on_collective_mode'] == '1'
    assert results['scaled_Rx']['variance_on_collective_mode'] == '8'
    assert results['identity']['collective_mode_is_eigenstate']
    n = projector(u)
    assert apply(n, u) == u
    # N is Hermitian; N^2=N follows from u^*u=norm, with rank one.
    assert all(n[i][j] == zconj(n[j][i]) for i in range(36) for j in range(36))
    assert sum(n[i][i][0] for i in range(36)) == 1
    neutral = (zconj(u[1]), zscale(zconj(u[0]), -1)) + (ZERO,) * 34
    assert any(z != ZERO for z in neutral) and inner(u, neutral) == ZERO
    assert apply(n, neutral) == (ZERO,) * 36
    for g in rotations:
        for x, r in enumerate(rotations):
            source = rotations.index(mm(transpose(g), r))
            assert zmv(g, vectors[source]) == vectors[x]
    report = {
        'status': 'passed', 'arithmetic': 'Q(i*sqrt(3))',
        'reference_eigenvector': [[str(a), str(b)] for a, b in v0],
        'reference_squared_norm': str(norm0), 'assembled_squared_norm': str(norm),
        'axis_squared_norms': list(map(str, axis_norms)), 'charge_candidates': results,
        'counterexamples_to_previous_no_go': {
            'identity': 'I=-H_x-H_y-H_z lies in the V4 algebra; spectrum {1}, expectation 1.',
            'N': 'N=u u*/80 commutes with the combined A4 action; spectrum {0,1}; Nu=u; N neutral=0.',
            '2N_minus_I': 'Hermitian involution commuting with A4; spectrum {-1,1}; u has eigenvalue 1.',
        },
        'scope': 'Finite candidate scan only. Neither a universal charge no-go nor a physical charge derivation.',
        'missing_physical_input': 'An independently specified neutral/antiparticle sector and electromagnetic coupling; the algebraic neutral example is not a neutron identification.',
    }
    dest = Path(__file__).resolve().parents[1] / 'results' / 'tetrahedral-axis-charge-operator.json'
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: 11 diagonal candidates; scaled Rx expectation 1 but variance 8.')
    print('PASS: I, N and 2N-I refute the previous universal charge no-go; no physical charge identification.')


if __name__ == '__main__':
    main()
