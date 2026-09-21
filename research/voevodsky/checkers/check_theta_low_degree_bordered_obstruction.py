"""Exact source identities; analytical consequences use linear column lifts.

Run: uv run --with sympy python research/voevodsky/checkers/check_theta_low_degree_bordered_obstruction.py
"""
from itertools import permutations
from pathlib import Path
import hashlib
import json
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/grothendieck'))
from theta_interval_signature import observe_route


def main():
    prior = json.loads((ROOT / 'research/voevodsky/results/theta-hidden-channel-transport.json').read_text())
    routes = list(permutations(range(4)))
    assert [list(w) for w in routes] == prior['route_order']
    signatures = [observe_route(w) for w in routes]
    keys = [sorted(set().union(*(set(sig[d]) for sig in signatures))) for d in range(5)]
    matrices = [sp.Matrix([[sig[d].get(k, 0) for sig in signatures] for k in keys[d]]) for d in range(5)]
    selected = [tuple(k) for k in prior['second_degree_coordinates']]
    S = matrices[2][[keys[2].index(k) for k in selected], :]
    parity = sp.Matrix(prior['parity_basis_K']).applyfunc(sp.Rational)
    assert S.shape == (18, 24) and S.rank() == 18
    assert parity.T * parity == 4 * sp.eye(6)
    assert S * parity == sp.zeros(18, 6)
    _, pivots = S.rref()
    inverse = S[:, list(pivots)].inv()
    relations = {}
    for d in range(4):
        R = matrices[d][:, list(pivots)] * inverse
        assert R * S == matrices[d]
        assert matrices[d] * parity == sp.zeros(len(keys[d]), 6)
        relations[str(d)] = {
            'coordinates': [list(k) for k in keys[d]],
            'rows': [[[j, str(R[i, j])] for j in range(18) if R[i, j] != 0]
                     for i in range(R.rows)],
            'all_coefficients_integral': all(x.q == 1 for x in R),
        }
    assert matrices[2].rank() == matrices[3].rank() == 18
    assert matrices[4].rank() == 24
    hidden_four = matrices[4] * parity
    assert hidden_four.rank() == 6
    selected_four = [keys[4].index(tuple(k)) for k in prior['fourth_degree_coordinates']]
    M = S.col_join(matrices[4][selected_four, :])
    assert abs(M.det()) == 1
    selected_hidden = hidden_four[selected_four, :]
    assert selected_hidden == sp.Matrix(prior['four_point_hidden_response_Q']).applyfunc(sp.Rational)
    center = sp.ones(24, 1) / 24
    plus, minus = center + parity[:, 0] / 48, center - parity[:, 0] / 48
    assert min(plus) > 0 and min(minus) > 0
    assert sum(plus) == sum(minus) == 1
    for d in range(4):
        assert matrices[d] * plus == matrices[d] * minus
    assert matrices[4] * plus != matrices[4] * minus
    parity_difference = parity.T * (plus - minus) / 2
    assert parity_difference == sp.eye(6)[:, 0] / 12
    result = {
        'schema': 'marici.voevodsky.theta-low-degree-bordered-obstruction.v1',
        'passed': True,
        'route_count': 24,
        'coordinate_counts': list(map(len, keys)),
        'degree_ranks': [m.rank() for m in matrices],
        'selected_two_point_coordinates': [list(k) for k in selected],
        'interpolation_route_columns': list(pivots),
        'identities': 'K_d = R_d S for d=0,1,2,3; S is the selected two-point matrix',
        'low_degree_common_kernel_dimension': 6,
        'four_point_parity_rank': 6,
        'strictly_positive_indistinguishable_mixtures': {
            'plus': [str(x) for x in plus],
            'minus': [str(x) for x in minus],
            'same_degrees': [0, 1, 2, 3],
            'different_degree': 4,
            'normalized_parity_difference': [str(x) for x in parity_difference],
        },
        'selected_completion_determinant': str(M.det()),
        'signature_implementation_sha256': hashlib.sha256((ROOT / 'research/grothendieck/theta_interval_signature.py').read_bytes()).hexdigest(),
        'relations': relations,
        'scope': 'Four-prime event-segmented packet; linear degreewise column lifts. No physical source adapter or observation-noise estimate certified.',
    }
    path = ROOT / 'research/voevodsky/results/theta-low-degree-bordered-obstruction.json'
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('relations', 'selected_two_point_coordinates')}, indent=2))


if __name__ == '__main__':
    main()
