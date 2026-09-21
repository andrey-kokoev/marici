#!/usr/bin/env python3
"""Exact realization and minimality certificates for six route-correlation probes.

uv run --with sympy python research/voevodsky/checkers/check_four_prime_correlation_observer.py
"""
import itertools
import json
import sys
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'research/voevodsky'))
from four_prime_correlation_observer import (PROBES, EdgeStreamObserver,
    EndpointCorrelationObserver, observe_route, observe_mixture)
prior = ROOT/'research/nima/results/prime-cube-path-observer-reconstruction.json'
data = json.loads(prior.read_text())
probes = [(tuple(p['first_edge']), tuple(p['second_edge']))
          for p in data['four_prime_hostile']['selected_probes']]
assert len(probes) == 6 and tuple(probes) == PROBES
edges = [(v, v | (1 << j), j) for v in range(16) for j in range(4) if not v & (1 << j)]
paths = []
for v in range(16):
    available = [j for j in range(4) if not v & (1 << j)]
    for k in range(len(available)+1):
        paths.extend((v, w) for w in itertools.permutations(available, k))


def end(p):
    return p[0] | sum(1 << j for j in p[1])


def word(p):
    v = p[0]
    out = []
    for j in p[1]:
        w = v | (1 << j)
        out.append((v, w, j))
        v = w
    return out


def direct(ww):
    return s.Matrix([sum(1 for j in range(len(ww)) for k in range(j+1, len(ww))
                         if ww[j] == a and ww[k] == b) for a, b in probes])


# State: constant, six first-event memories, six accumulated outputs.
vacuum = s.eye(13)[:, 0]
C = s.zeros(6, 13)
for i in range(6):
    C[i, 7+i] = 1
U = {}
for e in edges:
    A = s.eye(13)
    for i, (a, b) in enumerate(probes):
        if e == a:
            A[1+i, 0] += 1
        if e == b:
            A[7+i, 1+i] += 1
    U[e] = A


def transition(ww):
    A = s.eye(13)
    for e in ww:
        A = U[e]*A
    return A


def evaluate(ww):
    return C*transition(ww)*vacuum


# Full free-monoid reachability: empty, a_i, a_i b_i.
reach_words = [[]]+[[a] for a, b in probes]+[[a, b] for a, b in probes]
R = s.Matrix.hstack(*(transition(w)*vacuum for w in reach_words))
# Observable rows: empty/output i; suffix b_i/output i; suffix a_0 b_0/output 0.
obs = [(i, []) for i in range(6)]+[(i, [b]) for i, (a, b) in enumerate(probes)]+[(0, list(probes[0]))]
O = s.Matrix.vstack(*(C[i, :]*transition(w) for i, w in obs))
Hfree = O*R

# Endpoint-conditioned minimal state bundle: retain only future-observable reachable coordinates.
coordinates = {}
for v in range(16):
    if v == 0 or any(a[0] == v for a, b in probes):
        coords = [0]
    elif v.bit_count() == 2:
        coords = [1+i for i, (a, b) in enumerate(probes) if a[1] == v]
    elif v.bit_count() == 3:
        coords = [7+i for i, (a, b) in enumerate(probes) if b[1] == v]
    elif v == 15:
        coords = list(range(7, 13))
    else:
        coords = []
    coordinates[v] = coords
inclusions = {v: s.eye(13)[:, coords] if coords else s.zeros(13, 0)
              for v, coords in coordinates.items()}
restrictions = {v: E.T for v, E in inclusions.items()}
initial = {v: restrictions[v]*vacuum for v in range(16)}
readout = {v: C*inclusions[v] for v in range(16)}
T = {e: restrictions[e[1]]*U[e]*inclusions[e[0]] for e in edges}


def bundle(p):
    v = p[0]
    state = initial[v]
    for e in word(p):
        state = T[e]*state
        v = e[1]
    return readout[v]*state


# Typed Hankel H_v: rows (suffix starting at v, output), columns prefixes ending at v.
# Prefixes may start at any vertex, matching the reset contract.
ranks = {}
for v in range(16):
    prefixes = [p for p in paths if end(p) == v]
    suffixes = [q for q in paths if q[0] == v]
    columns = []
    for p in prefixes:
        values = []
        for q in suffixes:
            values.extend(direct(word(p)+word(q)))
        columns.append(s.Matrix(values))
    Hv = s.Matrix.hstack(*columns)
    ranks[v] = {'hankel_rank': Hv.rank(), 'state_dimension': len(coordinates[v]),
                'prefix_count': len(prefixes), 'suffix_count': len(suffixes)}

# Collision from the preceding packet, observed as two mixtures with equal edge response.
positive = [(0, (0, 1, 2, 3)), (0, (1, 0, 3, 2))]
negative = [(0, (0, 1, 3, 2)), (0, (1, 0, 2, 3))]
edge_index = {e: i for i, e in enumerate(edges)}


