"""Prime-labelled online window recorder, independently matched to signatures.

Run: uv run --with sympy python research/voevodsky/checkers/check_arithmetic_window_signature_adapter.py
No terminal route lookup is used by the recorder. History storage is explicit.
"""
from itertools import combinations, permutations
from math import prod
from pathlib import Path
import json
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/grothendieck'))
from theta_interval_signature import observe_route

PRIMES = (2, 3, 5, 7)
ENDPOINTS = sorted(2 * prod(subset) for k in range(5) for subset in combinations(PRIMES, k))


def initial():
    return ({(): 1}, {}, {}, {}, {})


def event_window(n, p):
    """Independent arithmetic definition: chambers contained in [log n,log np]."""
    if p not in PRIMES or n not in ENDPOINTS or n * p not in ENDPOINTS or (n // 2) % p == 0:
        raise ValueError('Prime is not an unused factor at this source label')
    return tuple(i for i, (a, b) in enumerate(zip(ENDPOINTS, ENDPOINTS[1:])) if n <= a and b <= n * p)


def step(n, history, p):
    window = event_window(n, p)
    out = tuple(dict(level) for level in history)
    # Each event contributes at most one tensor letter.
    for d in range(1, 5):
        for prefix, coefficient in history[d-1].items():
            for i in window:
                key = prefix + (i,)
                out[d][key] = out[d].get(key, 0) + coefficient
    return n * p, out


def record(n, word):
    state = initial()
    for p in word:
        n, state = step(n, state, p)
    return n, state


def aggregate(states, weights):
    out = tuple({} for _ in range(5))
    for state, weight in zip(states, weights):
        for d, level in enumerate(state):
            for key, coefficient in level.items():
                out[d][key] = out[d].get(key, 0) + weight * coefficient
    return tuple({k: v for k, v in level.items() if v} for level in out)


def main():
    comparisons = 0
    for mask in range(16):
        n = 2 * prod(PRIMES[j] for j in range(4) if mask >> j & 1)
        unused = [j for j in range(4) if not mask >> j & 1]
        for length in range(len(unused)+1):
            for word in permutations(unused, length):
                terminal, got = record(n, [PRIMES[j] for j in word])
                assert terminal == n * prod(PRIMES[j] for j in word)
                assert got == observe_route(word, start=mask)
                comparisons += 1
    assert comparisons == 168
    routes = list(permutations(range(4)))
    histories = [record(2, [PRIMES[j] for j in w])[1] for w in routes]
    prior = json.loads((ROOT / 'research/voevodsky/results/theta-hidden-channel-transport.json').read_text())
    assert [list(w) for w in routes] == prior['route_order']
    coordinates = [tuple(x) for x in prior['second_degree_coordinates']] + [tuple(x) for x in prior['fourth_degree_coordinates']]
    degrees = [2] * 18 + [4] * 6
    M = sp.Matrix([[state[d].get(key, 0) for state in histories] for key, d in zip(coordinates, degrees)])
    assert M.det() == 1
    parity = sp.Matrix(prior['parity_basis_K']).applyfunc(sp.Rational)
    B = parity.T / 2
    R = sp.Matrix(prior['theta_readout_R2']).applyfunc(sp.Rational).row_join(sp.Matrix(prior['theta_readout_R4']).applyfunc(sp.Rational))
    assert R * M == B

    # The two-step arithmetic base commutes, but its history extension does not.
    final_pq, pq = record(2, [2, 3])
    final_qp, qp = record(2, [3, 2])
    assert final_pq == final_qp == 12
    assert pq[0] == qp[0] and pq[1] == qp[1]
    assert pq[2] != qp[2]
    difference = {k: pq[2].get(k, 0) - qp[2].get(k, 0) for k in set(pq[2]) | set(qp[2])}
    difference = {k: v for k, v in difference.items() if v}

    plus = [sp.Rational(1, 24) + parity[j, 0]/48 for j in range(24)]
    minus = [sp.Rational(1, 24) - parity[j, 0]/48 for j in range(24)]
    obs_plus, obs_minus = aggregate(histories, plus), aggregate(histories, minus)
    assert all(obs_plus[d] == obs_minus[d] for d in range(4))
    assert obs_plus[4] != obs_minus[4]
    assert B * (sp.Matrix(plus)-sp.Matrix(minus)) == sp.eye(6)[:, 0]/12
    for n, p in ((4, 2), (2, 11), (420, 2)):
        try:
            event_window(n, p)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid source transition accepted')
    result = {
        'schema': 'marici.voevodsky.arithmetic-window-signature-adapter.v1',
        'passed': True,
        'endpoints': ENDPOINTS,
        'source_path_comparisons': comparisons,
        'runtime_input': 'current integer n, arriving prime p, retained truncated tensor history',
        'update': '(n,z) -> (np,z*(1+v(n,p))) in the truncated noncommutative tensor algebra',
        'selected_measurement_determinant': str(M.det()),
        'parity_reconstruction': 'R M = K^T/2 exactly',
        'two_step_base_terminal': final_pq,
        'two_step_degree_two_history_difference': [[list(k), v] for k, v in sorted(difference.items())],
        'positive_collision_separated_at_degree': 4,
        'normalized_parity_difference': ['1/12', '0', '0', '0', '0', '0'],
        'source_strength': 'online arithmetic history extension, conditional on event access and retained record memory',
        'base_only_natural_section': False,
        'physical_event_access_or_calibration_certified': False,
    }
    out = ROOT / 'research/voevodsky/results/arithmetic-window-signature-adapter.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
