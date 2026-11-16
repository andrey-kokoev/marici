"""Exact finite checks of simultaneous extension witnesses.

Python 3.10+; standard library only.
No path histories are identified. An independent set S is a compatibility
readout of an extension: a separate provenance record may retain every
construction history producing that readout.

Outputs: ramsey_joint_witness_results.json next to this script.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import math


def circulant(n: int, steps: tuple[int, ...]) -> tuple[int, ...]:
    if n < 1:
        raise ValueError('n must be positive')
    adjacency = [0] * n
    for v in range(n):
        for d in steps:
            w = (v + d) % n
            if w == v:
                raise ValueError('a step may not create a loop')
            adjacency[v] |= 1 << w
            adjacency[w] |= 1 << v
    return tuple(adjacency)


def vertices(mask: int) -> list[int]:
    return [i for i in range(mask.bit_length()) if mask & (1 << i)]


def mask_of(items: list[int]) -> int:
    return sum(1 << i for i in items)


def independent(mask: int, adj: tuple[int, ...]) -> bool:
    rest = mask
    while rest:
        bit = rest & -rest
        v = bit.bit_length() - 1
        rest ^= bit
        if adj[v] & rest:
            return False
    return True


def independent_sets(adj: tuple[int, ...]) -> list[int]:
    return [s for s in range(1 << len(adj)) if independent(s, adj)]


def analyse(name: str, adj: tuple[int, ...], k: int,
            max_core_search: int = 5) -> dict:
    n = len(adj)
    inds = independent_sets(adj)
    alpha = max(s.bit_count() for s in inds)
    assert alpha < k
    assert all(independent(adj[v], adj) for v in range(n)), 'triangle found'
    obligations = [s for s in inds if s.bit_count() == k - 1]
    solution_masks = [sum(1 << j for j, s in enumerate(inds) if s & t)
                      for t in obligations]
    all_candidates = (1 << len(inds)) - 1
    viable = all_candidates
    for solution_mask in solution_masks:
        viable &= solution_mask
    cores = None
    examined = {}
    for size in range(1, min(max_core_search, len(obligations)) + 1):
        core_count = 0
        first = None
        for chosen in combinations(range(len(obligations)), size):
            common = all_candidates
            for j in chosen:
                common &= solution_masks[j]
            if common == 0:
                core_count += 1
                if first is None:
                    first = chosen
        examined[str(size)] = {
            'families_checked': math.comb(len(obligations), size),
            'inconsistent_families': core_count,
        }
        if first is not None:
            cores = {
                'minimum_size': size,
                'count_at_minimum_size': core_count,
                'first_example': [vertices(obligations[j]) for j in first],
            }
            break
    coverage = [sum(bool(s & t) for t in obligations) for s in inds]
    return {
        'name': name,
        'vertices': n,
        'edges': sum(x.bit_count() for x in adj) // 2,
        'triangle_free': True,
        'independence_number': alpha,
        'independent_sets_by_size': dict(sorted(Counter(s.bit_count() for s in inds).items())),
        'obligations': len(obligations),
        'valid_one_vertex_extensions': viable.bit_count(),
        'minimum_unmet_obligations_after_triangle_safe_choice': len(obligations) - max(coverage),
        'core_enumeration': examined,
        'smallest_obstruction': cores,
    }


def five_obligation_certificate(adj: tuple[int, ...]) -> dict:
    # H = C_13(1,5), with N(0) = {1,5,8,12}.
    keys = [0, 1, 5, 8, 12]
    obligations = [adj[v] for v in keys]
    # Each row is a common witness for all obligations except the named one.
    omitted_witnesses = {
        0: [0],
        1: [1, 4, 7],
        5: [5, 7, 9],
        8: [4, 6, 8],
        12: [6, 9, 12],
    }
    inds = independent_sets(adj)
    assert all(t.bit_count() == 4 and independent(t, adj) for t in obligations)
    assert not any(all(s & t for t in obligations) for s in inds)
    for omitted, points in omitted_witnesses.items():
        s = mask_of(points)
        assert independent(s, adj)
        assert not (s & adj[omitted])
        assert all(s & adj[v] for v in keys if v != omitted)
    fvector = []
    for size in range(1, 6):
        count = 0
        for selected in combinations(obligations, size):
            count += any(all(s & t for t in selected) for s in inds)
        fvector.append(count)
    assert fvector == [5, 10, 10, 5, 0]
    # The fourfold permutation h(v)=5v preserves the whole graph.
    for v in range(13):
        image = mask_of(sorted((5 * w) % 13 for w in vertices(adj[v])))
        assert image == adj[(5 * v) % 13]
    return {
        'requirement_indices': keys,
        'requirements': {str(v): vertices(adj[v]) for v in keys},
        'witness_after_omitting_requirement': omitted_witnesses,
        'simplex_counts_by_number_of_vertices_1_through_5': fvector,
        'joint_witness_count': 0,
        'fourfold_symmetry_v_maps_to_5v_verified': True,
        'analytic_obstruction': (
            'Any independent S meeting N(0) contains a in N(0). '
            'Independence then forces S disjoint from N(a), '
            'but N(a) is another required set.'
        ),
        'scope': (
            'The induced compatibility complex on these five requirements '
            'is the boundary of a 4-simplex. No assertion about nonzero '
            'homology of the entire compatibility complex is made.'
        ),
    }


def main() -> None:
    c5 = circulant(5, (1,))
    w8 = circulant(8, (1, 4))
    h13 = circulant(13, (1, 5))
    k33 = tuple(sum(1 << j for j in range(6) if (i < 3) != (j < 3))
                for i in range(6))
    results = {
        'meaning': ('S is an independent set of first-relation neighbors of a new vertex. '
                    'For each old independent (k-1)-set T, the requirement is S intersects T. '
                    'The resulting predicate is exactly the standard one-vertex Ramsey extension test.'),
        'cases': [analyse('C5, k=3', c5, 3),
                  analyse('W8, k=4', w8, 4),
                  analyse('C13(1,5), k=5', h13, 5),
                  analyse('K3,3 early dead end, k=4', k33, 4)],
        'five_requirement_certificate': five_obligation_certificate(h13),
        'claims_not_made': [
            'No new Ramsey value is claimed.',
            'This does not derive the Ramsey conditions from rotation and inversion alone.',
            'A nonextendable graph need not have maximum possible order.',
            'Three or four operation generators need not imply an obstruction arity of three or four.',
            'The finite code checks are not a proof-assistant formalization.',
        ],
    }
    out = Path(__file__).with_name('ramsey_joint_witness_results.json')
    out.write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
