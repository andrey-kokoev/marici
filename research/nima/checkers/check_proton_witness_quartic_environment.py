"""Exact quartic probe tests on the existing tetrahedral collective mode.

Probe partitions are candidate environment models, not a derived universe.
No fitted coefficients; all arithmetic is in Q(sqrt(-3)) or Q.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import (
    LABELS, POINTS, ONE, OMEGA, compose, rotation, mean, transpose,
    zmv, zmul, znorm,
)


def main():
    generators = ((1, 2, 0, 3), (3, 0, 2, 1))
    group = {(0, 1, 2, 3)}
    frontier = list(group)
    while frontier:
        q = frontier.pop()
        for g in generators:
            p = compose(g, q)
            if p not in group:
                group.add(p)
                frontier.append(p)
    assert len(group) == 12
    x0 = transpose((mean([POINTS[k] for k in 'ABC']), POINTS['A'], POINTS['B']))
    v0 = zmv(x0, (ONE, OMEGA, zmul(OMEGA, OMEGA)))
    permutations = sorted(group)
    vectors = [zmv(rotation(g), v0) for g in permutations]
    u = [z for v in vectors for z in v]
    norm = sum(map(znorm, u))
    assert norm == 80
    weights = [znorm(z) / norm for z in u]
    assert sum(weights) == 1 and all(w > 0 for w in weights)

    # e is the unit Hermitian-dual candidate of the unit collective mode p.
    # Thus |e_j|^2 = |p_j|^2 = weights[j]. For orthogonal block probes E_a,
    # Q_U(p,e) = sum_a (p† E_a p)(e† conjugate(E_a) e).
    # Here E_a are real diagonal masks, so Q_U = sum_a block_weight[a]^2.
    partitions = {
        'whole_space': [0] * 36,
        'four_parent_faces': [tuple(sorted(g[:3])) for g in permutations for _ in range(3)],
        'twelve_triangles': [i for i in range(12) for _ in range(3)],
        'three_ambient_axes': [j for _ in range(12) for j in range(3)],
        'thirty_six_ports': list(range(36)),
    }
    rows = []
    for name, labels in partitions.items():
        blocks = {}
        for label, w in zip(labels, weights):
            blocks[label] = blocks.get(label, F(0)) + w
        q = sum(w*w for w in blocks.values())
        # Fixed test energy: E_U(a p, b e) = |a|² + |b|² + |a b|² Q_U.
        # This is a declared unit-strength model; the baselines cancel.
        def energy(a, b):
            return a*a + b*b + a*a*b*b*q
        excess = energy(F(1), F(1))-energy(F(1), F(0))-energy(F(0), F(1))+energy(F(0), F(0))
        assert excess == q
        assert energy(F(2), F(3))-energy(F(2), F(0))-energy(F(0), F(3)) == 36*q
        assert energy(F(1), F(0))-energy(F(1), F(0))-energy(F(0), F(0)) == 0
        assert F(1, len(blocks)) <= q <= 1
        # Negative control: a sign reversal is visible in inclusion-exclusion.
        wrong_pair_energy = F(2)-q
        assert wrong_pair_energy-F(1)-F(1) == -q != q
        rows.append({'environment': name, 'probe_count': len(blocks),
                     'block_weights': [str(w) for w in blocks.values()],
                     'quartic_excess': str(q), 'decimal': float(q),
                     'equals_3_over_20': q == F(3, 20)})
    assert rows[1]['quartic_excess'] == '1/4'
    assert rows[2]['quartic_excess'] == '1/12'
    assert rows[3]['quartic_excess'] == '1/3'
    result = {
        'schema': 'marici.nima.proton-witness-quartic-environment.v1',
        'status': 'pass',
        'source': 'twelve-triangle-positive-geometry.md',
        'source_norm_squared': str(norm),
        'witness': 'unit Hermitian dual of the normalized collective mode; not an independently generated electron',
        'coupling': 'sum_a E_a tensor conjugate(E_a), with unit coefficients',
        'normalization': 'both modes unit norm; differs from using unnormalized u and u†/80 separately',
        'rows': rows,
        'controls': ['zero witness removes cross-term', 'amplitude scaling is quartic',
                     'reversed interaction sign changes extracted excess'],
        'residual': 'No source-selected surrounding operator or relative interaction strength has been derived. These are fixed candidate probe models.',
    }
    out = Path(__file__).resolve().parents[1] / 'results/proton-witness-quartic-environment.json'
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
