"""H6: distinguish geometric refinement from higher-dimensional witnesses.

Checks face-centroid subdivisions, both parent maps of the historical six-cell
bipyramid refinement, the actual belt's center link, geometric diagonal flips,
and the two-versus-three split of the electron 4-simplex boundary.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json

from check_common_assembly_symmetry import BASE, load_targets, affine_coordinates, determinant, inverse, vertex, cell
from check_common_assembly_gluing import orient, permutation_sign
from check_common_assembly_cones import closure, invariants, link, cone


def boundary_chain(oriented_cells):
    out = Counter()
    for c in oriented_cells:
        for i in range(len(c)):
            face = c[:i]+c[i+1:]
            out[tuple(sorted(face))] += (-1)**i * permutation_sign(face)
    return {f: n for f, n in out.items() if n}


def face_subdivision_test(distances, target_cells):
    n = len(distances)
    parents = {tuple(i for i in range(n) if any(v[i] for v in c)) for c in target_cells}
    assert all(len(p) == 3 for p in parents)
    coarse_cells = {cell(vertex(n, i) for i in p) for p in parents}
    oriented_parents = orient(distances, coarse_cells)
    generated = []
    for a, b, c in oriented_parents:
        centre = tuple((x+y+z)/3 for x, y, z in zip(a, b, c))
        children = [(centre, a, b), (centre, b, c), (centre, c, a)]
        assert boundary_chain(children) == boundary_chain([(a, b, c)])
        # The centroid is internal with strictly positive barycentric weights.
        assert all(centre[i] == Q(1, 3) for i in range(n) if a[i] or b[i] or c[i])
        generated.extend(children)
    assert {cell(c) for c in generated} == set(target_cells)
    assert boundary_chain(generated) == boundary_chain(oriented_parents)
    return {'coarse_faces': len(parents), 'generated_faces': len(generated),
            'exact_target_cells': True, 'facewise_and_global_boundary_preserved': True,
            'finding': 'The same centroid subdivision reproduces the target triangulation, provided the coarse surface is already supplied.'}


def subtract(a, b):
    return tuple(x-y for x, y in zip(a, b))


def tetra_det(points, tetra):
    a, b, c, d = [points[k] for k in tetra]
    return determinant([subtract(b, a), subtract(c, a), subtract(d, a)])


def positive_tetra(points, tetra):
    tetra = tuple(tetra)
    if tetra_det(points, tetra) < 0:
        tetra = (tetra[1], tetra[0], *tetra[2:])
    assert tetra_det(points, tetra) > 0
    return tetra


def barycentric_in_tetra(points, tetra, point):
    a, b, c, d = [points[k] for k in tetra]
    matrix = [[b[i]-a[i], c[i]-a[i], d[i]-a[i]] for i in range(3)]
    inv = inverse(matrix)
    v = subtract(point, a)
    weights = [sum(row[i]*v[i] for i in range(3)) for row in inv]
    return [1-sum(weights)]+weights


def bipyramid_test():
    path = BASE/'results/three_tetrahedron_belt.json'
    source = json.loads(path.read_text())
    assert source['verification_passed']
    points = {k: tuple(map(Q, v)) for k, v in source['coordinates'].items()}
    pair = [positive_tetra(points, t) for t in source['pair_tetrahedra']]
    triple = [positive_tetra(points, t) for t in source['belt_tetrahedra']]
    records = source['common_refinement']
    fine = [positive_tetra(points, r['tetrahedron']) for r in records]
    assert boundary_chain(pair) == boundary_chain(triple) == boundary_chain(fine)
    parent_reports = []
    for key, parents in [('pair_parent', pair), ('belt_parent', triple)]:
        for parent in parents:
            children = [t for t, r in zip(fine, records) if set(r[key]) == set(parent)]
            assert children
            for child in children:
                for k in child:
                    weights = barycentric_in_tetra(points, parent, points[k])
                    assert sum(weights) == 1 and min(weights) >= 0
            parent_volume = tetra_det(points, parent)/6
            assert sum(tetra_det(points, c)/6 for c in children) == parent_volume
            parent_reports.append({'map': key, 'parent': list(parent), 'children': len(children),
                                   'exact_containment_and_volume': True})
    fine_complex = closure(fine)
    center_link = invariants(link(fine_complex, 'F'))
    assert center_link['rational_betti'] == [1, 0, 1]
    actual = json.loads((BASE/'results/four_six_center_cones.json').read_text())
    actual_complex = closure([tuple(t) for t in actual['belt_tetrahedra']])
    actual_link = invariants(link(actual_complex, 'O'))
    assert actual_link['rational_betti'] == [1, 1, 0]
    assert center_link['rational_betti'] != actual_link['rational_betti']
    return {'refinement_cells': len(fine), 'parent_maps': parent_reports,
            'same_exact_outer_boundary': True, 'total_volume': str(sum(tetra_det(points, t)/6 for t in fine)),
            'bipyramid_refinement_center_link': center_link,
            'stored_neutron_center_link': actual_link,
            'center_preserving_refinement_identification_possible': False,
            'finding': 'Both six-cell constructions are contractible, but their marked center links differ. The bipyramid refinement is not the stored neutron belt.'}, path


def belt_flip_test():
    source = json.loads((BASE/'results/four_six_center_cones.json').read_text())
    points = {k: tuple(map(Q, v)) for k, v in source['belt_scaled_coordinates'].items() if k != 'O'}
    faces = [tuple(f) for f in source['belt_faces']]
    tests = []
    for a, b in combinations(faces, 2):
        seam = set(a) & set(b)
        if len(seam) != 2:
            continue
        vertices = tuple(sorted(set(a) | set(b)))
        value = tetra_det(points, vertices)
        assert value != 0
        tips = tuple(sorted((set(a) | set(b))-seam))
        alternative = [tuple((*tips, s)) for s in sorted(seam)]
        original_edges = Counter(tuple(sorted(e)) for f in (a, b) for e in combinations(f, 2))
        new_edges = Counter(tuple(sorted(e)) for f in alternative for e in combinations(f, 2))
        assert {e for e, count in original_edges.items() if count == 1} == {
            e for e, count in new_edges.items() if count == 1}
        tests.append({'shared_edge': sorted(seam), 'alternative_diagonal': list(tips),
                      'nonzero_scaled_tetrahedron_determinant': str(value),
                      'same_patch_boundary_edges': True, 'same_geometric_surface': False})
    assert len(tests) == 6
    return {'internal_edge_flips': tests,
            'finding': 'Every coarse internal seam joins noncoplanar triangles. Flipping its diagonal preserves the patch boundary but changes spatial support, so it is not an ordinary geometric refinement. A swept tetrahedral cell would be extra witness data.'}


def electron_witness_test(distances, cells):
    oriented = orient(distances, cells)
    left, right = oriented[:2], oriented[2:]
    lb, rb = boundary_chain(left), boundary_chain(right)
    assert lb == {f: -v for f, v in rb.items()}
    assert len(lb) == 6 and not boundary_chain(oriented)
    # A relative-interior point of each left facet cannot lie in any right
    # facet: simplex barycentric coordinates are unique in affine dimension 4.
    n = len(distances)
    separating_points = []
    for facet in left:
        center = tuple(sum(v[i] for v in facet)/len(facet) for i in range(n))
        for other in right:
            missing = [i for i in range(n) if all(v[i] == 0 for v in other)]
            assert len(missing) == 1 and center[missing[0]] > 0
        separating_points.append(list(map(str, center)))
    _, coordinates = affine_coordinates(distances)
    assert len(coordinates[0]) == 4
    G = [[(distances[0][i]+distances[0][j]-distances[i][j])/2 for j in range(1, n)] for i in range(1, n)]
    assert determinant(G) == 1280
    simplex = tuple(vertex(n, i) for i in range(n))
    full_boundary = boundary_chain([simplex])
    oriented_signs = {tuple(sorted(c)): permutation_sign(c) for c in oriented}
    assert oriented_signs == full_boundary or oriented_signs == {f: -v for f, v in full_boundary.items()}
    base = [tuple(vertex(n, i) for i in range(4))]
    base_topology, full_topology = invariants(closure(base)), invariants(closure(cells))
    assert base_topology['rational_betti'] == [1, 0, 0, 0]
    assert full_topology['rational_betti'] == [1, 0, 0, 1]
    return {'boundary_partition': [len(left), len(right)], 'shared_boundary_triangles': len(lb),
            'opposite_boundary_chains_exact': True, 'left_interior_points_not_on_right': separating_points,
            'geometric_common_refinement_of_two_sides_possible': False,
            'four_simplex_gram_determinant': '1280', 'full_boundary_is_exact_simplex_boundary': True,
            'attachment_tetrahedron_topology': base_topology, 'pentachoron_boundary_topology': full_topology,
            'finding': 'The two and three tetrahedral boundary routes share a boundary but have different supports in 4D. The pentachoron supplies a higher filling witness, not a common subdivision of those routes or of the attachment tetrahedron.'}


def main():
    targets, evidence = load_targets()
    subdivisions = {name: face_subdivision_test(targets[name][0], targets[name][1])
                    for name in ('proton', 'neutron_belt')}
    bipyramid, path = bipyramid_test()
    evidence[str(path.relative_to(BASE.parent))] = hashlib.sha256(path.read_bytes()).hexdigest()
    report = {'hypothesis': 6, 'status': 'tested', 'shared_centroid_subdivision': subdivisions,
              'historical_two_three_common_refinement': bipyramid,
              'actual_belt_diagonal_flips': belt_flip_test(),
              'electron_higher_witness': electron_witness_test(targets['electron_pentachoron'][0], targets['electron_pentachoron'][1]),
              'sources': evidence,
              'implementation_sha256': {name: hashlib.sha256((BASE/'checkers'/name).read_bytes()).hexdigest()
                  for name in ('check_common_assembly_refinement.py', 'check_common_assembly_symmetry.py', 'check_common_assembly_cones.py', 'check_common_assembly_gluing.py')},
              'conclusion': 'Ordinary refinement reproduces supplied proton/belt triangulations but cannot be the whole common assembly law. The historical six-cell bipyramid has the wrong center link for the neutron. The electron two/three boundary relation is filled by a 4-simplex, not by a common geometric subdivision. Higher witnesses remain a distinct candidate operation.',
              'scope': 'Exact bounded refinement and obstruction tests; no derivation of elementary cell inventories or coefficient transport.'}
    (BASE/'results/common_assembly_refinement.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
