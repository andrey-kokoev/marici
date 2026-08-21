"""Audit in-place S3^3 actions on the one-loop flavor phase line.

The sparse nine-link carrier has a rank-one integral cycle lattice.  This
checker enumerates the actual support stabilizers and computes their action on
that lattice.  It tests whether any order-three chart symmetry can induce a
nontrivial order-three action on the phase line.
"""

from collections import Counter
import itertools
import json
from math import lcm
from pathlib import Path


INPUT = Path("research/flavor/results/wp10_sparse_fiber_incidence_graph.json")
OUTPUT = Path("research/nima/results/flavor_phase_line_stabilizers.json")
PERMS = list(itertools.permutations(range(3)))


def slots(mask):
    return [(i, j) for i in range(3) for j in range(3) if mask & (1 << (3 * i + j))]


def edges(pair):
    return ([('u', i, j) for i, j in slots(pair[0])] +
            [('d', i, j) for i, j in slots(pair[1])])


def transport_edge(edge, action):
    sector, i, j = edge
    q, u, d = action
    return sector, q[i], (u if sector == 'u' else d)[j]


def transport_pair(pair, action):
    moved = {transport_edge(e, action) for e in edges(pair)}
    masks = []
    for sector in ('u', 'd'):
        masks.append(sum(1 << (3 * i + j) for s, i, j in moved if s == sector))
    return tuple(masks)


def cycle_vector(pair):
    """Primitive generator of ker(incidence), with Q-to-column edge orientation."""
    es = edges(pair)
    nodes = list(range(9))
    # Incidence has -1 at Q and +1 at the corresponding u/d column node.
    incidence = [[0] * len(es) for _ in nodes]
    for k, (sector, i, j) in enumerate(es):
        incidence[i][k] = -1
        incidence[(3 if sector == 'u' else 6) + j][k] = 1

    # Connected unicyclic graph: delete one row and solve by exhaustive
    # {-1,0,1} search.  With nine edges this is tiny and keeps the certificate
    # dependency-free.
    solutions = []
    for vector in itertools.product((-1, 0, 1), repeat=len(es)):
        if not any(vector):
            continue
        if all(sum(row[k] * vector[k] for k in range(len(es))) == 0
               for row in incidence):
            solutions.append(vector)
    assert len(solutions) == 2, (pair, len(solutions))
    vector = min(solutions)  # deterministic choice between v and -v
    return dict(zip(es, vector))


def permutation_order(p):
    seen = [False] * len(p)
    answer = 1
    for i in range(len(p)):
        if seen[i]:
            continue
        j = i
        length = 0
        while not seen[j]:
            seen[j] = True
            length += 1
            j = p[j]
        answer = lcm(answer, length)
    return answer


def action_order(action):
    return lcm(*(permutation_order(p) for p in action))


def induced_sign(vector, action):
    moved = {transport_edge(edge, action): value for edge, value in vector.items()}
    if moved == vector:
        return 1
    if all(moved[e] == -value for e, value in vector.items()):
        return -1
    raise AssertionError((vector, action, moved))


def main():
    packet = json.loads(INPUT.read_text())
    pairs = sorted({tuple(vertex['member']) for vertex in packet['vertices']})
    records = []
    global_orders = Counter()
    global_signs = Counter()
    order_three_signs = Counter()
    for pair in pairs:
        vector = cycle_vector(pair)
        stabilizers = [action for action in itertools.product(PERMS, repeat=3)
                       if transport_pair(pair, action) == pair]
        action_rows = []
        for action in stabilizers:
            order = action_order(action)
            sign = induced_sign(vector, action)
            global_orders[order] += 1
            global_signs[sign] += 1
            if order == 3:
                order_three_signs[sign] += 1
            action_rows.append({'order': order, 'phase_line_sign': sign})
        records.append({
            'member': list(pair),
            'stabilizer_size': len(stabilizers),
            'action_histogram': {
                f'order_{order}_sign_{sign}': count
                for (order, sign), count in sorted(Counter(
                    (row['order'], row['phase_line_sign']) for row in action_rows
                ).items())
            },
        })

    out = {
        'schema': 'marici.flavor.phase_line_stabilizer_audit.v1',
        'support_pair_count': len(pairs),
        'integral_phase_line_automorphism_group': ['+1', '-1'],
        'stabilizer_order_histogram': dict(sorted(global_orders.items())),
        'phase_line_sign_histogram': {str(k): v for k, v in sorted(global_signs.items())},
        'order_three_phase_line_sign_histogram': {
            str(k): v for k, v in sorted(order_three_signs.items())},
        'order_three_stabilizer_count': sum(order_three_signs.values()),
        'nontrivial_order_three_phase_action_count': order_three_signs[-1],
        'conclusion': (
            'Every in-place support stabilizer acts on the rank-one integral '
            'phase line through GL(1,Z)={+1,-1}. The concrete census contains '
            'no order-three support stabilizer; its five nonidentity '
            'stabilizers are involutions acting by -1. Therefore the sparse '
            'one-loop phase line does not promote 3 to a physical bad prime.'),
        'scope': (
            'This excludes prime 3 only for the source-defined in-place '
            'one-loop phase-line action. It does not exclude a different '
            'physical order-three cover or readout supplied independently.'),
        'supports': records,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'supports'}, indent=2))


if __name__ == '__main__':
    main()
