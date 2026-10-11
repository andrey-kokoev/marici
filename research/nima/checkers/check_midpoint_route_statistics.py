"""Exact finite route statistics; squared geometric cost is a test choice, not energy."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import POINTS, mean, dot, sub

ROOT = Path(__file__).resolve().parents[1]


def enumerate_routes(points, order):
    levels = [[mean([points[v] for v in order[:n]]) for n in range(1, 5)]]
    for _ in range(3):
        row = levels[-1]
        levels.append([mean(row[i:i+2]) for i in range(len(row)-1)])
    records = []
    for bits in product((0, 1), repeat=3):
        j = 0
        nodes = [levels[3][0]]
        for level, bit in zip((2, 1, 0), bits):
            j += bit
            nodes.append(levels[level][j])
        costs = [dot(sub(b, a), sub(b, a)) for a, b in zip(nodes, nodes[1:])]
        records.append(dict(route=''.join(map(str, bits)), stage=j,
                            nodes=nodes, edge_costs=costs, cost=sum(costs)))
    return levels, records


def main():
    reference = None
    assembly_costs = set()
    all_orders = []
    for order in permutations('ABCD'):
        levels, records = enumerate_routes(POINTS, order)
        cs = levels[0]
        assembly_costs.add(sum(dot(sub(b, a), sub(b, a)) for a, b in zip(cs, cs[1:])))
        counts = Counter(r['stage'] for r in records)
        assert counts == {0: 1, 1: 3, 2: 3, 3: 1}
        assert mean([r['nodes'][-1] for r in records]) == levels[-1][0]
        signature = [(r['route'], r['stage'], r['cost']) for r in records]
        if reference is None:
            reference = signature
            base_records = records
            base_levels = levels
        else:
            assert signature == reference
        all_orders.append(dict(order=''.join(order), expected_state=levels[-1][0]))
    assert assembly_costs == {F(3)}
    assert len({tuple(r['expected_state']) for r in all_orders}) == 24
    assert base_levels[-1][0] == (F(5, 8), F(1, 4), F(0))
    grouped = defaultdict(list)
    for r in base_records:
        grouped[r['stage']].append(r)
    unequal = [(a, b) for rs in grouped.values() for a in rs for b in rs
               if a['route'] < b['route'] and a['cost'] != b['cost']]
    assert unequal, 'Squared route cost unexpectedly descends to terminal stage'
    a, b = unequal[0]
    assert a['nodes'][0] == b['nodes'][0] and a['nodes'][-1] == b['nodes'][-1]
    costs = [r['cost'] for r in base_records]
    average = sum(costs)/8
    variance = sum((e-average)**2 for e in costs)/8
    assert variance > 0
    # Midpoint ancestry is a vector martingale under fair child selection.
    # Orthogonality in expectation (not on every path) makes the expected
    # accumulated squared displacement equal to terminal state variance.
    for depth in range(3):
        prefixes = defaultdict(list)
        for r in base_records:
            prefixes[r['route'][:depth]].append(r)
        for rs in prefixes.values():
            assert mean([r['nodes'][depth+1] for r in rs]) == rs[0]['nodes'][depth]
    root = base_levels[-1][0]
    terminal_variance = sum(dot(sub(r['nodes'][-1], root), sub(r['nodes'][-1], root))
                            for r in base_records)/8
    assert terminal_variance == average == F(27, 64)
    # Conditional mean replaces endpoint-only energy only at first order:
    # E[E^2|k] - E[E|k]^2 is an exact obstruction at second order in beta.
    conditional_variances = {}
    for k, rs in grouped.items():
        m = sum(r['cost'] for r in rs)/len(rs)
        conditional_variances[k] = sum((r['cost']-m)**2 for r in rs)/len(rs)
    assert conditional_variances[1] > 0 and conditional_variances[2] > 0
    # Alternative declared cost: a potential difference telescopes and DOES
    # descend to endpoint. Route dependence is cost-specific, not inevitable.
    for r in base_records:
        ns = r['nodes']
        telescoped = sum(dot(y, y)-dot(x, x) for x, y in zip(ns, ns[1:]))
        assert telescoped == dot(ns[-1], ns[-1])-dot(ns[0], ns[0])
    # Metric-scaling control: these costs have units of squared length.
    doubled = {k: tuple(2*x for x in v) for k, v in POINTS.items()}
    _, doubled_records = enumerate_routes(doubled, 'ABCD')
    assert all(s['cost'] == 4*r['cost'] for r, s in zip(base_records, doubled_records))
    result = dict(
        schema='marici.nima.midpoint-route-statistics.v1', status='pass',
        scope='24 regular-tetrahedron assembly orders; 8 midpoint ancestry routes per order',
        obligation='readout descent: does squared route cost factor through the terminal stage?',
        cost_choice='sum of squared Euclidean edge displacements; not a source-selected physical energy',
        assembly_costs=sorted(assembly_costs), route_multiplicities=dict(counts),
        route_cost_spectrum=dict(sorted(Counter(costs).items())),
        uniform_mean_cost=average, uniform_cost_variance=variance,
        terminal_state_variance=terminal_variance,
        midpoint_martingale='Fair child selection preserves conditional mean; expected accumulated squared displacement equals terminal state variance.',
        same_endpoint_counterexample=[a, b], conditional_variances=conditional_variances,
        routes=base_records, assembly_expected_states=all_orders,
        partition_function='Z(beta)=sum_route exp(-beta E_route); Z(0)=8',
        exact_zero_beta_derivatives={'Z': 8, 'Z_prime': -sum(costs),
                                     'Z_second': sum(e*e for e in costs)},
        entropy_identities={'route': '3 ln(2)', 'stage': '3 ln(2)-(3/4) ln(3)',
                            'route_given_stage': '(3/4) ln(3)'},
        controls=['telescoping potential cost descends to endpoint',
                  'doubling geometry multiplies squared costs by four',
                  'all 24 order changes preserve the route-cost table'],
        residual='No native WG cost-selection law, physical energy scale, temperature, heat exchange, dynamics or thermodynamic limit supplied.')

    def encode(obj):
        if isinstance(obj, F): return str(obj)
        if isinstance(obj, dict): return {str(k): encode(v) for k, v in obj.items()}
        if isinstance(obj, (tuple, list)): return [encode(v) for v in obj]
        return obj
    result = encode(result)
    (ROOT/'results/midpoint-route-statistics.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('routes', 'assembly_expected_states', 'same_endpoint_counterexample')}, indent=2))


if __name__ == '__main__':
    main()
