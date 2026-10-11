"""H2: exact simplicial cones, center links, homology and subdivision tests.

Uses the same frozen targets as H4. Rational homology is computed, not inferred
from Euler characteristic. Coning is one common operation in every dimension.
The input is still the target link, not a newly derived minimal arrow seed.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json

from check_common_assembly_symmetry import load_targets, affine_coordinates, determinant, BASE


def closure(maximal):
    return {tuple(c) for simplex in maximal for size in range(1, len(simplex)+1)
            for c in combinations(sorted(simplex), size)}


def ranks(matrix):
    a = [list(map(Q, row)) for row in matrix]
    if not a:
        return 0
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        v = a[row][col]
        a[row] = [x/v for x in a[row]]
        for i in range(row+1, len(a)):
            v = a[i][col]
            if v:
                a[i] = [x-v*y for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def invariants(complex_cells):
    if not complex_cells:
        return {'f_vector': [], 'rational_betti': [], 'euler_characteristic': 0}
    dimension = max(map(len, complex_cells))-1
    levels = [sorted(s for s in complex_cells if len(s) == d+1) for d in range(dimension+1)]
    boundary_ranks = [0]
    for d in range(1, dimension+1):
        index = {s: i for i, s in enumerate(levels[d-1])}
        matrix = [[0]*len(levels[d]) for _ in levels[d-1]]
        for j, s in enumerate(levels[d]):
            for i in range(len(s)):
                matrix[index[s[:i]+s[i+1:]]][j] = (-1)**i
        boundary_ranks.append(ranks(matrix))
    boundary_ranks.append(0)
    betti = [len(levels[d])-boundary_ranks[d]-boundary_ranks[d+1] for d in range(dimension+1)]
    f_vector = list(map(len, levels))
    euler = sum((-1)**i*n for i, n in enumerate(f_vector))
    assert euler == sum((-1)**i*n for i, n in enumerate(betti))
    return {'f_vector': f_vector, 'rational_betti': betti,
            'boundary_ranks': boundary_ranks[1:-1], 'euler_characteristic': euler}


def boundary_facets(maximal):
    count = Counter(tuple(f) for s in maximal for f in combinations(sorted(s), len(s)-1))
    assert max(count.values(), default=0) <= 2, 'Not a pseudomanifold at a codimension-one face'
    return {s for s, n in count.items() if n == 1}


def link(complex_cells, vertex):
    return {tuple(v for v in s if v != vertex) for s in complex_cells if vertex in s and len(s) > 1}


def cone(maximal, apex):
    return {tuple(sorted((*s, apex))) for s in maximal}


def run_target(distances, cells):
    vertices = sorted({v for c in cells for v in c})
    ids = {v: i for i, v in enumerate(vertices)}
    maximal = {tuple(sorted(ids[v] for v in c)) for c in cells}
    K = closure(maximal)
    apex = len(vertices)
    cone_maximal = cone(maximal, apex)
    CK = closure(cone_maximal)
    assert link(CK, apex) == K
    # Construct an actual elementary-collapse sequence to the apex. This is
    # stronger than merely observing vanishing reduced homology.
    remaining = set(CK)
    collapse_pairs = []
    for s in sorted(K, key=lambda s: (-len(s), s)):
        joined = tuple(sorted((*s, apex)))
        cofaces = {t for t in remaining if len(t) > len(s) and set(s) <= set(t)}
        assert cofaces == {joined}
        remaining.remove(s)
        remaining.remove(joined)
        collapse_pairs.append([list(s), list(joined)])
    assert remaining == {(apex,)}
    base_betti = invariants(K)['rational_betti']
    local_homology = [0] + [b - (i == 0) for i, b in enumerate(base_betti)]
    boundary = boundary_facets(maximal)
    cone_boundary = boundary_facets(cone_maximal)
    # Boundary of a cone is the base plus the cones on its exposed boundary.
    assert cone_boundary == maximal | cone(boundary, apex)
    # Empty boundary remains empty under this definition of cone on facets.
    assert invariants(CK)['rational_betti'] == [1]+[0]*max(map(len, maximal))
    # Collapse only the explicitly barycentric subdivision, not arbitrary seams.
    parent_of = {c: tuple(i for i in range(len(distances)) if any(v[i] for v in c)) for c in cells}
    coarse = set(parent_of.values())
    coarseK = closure(coarse)
    assert invariants(coarseK)['rational_betti'] == invariants(K)['rational_betti']
    _, coordinates = affine_coordinates(distances)
    d = len(coordinates[0])
    center = tuple(sum(v[k] for v in coordinates)/len(coordinates) for k in range(d))
    def realized(v):
        return tuple(sum(w*coordinates[i][k] for i, w in enumerate(v)) for k in range(d))
    def cone_determinant(points):
        assert len(points) == d
        return abs(determinant([[p[k]-center[k] for p in points] for k in range(d)]))
    volume_checks = []
    for parent in sorted(coarse):
        coarse_volume = cone_determinant([coordinates[i] for i in parent])
        children = [c for c, p in parent_of.items() if p == parent]
        volumes = [cone_determinant([realized(v) for v in c]) for c in children]
        assert all(v > 0 for v in volumes)
        assert sum(volumes) == coarse_volume
        volume_checks.append({'parent': list(parent), 'children': len(children),
                              'positive_cone_determinant': str(coarse_volume)})
    vertex_link_types = Counter(tuple(invariants(link(K, v))['rational_betti']) for v in ids.values())
    if max(map(len, maximal)) == 3:
        for v in ids.values():
            lk = link(K, v)
            degrees = Counter(x for e in lk if len(e) == 2 for x in e)
            assert set(degrees.values()) <= {1, 2}
            assert sum(n == 1 for n in degrees.values()) in (0, 2)
            assert invariants(lk)['rational_betti'][0] == 1
    return {'base': invariants(K), 'base_boundary': invariants(closure(boundary)),
            'cone': invariants(CK), 'cone_boundary': invariants(closure(cone_boundary)),
            'center_link_exactly_base': True, 'boundary_formula_exact': True,
            'center_local_rational_homology': local_homology,
            'elementary_collapse_to_apex': collapse_pairs,
            'coarse_base': invariants(coarseK), 'coarse_cone_cells': len(coarse),
            'fine_cone_cells': len(cone_maximal),
            'positive_subdivision_volume_checks': volume_checks,
            'base_vertex_link_betti_types': {str(k): v for k, v in vertex_link_types.items()}}, coarse


def main():
    targets, evidence = load_targets()
    results, coarse_cells = {}, {}
    for name, (distances, cells, marks) in targets.items():
        results[name], coarse_cells[name] = run_target(distances, cells)
    assert results['proton']['base']['rational_betti'] == [1, 0, 1]
    assert results['neutron_belt']['base']['rational_betti'] == [1, 1, 0]
    assert results['neutron_belt']['base_boundary']['rational_betti'] == [2, 2]
    assert results['electron_pentachoron']['base']['rational_betti'] == [1, 0, 0, 1]
    assert results['proton']['center_local_rational_homology'] == [0, 0, 0, 1]
    assert results['neutron_belt']['center_local_rational_homology'] == [0, 0, 1, 0]
    assert results['electron_pentachoron']['center_local_rational_homology'] == [0, 0, 0, 0, 1]
    # Bind the recovered coarse cone cells to the existing six-piece belt store.
    source = json.loads((BASE/'results/four_six_center_cones.json').read_text())
    labels = [k for k in source['belt_scaled_coordinates'] if k != 'O']
    actual_belt = {frozenset(['O']+[labels[i] for i in c]) for c in coarse_cells['neutron_belt']}
    assert actual_belt == {frozenset(c) for c in source['belt_tetrahedra']}
    # Counterfactual: fill both attachment rims. This changes the link, not just
    # its triangulation, and adds exactly the two explicitly missing cone cells.
    caps = {tuple(sorted(labels.index(k) for k in t if k != 'O'))
            for t in source['missing_cap_tetrahedra']}
    capped = coarse_cells['neutron_belt'] | caps
    cap_invariants = invariants(closure(capped))
    assert cap_invariants['rational_betti'] == [1, 0, 1]
    assert not boundary_facets(capped)
    proton_coarse = {frozenset(['O']+['ABCD'[i] for i in c]) for c in coarse_cells['proton']}
    assert proton_coarse == {frozenset(c) for c in source['proton_tetrahedra']}
    report = {'hypothesis': 2, 'status': 'tested', 'results': results,
              'stored_proton_and_belt_coarse_cone_cells_match': True,
              'capped_belt_control': cap_invariants,
              'sources': evidence,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'target_loader_sha256': hashlib.sha256((BASE/'checkers/check_common_assembly_symmetry.py').read_bytes()).hexdigest(),
              'conclusion': 'One cone operation reconstructs the stored proton and belt constituents up to checked positive subdivision, and a stellar subdivision of the electron 4-simplex. The belt apex has annular link, not the link of a manifold point. Capping the rims changes that link to a sphere.',
              'scope': 'Target-link reconstruction, not a derivation of links from minimal arrows. No coefficient counts inferred.'}
    dest = BASE/'results/common_assembly_cones.json'
    dest.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
