#!/usr/bin/env python3
"""Exact finite convex-polygon dissections and face-product verification."""
from itertools import combinations, product
import json
from pathlib import Path

def diagonals(n):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n)
                 if j != i + 1 and (i, j) != (0, n - 1))

def crosses(a, b):
    i, j = a; k, l = b
    return (i < k < j < l) or (k < i < l < j)

def dissections_on(diags):
    out = []
    for r in range(len(diags) + 1):
        for ds in combinations(diags, r):
            if all(not crosses(a, b) for a, b in combinations(ds, 2)):
                out.append(frozenset(ds))
    return tuple(out)

def split_regions(n, dissection):
    regions = [tuple(range(n))]
    for a, b in sorted(dissection):
        found = None
        for q, region in enumerate(regions):
            if a in region and b in region:
                ia, ib = region.index(a), region.index(b)
                if ia > ib: ia, ib = ib, ia
                if ib != ia + 1 and not (ia == 0 and ib == len(region) - 1):
                    found = (q, ia, ib, region); break
        assert found is not None, (n, dissection, (a, b), regions)
        q, ia, ib, region = found
        first = region[ia:ib + 1]
        second = region[ib:] + region[:ia + 1]
        regions[q:q + 1] = [first, second]
    return tuple(regions)

def region_diagonals(region):
    edges = {frozenset((region[i], region[(i + 1) % len(region)]))
             for i in range(len(region))}
    return tuple((a, b) for a, b in combinations(sorted(region), 2)
                 if frozenset((a, b)) not in edges)

def verify(n):
    all_dis = dissections_on(diagonals(n))
    face_checks = tuple_checks = unique_region_checks = 0
    for base in all_dis:
        regions = split_regions(n, base)
        local_factors = [dissections_on(region_diagonals(r)) for r in regions]
        face = {d for d in all_dis if base <= d}
        encoded = set()
        for refined in face:
            extra = refined - base
            pieces = []
            for d in extra:
                carriers = [q for q, r in enumerate(regions)
                            if d[0] in r and d[1] in r and d in region_diagonals(r)]
                assert len(carriers) == 1
                unique_region_checks += 1
            for r in regions:
                allowed = set(region_diagonals(r))
                pieces.append(frozenset(d for d in extra if d in allowed))
            encoded.add(tuple(pieces)); face_checks += 1
        tuples = set(product(*local_factors))
        assert encoded == tuples
        for pieces in tuples:
            union = base | frozenset(d for piece in pieces for d in piece)
            assert union in face
            tuple_checks += 1
    return {
        'n': n,
        'diagonals': len(diagonals(n)),
        'dissections': len(all_dis),
        'face_elements_checked': face_checks,
        'factor_tuples_checked': tuple_checks,
        'unique_region_assignments_checked': unique_region_checks,
        'status': 'passed'
    }

if __name__ == '__main__':
    result = {
        'schema': 'marici.polygon-face-product-check.v1',
        'claim': 'For each tested convex n-gon dissection D, refinements above D are bijective with the product of dissection sets of its regions.',
        'strength': 'exhaustive finite instances; algorithm generic in n; not an unbounded theorem',
        'tests': [verify(n) for n in range(3, 8)]
    }
    out = Path('research/nima/results/generic_polygon_face_product.json')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, sort_keys=True))
