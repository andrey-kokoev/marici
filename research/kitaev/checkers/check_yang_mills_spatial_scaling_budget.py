"""Exact lattice/budget controls; source cluster theorem remains an analytic input."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
from check_yang_mills_source_clustering import report as clustering_report
from check_yang_mills_parameterized_strong_map import report as predecessor_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-spatial-scaling-budget.v1.json'
NOTE = BASE+'yang-mills-spatial-scaling-budget-v1.md'
SELF = BASE+'checkers/check_yang_mills_spatial_scaling_budget.py'
OUT = ROOT/(BASE+'results/yang-mills-spatial-scaling-budget-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def add(v, axis):
    return tuple(x+int(i == axis) for i, x in enumerate(v))


def edge(a, b):
    return tuple(sorted([a, b]))


def plaquette(origin, axes):
    a, b = axes
    u, v = add(origin, a), add(origin, b)
    far = add(u, b)
    return [edge(origin, u), edge(u, far), edge(v, far), edge(origin, v)]


def report():
    c = json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    require(c['batch'] == {'kind': 'spatial-scaling', 'iteration': 1, 'size': 10}, 'batch provenance')
    require(all(v is False for v in c['boundary'].values()), 'scope')
    require(c['net_update']['ready_frontier'] == ['macroscopic-loop-normalization-audit'] and c['net_update']['parent_outcome'] is None, 'executable observer-boundary continuation')
    source = clustering_report()
    source_path = BASE+'results/yang-mills-source-clustering-v1.json'
    require(source['passed'] and source == json.loads((ROOT/source_path).read_text()), 'fresh source clustering controls,not analytic certification')
    previous = predecessor_report()
    previous_path = BASE+'results/yang-mills-parameterized-strong-map-v1.json'
    require(previous['passed'] and previous == json.loads((ROOT/previous_path).read_text()), 'fresh completed predecessor and unchanged frozen evidence')
    counts = {}
    count = 0
    for axes in combinations(range(3), 2):
        edges = plaquette((0, 0, 0), axes)
        midpoints = [tuple(F(x+y, 2) for x, y in zip(u, v)) for u, v in edges]
        for p, q in product(midpoints, repeat=2):
            require(sum((x-y)**2 for x, y in zip(p, q)) <= 1, 'one link-graph step moves physical midpoint at most one spacing')
            count += 1
    counts['actual_midpoint_geometry_packets'] = count
    count = 0
    for N in [2, 3, 4]:
        squares = []
        for origin in product(range(N+1), repeat=3):
            for axes in combinations(range(3), 2):
                if all(origin[axis] < N for axis in axes):
                    squares.append((origin, plaquette(origin, axes)))
        incidence = Counter(e for _, square in squares for e in square)
        require(len(squares) == 3*(N+1)*N*N, 'actual plaquette count')
        require(len(incidence) == 3*(N+1)**2*N, 'actual edge count')
        require(max(incidence.values()) <= 4 and sum(incidence.values()) == 4*len(squares), 'actual source incidence')
        for Z, signed in product([F(1), F(N**4)], [False, True]):
            coefficients = [Z*F(1, N**3)*((-1)**sum(o) if signed else 1) for o, _ in squares]
            link_upper = {}
            for (_, square), coefficient in zip(squares, coefficients):
                for e in square:
                    link_upper[e] = link_upper.get(e, F(0))+2*abs(coefficient)
            oscillation_upper = sum(link_upper.values())
            require(oscillation_upper == 8*sum(map(abs, coefficients)), 'plaquette-smear triangle oscillation bound')
            require(oscillation_upper <= 48*Z, 'unit-region integrated budget is O(Z),not O(volume*Z)')
            require(F(1, N**3)*len(squares) == 3*(1+F(1, N)) <= 6, 'correct h^3 normalization')
            count += 1
    counts['actual_plaquette_incidence_budget_packets'] = count
    count = 0
    max_level = 0
    q = F(3, 4)
    for power, separation_index, amplitude, tolerance in product([0, 2, 8, 16], [1, 2, 4], [F(1), F(2304)], [F(1, 100), F(1, 1000000)]):
        # Physical spacing h=1/(2N),separation r=separation_index/2.
        base = q**separation_index
        N0 = 1
        while (1+F(1, N0))**power*base > F(7, 8):
            N0 += 1
        N = N0
        envelope = lambda n: amplitude*F((2*n)**power)*base**n/28
        while envelope(N) > tolerance:
            N += 1
        require(envelope(N) <= tolerance and (N == N0 or envelope(N-1) > tolerance), 'least sufficient tail level beyond monotonicity threshold')
        require((1+F(1, N))**power*base <= F(7, 8), 'all subsequent integer levels have a geometric tail envelope')
        max_level = max(max_level, N)
        count += 1
    counts['polynomial_tail_planners'] = count
    count = 0
    for budget_base, distance_index, N in product([F(1), F(4, 3), F(16, 9), F(256, 81)], [1, 2, 4], [1, 2, 4, 8]):
        ratio = budget_base*q**distance_index
        envelope = budget_base**N*q**(distance_index*N)/28
        require(envelope == ratio**N/28, 'exact exponential budget/decay competition')
        if ratio < 1:
            require(envelope < F(1, 28), 'vanishing envelope class')
        elif ratio == 1:
            require(envelope == F(1, 28), 'threshold is not forced to vanish by this estimate')
        else:
            require(envelope > F(1, 28), 'growing upper envelope is inconclusive,not actual survival')
        count += 1
    counts['exponential_envelope_classifications'] = count
    count = 0
    rho = F(1, 64)
    for N in range(1, 13):
        distance = 2*N
        law = {(s, t): (1+rho**distance*s*t)/4 for s, t in product([-1, 1], repeat=2)}
        require(sum(law.values()) == 1 and all(p > 0 for p in law.values()), 'positive endpoint law of the stationary binary chain')
        require(sum(s*p for (s, t), p in law.items()) == sum(t*p for (s, t), p in law.items()) == 0, 'centered endpoint spins')
        bare_covariance = sum(s*t*p for (s, t), p in law.items())
        Z = rho**(-N)
        require(bare_covariance == rho**distance and Z**2*bare_covariance == 1, 'exponential normalization can keep one separated reader nonzero')
        require(Z**2*rho**N == rho**(-N) and Z**2*rho**(4*N) == rho**(2*N), 'other physical separations do not establish a finite continuum packet')
        require(Z**2*bare_covariance <= 4*Z**2*q**distance/28, 'counterfixture is compatible with the stated upper envelope')
        count += 1
    counts['positive_chain_normalization_controls'] = count
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 168, 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, source_path, previous_path]
    paths += [BASE+name for name in [
        'yang-mills-source-clustering-v1.md', 'contracts/yang-mills-source-clustering.v1.json',
        'checkers/check_yang_mills_source_clustering.py', 'yang-mills-thermodynamic-vacuum-v1.md',
        'yang-mills-physical-scaling-obstruction-v1.md', 'contracts/yang-mills-gap-net.v2.json']]
    return {
        'schema': 'marici.yang-mills-spatial-scaling-budget.result.v1', 'passed': True,
        'strength': 'written conditional clock-independent spatial budget theorem for specified multiplication readers; no universal continuum/triviality claim',
        'coverage': counts, 'new_exact_controls': 168,
        'source_clustering_receipt_fresh': True,
        'predecessor_R4_controls_freshly_replayed': previous['new_exact_controls'],
        'unit_box_plaquette_budget_coefficient': '48',
        'pair_h_minus_four_budget_coefficient': '2304',
        'largest_sufficient_integer_tail_level': max_level,
        'exponential_normalization_counterreader': '1',
        'independent_analytic_review_complete': False,
        'all_exponential_loop_normalizations_excluded': False,
        'physical_continuum_or_Yang_Mills_root_discharged': False,
        'next_executable': 'macroscopic-loop-normalization-audit',
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, indent=2))
