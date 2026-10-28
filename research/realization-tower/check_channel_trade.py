"""Exact finite incidence audit of the proposed input/output trade.

No physical claims and no assumed identification of existing rung APIs.
Run: python research/realization-tower/check_channel_trade.py
"""
from itertools import combinations
from pathlib import Path
import json


def simplex(vertices):
    vertices = tuple(vertices)
    return {frozenset(c) for k in range(len(vertices) + 1)
            for c in combinations(vertices, k)}


def cone(k, apex):
    assert all(apex not in f for f in k)
    return k | {f | {apex} for f in k}


def link(k, face):
    assert face in k
    return {f for f in k if not (f & face) and f | face in k}


def arrows(k):
    return {(u, v) for f in k if len(f) == 2
            for u in f for v in f if u != v}


def main():
    base = simplex(range(4))
    a = arrows(base)
    assert len(a) == 12
    local = []
    for v in range(4):
        incoming = {e for e in a if e[1] == v}
        outgoing = {e for e in a if e[0] == v}
        lk = link(base, frozenset({v}))
        assert len(incoming) == len(outgoing) == 3
        assert cone(lk, v) == base
        assert len(arrows(lk)) == 6
        # Outgoing channels correspond to link vertices, not its directed edges.
        assert {w for _, w in outgoing} == {next(iter(f)) for f in lk if len(f) == 1}
        local.append({'vertex': v, 'incoming': 3, 'outgoing': 3,
                      'link_vertices': 3, 'link_directed_edges': 6})

    coned = cone(base, 4)
    assert coned == simplex(range(5))
    assert len(arrows(coned)) == 20
    assert len(arrows(coned) - a) == 8
    assert a <= arrows(coned)
    assert link(coned, frozenset({4})) == base
    assert all(sum(u == v for u, _ in arrows(coned)) == 4 for v in range(5))

    cone_rows = []
    for n in range(1, 13):
        k = simplex(range(n))
        next_k = cone(k, n)
        old, new = arrows(k), arrows(next_k)
        assert len(old) == n * (n - 1)
        assert len(new) - len(old) == 2 * n
        assert len(next_k) == 2 * len(k)
        cone_rows.append({'old_vertices': n, 'old_directed_edges': len(old),
                          'new_directed_edges': len(new),
                          'new_nonempty_faces': len(next_k) - 1})

    # Four plane normals and twelve nearest-neighbour FCC directions.
    # Dot products need no square roots to classify sides of the parallel plane
    # through the selected point.
    normals = [(1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)]
    directions = set()
    for zero in range(3):
        axes = [j for j in range(3) if j != zero]
        for x in (-1, 1):
            for y in (-1, 1):
                d = [0, 0, 0]
                d[axes[0]], d[axes[1]] = x, y
                directions.add(tuple(d))
    assert len(directions) == 12
    plane_rows = []
    for n in normals:
        dots = [sum(x * y for x, y in zip(n, d)) for d in directions]
        counts = [sum(x < 0 for x in dots), dots.count(0), sum(x > 0 for x in dots)]
        assert counts == [3, 6, 3]
        plane_rows.append({'normal': n, 'negative': 3, 'tangent': 6, 'positive': 3})

    # A 15-token partition DOES realize the proposed arithmetic, but is an
    # additional role-transfer rule. Exhaust all initial three-token selections
    # and all first transfers: 455 * 12 = 5460 cases.
    tokens = frozenset(range(15))
    transfers = 0
    for selected in combinations(tokens, 3):
        inputs = frozenset(selected)
        outputs = tokens - inputs
        for e in outputs:
            next_inputs, next_outputs = inputs | {e}, outputs - {e}
            assert len(next_inputs) == 4 and len(next_outputs) == 11
            assert not next_inputs & next_outputs
            assert next_inputs | next_outputs == tokens
            transfers += 1
    assert transfers == 5460
    schedule = [{'rung': r, 'inputs': 15-r, 'outputs': r} for r in range(12, 3, -1)]
    assert all(row['inputs'] + row['outputs'] == 15 for row in schedule)
    # A tetrahedron happens to have 15 nonempty faces, but these are mixed
    # dimensional cells, NOT 15 arrows or a canonical three-input partition.
    f_vector = [sum(len(f) == k for f in base) for k in range(1, 5)]
    assert f_vector == [4, 6, 4, 1] and sum(f_vector) == 15

    result = {
        'status': 'pass',
        'meaning': 'Audit assertions pass; plain-coning identification fails at the declared incidence scope.',
        'tetrahedron': {'directed_edges': 12, 'local_interfaces': local, 'f_vector': f_vector},
        'first_cone': {'directed_edges_before': 12, 'directed_edges_after': 20,
                       'local_incoming_after': 4, 'local_outgoing_after': 4},
        'cone_checks': cone_rows,
        'plane_split_for_standard_FCC_neighbours': plane_rows,
        'additional_role_partition': {'first_step_cases': transfers, 'schedule': schedule},
        'surviving_result': 'The arithmetic trade is a valid retained partition update on 15 supplied tokens, not a consequence of ordinary coning. Coning/linking recovers a marked simplex and relates its outgoing apex channels to link vertices.',
        'not_tested': 'A new decorated cone with a specified causal/routing law, or identification with actual WG/rung transport APIs.'
    }
    target = Path(__file__).with_name('results') / 'channel-trade-v1.json'
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'first_step_cases': transfers,
                      'plain_coning_trade': 'not_realized', 'receipt': str(target)}))


if __name__ == '__main__':
    main()