def chain(p):
    v = s.zeros(32, 1)
    for e in word(p):
        v[edge_index[e]] += 1
    return v


chain_plus = sum((chain(p) for p in positive), s.zeros(32, 1))
chain_minus = sum((chain(p) for p in negative), s.zeros(32, 1))
out_plus = sum((bundle(p) for p in positive), s.zeros(6, 1))
out_minus = sum((bundle(p) for p in negative), s.zeros(6, 1))
full_paths = [p for p in paths if p[0] == 0 and end(p) == 15]
completed = s.Matrix.hstack(*(chain(p).col_join(bundle(p)) for p in full_paths))
recovery = (completed.T*completed).inv()*completed.T

# Non-path strings check that the autonomous signature observer also handles repetition.
repeated = [[probes[i][0], probes[i][0], probes[i][1], probes[i][1]] for i in range(6)]

# Composition for every admissible cut, tested before final readout.
composition_ok = True
for p in paths:
    for q in paths:
        if end(p) != q[0]:
            continue
        joined = word(p)+word(q)
        composition_ok &= transition(joined) == transition(word(q))*transition(word(p))

def streaming_full(ww):
    observer = EdgeStreamObserver()
    for edge in ww:
        observer = observer.step(edge)
    return s.Matrix(observer.output)

packet_readout = s.Matrix.hstack(*(direct(word(p)) for p in paths))
full_readout = s.Matrix.hstack(*(direct(word(p)) for p in full_paths))
invalid_steps_rejected = True
for start, j in [(1, 0), (15, 2), (0, -1), (0, 4)]:
    try:
        EndpointCorrelationObserver.start(start).step(j)
        invalid_steps_rejected = False
    except ValueError:
        pass

checks = {
    'all_168_path_outputs_match_ordered_pair_counts': all(evaluate(word(p)) == direct(word(p)) for p in paths),
    'repeated_events_count_all_ordered_pairs': all(evaluate(w) == direct(w) for w in repeated),
    'free_stream_reachable_rank_13': R.rank() == 13,
    'free_stream_observable_rank_13': O.rank() == 13,
    'free_stream_hankel_rank_13': Hfree.rank() == 13,
    'all_cube_path_bundle_outputs_correct': all(bundle(p) == direct(word(p)) for p in paths),
    'typed_hankel_ranks_match_every_state_space': all(r['hankel_rank'] == r['state_dimension'] for r in ranks.values()),
    'typed_total_dimension_22_peak_6': sum(len(c) for c in coordinates.values()) == 22
        and max(len(c) for c in coordinates.values()) == 6,
    'every_admissible_cut_preserves_transition_composition': composition_ok,
    'equal_edge_mixtures': chain_plus == chain_minus,
    'correlation_output_separates_mixtures': out_plus != out_minus,
    'operator_completed_observer_rank_24': completed.rank() == 24,
    'operator_completed_observer_exact_inverse': recovery*completed == s.eye(24),
    'streaming_implementation_all_paths': all(s.Matrix(observe_route(p[1], p[0])) == direct(word(p)) for p in paths),
    'unrestricted_streaming_implementation': all(streaming_full(w) == direct(w)
        for w in repeated+[word(p) for p in paths]),
    'streaming_mixture_separates_collision': observe_mixture([(1,p[0],p[1]) for p in positive])
        != observe_mixture([(1,p[0],p[1]) for p in negative]),
    'invalid_cube_steps_rejected': invalid_steps_rejected,
    'all_route_probe_gram_is_four_identity': packet_readout*packet_readout.T == 4*s.eye(6),
    'full_route_probe_gram_is_identity': full_readout*full_readout.T == s.eye(6),
}
checks = {k: bool(v) for k, v in checks.items()}
out = {
    'schema': 'marici.voevodsky.four-prime-correlation-observer.v1',
    'source_result': str(prior.relative_to(ROOT)),
    'arithmetic': 'exact rational',
    'checks': checks, 'passed': all(checks.values()),
    'free_stream': {'homogeneous_state_dimension': 13, 'dynamic_coordinates_with_fixed_unit': 12,
                    'reachability_rank': R.rank(), 'observability_rank': O.rank(), 'hankel_rank': Hfree.rank()},
    'endpoint_bundle': {'ranks': ranks, 'retained_coordinates': coordinates,
                        'total_fiber_dimension': sum(len(c) for c in coordinates.values()),
                        'peak_fiber_dimension': max(len(c) for c in coordinates.values())},
    'collision_outputs': {'positive': [int(x) for x in out_plus], 'negative': [int(x) for x in out_minus]},
    'completed_path_rank': completed.rank(),
    'counting_metric_operator_norms': {'all_routes': 2, 'full_routes': 1},
    'scope': 'Linear switched observer and endpoint-typed linear realization. New probes read the route before additive theta/edge aggregation. No implementation of a new theta measurement is claimed.',
}
path = ROOT/'research/voevodsky/results/four-prime-correlation-observer.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
raise SystemExit(0 if out['passed'] else 1)
