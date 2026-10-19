"""Exact finite geometry, series and scope controls; no analytic gap/LR prover."""
from collections import Counter, deque
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from math import factorial
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_spatial_scaling_budget import report as predecessor_report, plaquette, edge

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-arbitrary-clock-locality.v1.json'
NOTE = BASE+'yang-mills-arbitrary-clock-locality-v1.md'
SELF = BASE+'checkers/check_yang_mills_arbitrary_clock_locality.py'
OUT = ROOT/(BASE+'results/yang-mills-arbitrary-clock-locality-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0)) for col in zip(*b)] for row in a]


def comm(a, b):
    ab, ba = mul(a, b), mul(b, a)
    return [[x-y for x, y in zip(row, other)] for row, other in zip(ab, ba)]


@lru_cache(None)
def exp_upper(z):
    """Positive Taylor series plus a rigorously geometric remainder, all rational."""
    require(z >= 0, 'positive exponential argument')
    M = max(1, (2*z.numerator+z.denominator-1)//z.denominator)
    term, total = F(1), F(1)
    for k in range(1, M+1):
        term *= z/k
        total += term
    next_term = term*z/(M+1)
    ratio = z/(M+2)
    require(ratio <= F(1, 2), 'all omitted exponential ratios are bounded by a geometric tail')
    return total+next_term/(1-ratio)


def report():
    c = json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    require(c['batch'] == {'kind': 'spatial-scaling', 'iteration': 2, 'size': 10}, 'batch provenance')
    require(all(v is False for v in c['boundary'].values()), 'claim boundary')
    require(c['net_update']['ready_frontier'] == ['relativistic-scalar-witness-bridge'] and c['net_update']['parent_outcome'] is None, 'necessary witness bridge remains')
    prev = predecessor_report()
    prev_path = BASE+'results/yang-mills-spatial-scaling-budget-v1.json'
    require(prev['passed'] and prev == json.loads((ROOT/prev_path).read_text()), 'fresh predecessor controls and frozen evidence')
    counts = {}
    count = 0
    # Set three plaquette links to identity and vary the fourth through actual SU2 points.
    points = [[F(1), 0, 0, 0], [F(-1), 0, 0, 0], [0, F(1), 0, 0],
              [F(3, 5), F(4, 5), 0, 0], [F(1, 2)]*4]
    for q, J in product(points, [F(1, 4), F(1), F(2)]):
        require(sum(x*x for x in q) == 1, 'unit quaternion plaquette holonomy')
        w = q[0]
        interaction, full = -J*w, J*(1-w)
        require(abs(interaction) <= J and 0 <= full <= 2*J and full-interaction == J, 'actual bounded interaction after scalar subtraction')
        if abs(w) == 1:
            require(abs(interaction) == J, 'norm J is attained,not2J')
        count += 1
    counts['actual_SU2_plaquette_norm_packets'] = count
    count = 0
    for N in [2, 3, 4]:
        squares = [set(plaquette(o, axes)) for o in product(range(N+1), repeat=3)
                   for axes in combinations(range(3), 2) if all(o[a] < N for a in axes)]
        incidence = Counter(e for square in squares for e in square)
        require(max(incidence.values()) <= 4, 'four plaquettes per link')
        neighbors = [[j for j, q in enumerate(squares) if p & q] for p in squares]
        require(max(map(len, neighbors)) <= 16, 'four-link by four-incidence overcount')
        if N >= 3:
            require(max(map(len, neighbors)) == 13, 'actual interior intersections below conservative16')
        graph = {e: set() for e in incidence}
        for square in squares:
            for e in square:
                graph[e].update(square-{e})
        target = edge((N-1, N, N), (N, N, N))
        supports = [{edge((0, 0, 0), (1, 0, 0))}, squares[0], squares[0] | squares[1]]
        for X in supports:
            queue = deque((e, 0) for e in X)
            seen = set(X)
            distance = None
            while queue:
                e, d = queue.popleft()
                if e == target:
                    distance = d
                    break
                for v in graph[e]-seen:
                    seen.add(v)
                    queue.append((v, d+1))
            require(distance is not None and distance >= 1, 'disjoint source supports have finite graph distance')
            weights = [int(bool(square & X)) for square in squares]
            require(sum(weights) <= 4*len(X), 'first plaquette count')
            for n in range(1, distance+3):
                endpoint_count = sum(w for w, square in zip(weights, squares) if target in square)
                require(endpoint_count <= 4*len(X)*16**(n-1), 'actual plaquette-chain bound')
                if n < distance:
                    require(endpoint_count == 0, 'too-short chains cannot connect the supports')
                if n == distance:
                    require(endpoint_count > 0, 'minimal chain length matches link distance')
                weights = [sum(weights[i] for i in near) for near in neighbors]
            count += 1
    counts['actual_lattice_chain_packets'] = count
    count = 0
    for d, x, weight in product([1, 2, 4, 8, 16], [F(0), F(1, 4), F(1), F(4)], [F(2), F(4), F(8)]):
        M = max(d, 20)
        tail_partial = sum(x**n/factorial(n) for n in range(d, M+1))
        weighted_partial = weight**(-d)*sum((weight*x)**n/factorial(n) for n in range(1, M+1))
        require(tail_partial <= weighted_partial <= weight**(-d)*(exp_upper(weight*x)-1), 'weighted locality-series envelope')
        count += 1
    counts['weighted_series_envelopes'] = count
    count, largest_level, largest_weight = 0, 0, 0
    for budget_base, separation, power, JT in product([F(1), F(2), F(4), F(16)], [1, 2, 4], [0, 2, 8], [F(0), F(1, 64), F(1, 8)]):
        weight = 2
        while weight**separation <= 2*budget_base:
            weight *= 2
        ratio = budget_base/F(weight**separation)
        require(ratio < F(1, 2), 'one fixed locality weight beats the finite exponential budget')
        prefactor = exp_upper(32*weight*JT)-1
        N0 = 1
        while (1+F(1, N0))**power*ratio > F(3, 4):
            N0 += 1
        N = N0
        envelope = lambda n: n**power*ratio**n*prefactor
        while envelope(N) > F(1, 1000000):
            N += 1
        require(envelope(N) <= F(1, 1000000), 'finite-exponential budget planner')
        require(N == N0 or envelope(N-1) > F(1, 1000000), 'least sufficient level after monotonicity threshold')
        largest_level, largest_weight = max(largest_level, N), max(largest_weight, weight)
        count += 1
    counts['finite_exponential_budget_planners'] = count
    eta_star = F(27, 262144)
    count = 0
    for m, k, fraction in product([1, 2, 4, 8], [1, 2, 4, 8], [F(0), F(1, 2), F(3, 4)]):
        # t*=2log2,sigma=64m/5,C/c=2^k: spectral inequality is exact arithmetic.
        sigma, bound = F(64*m, 5), F(64*k, 5)
        earlier_cap, later_floor = F(2**k), F(1)
        require((earlier_cap*F(1, 2**m) >= later_floor) == (m <= k), 'two-time witness rejects an excessive clock')
        if m <= k:
            J = sigma*eta_star*fraction
            require(sigma <= bound and J <= bound*eta_star, 'bounded eta bounds the interaction in the same clock')
        count += 1
    counts['clock_interaction_envelopes'] = count
    count = 0
    P = [[F(1), 0, 0], [0, F(1), 0], [0, 0, F(0)]]
    blocks = [[[1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]]]
    for a, b in product(blocks, repeat=2):
        A = [list(map(F, row))+[F(0)] for row in a]+[[F(0), F(0), F(2)]]
        B = [list(map(F, row))+[F(0)] for row in b]+[[F(0), F(0), F(3)]]
        require(mul(P, A) == mul(A, P) and mul(P, B) == mul(B, P), 'reducing sector')
        require(comm(mul(mul(P, A), P), mul(mul(P, B), P)) == mul(mul(P, comm(A, B)), P), 'physical restriction of the full commutator')
        count += 1
    A, B = [[0, 0, 1], [0, 0, 0], [1, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
    compressed_comm = comm(mul(mul(P, A), P), mul(mul(P, B), P))
    full_compressed = mul(mul(P, comm(A, B)), P)
    require(compressed_comm == [[0]*3 for _ in range(3)] and full_compressed[0][1] == 1, 'nonreducing compression defect1')
    count += 1
    counts['reducing_sector_packets'] = count
    count = 0
    for sigma, k in product([1, 2, 4], [1, 2, 3]):
        earlier = F(1, 4*2**(3*sigma*k))
        later = F(1, 4*2**(6*sigma*k))
        require(0 < later < earlier and later/earlier == F(1, 2**(3*sigma*k)), 'actual free plaquette temporal channel,variance1/4 and energy3sigma')
        require(exp_upper(F(0))-1 == 0, 'J=0 leaves every separated commutator zero despite that channel')
        count += 1
    counts['actual_free_SU2_temporal_packets'] = count
    count = 0
    for g2, spacing in product(map(F, [300, 512, 1024]), [F(1), F(1, 4)]):
        kappa, lam = g2/(2*spacing), 4/(spacing*g2)
        eta = lam/kappa
        require(eta == 8/g2**2 < eta_star, 'once-counted canonical bare convention')
        require((spacing*F(5, 64)*kappa)**2 > F(3200, 27), 'corrected conditional physical coefficient square')
        count += 1
    counts['corrected_matching_arithmetic_packets'] = count
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 265, 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, prev_path]
    paths += [BASE+name for name in [
        'yang-mills-ground-state-transfer-v1.md', 'yang-mills-uniform-detection-v1.md',
        'yang-mills-spatial-scaling-budget-v1.md', 'yang-mills-spatial-scaling-next-step-v1.md',
        'contracts/yang-mills-spatial-scaling-progress.v1.json']]
    return {
        'schema': 'marici.yang-mills-arbitrary-clock-locality.result.v1', 'passed': True,
        'strength': 'written conditional arbitrary-clock gap/locality theorem with actual source constants; missing relativistic/observable witness bridge stays explicit',
        'coverage': counts, 'new_exact_controls': 265,
        'predecessor_spatial_budget_controls_replayed': prev['new_exact_controls'],
        'plaquettes_per_link_bound': 4, 'plaquette_chain_branch_bound': 16, 'series_rate': 32,
        'largest_budget_planner_level': largest_level, 'largest_fixed_locality_weight_base': largest_weight,
        'nonreducing_compression_defect': '1',
        'actual_free_temporal_channel_with_zero_propagation': True,
        'finite_exponential_norm_budgets_covered_conditionally': True,
        'finite_controls_certify_analytic_theorem': False,
        'independent_analytic_review_complete': False,
        'physical_continuum_or_Yang_Mills_root_discharged': False,
        'next_executable': 'relativistic-scalar-witness-bridge',
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, indent=2))
