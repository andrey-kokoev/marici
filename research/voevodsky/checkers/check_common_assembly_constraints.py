"""H5: source-edge distance constraints versus completed target metrics.

One exact Euclidean-distance/Gram test is used for all candidates. Explicit
counterexamples distinguish constraints carried by seed arrows, prescribed
coordinates, and extra global convexity/parallel-rim conditions. No optimizer
is allowed to silently insert the target distances into missing edges.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json

from check_common_assembly_symmetry import BASE, RESEARCH, determinant, metric, load_targets
from check_common_assembly_cones import ranks


def gram(distances):
    n = len(distances)
    assert all(distances[i][i] == 0 for i in range(n))
    assert all(distances[i][j] == distances[j][i] for i in range(n) for j in range(n))
    return [[(distances[0][i]+distances[0][j]-distances[i][j])/2
             for j in range(1, n)] for i in range(1, n)]


def inspect_metric(distances):
    G = gram(distances)
    # A symmetric rational matrix is PSD iff all principal minors are >= 0.
    minors = [determinant([[G[i][j] for j in selected] for i in selected])
              for size in range(1, len(G)+1) for selected in combinations(range(len(G)), size)]
    psd = all(x >= 0 for x in minors)
    return {'euclidean': psd, 'affine_dimension': ranks(G) if psd else None,
            'gram_determinant': str(determinant(G)),
            'distinct_vertices': all(distances[i][j] > 0 for i, j in combinations(range(len(distances)), 2))}


def same_constraints(a, b, edges):
    return all(a[i][j] == b[i][j] for i, j in edges)


def rigidity_rank(points, edges, weights):
    rows = []
    for i, j in sorted(edges):
        row = [Q(0)]*(3*len(points))
        for k, w in enumerate(weights):
            row[3*i+k] = w*(points[i][k]-points[j][k])
            row[3*j+k] = -row[3*i+k]
        rows.append(row)
    return ranks(rows)


def subtract(a, b):
    return tuple(x-y for x, y in zip(a, b))


def supporting_faces(points, faces, preserve_outward_orientation=False):
    out = []
    for face in faces:
        a, b, c = [points[i] for i in face]
        signs = [determinant([subtract(b, a), subtract(c, a), subtract(p, a)]) for p in points]
        if all(s <= 0 for s in signs) or (not preserve_outward_orientation and all(s >= 0 for s in signs)):
            out.append(list(face))
    return out


def proton_test(target):
    source = json.loads((RESEARCH/'nima/inputs/proton-six-arrows.json').read_text())
    labels = list(source['vertices'])
    edges = {tuple(sorted((labels.index(a), labels.index(b)))) for a, b in source['arrows'] if a != b}
    assert len(edges) == 5
    missing = set(combinations(range(4), 2))-edges
    assert missing == {(labels.index('C'), labels.index('D'))}
    assert all(target[i][j] == 8 for i, j in edges)
    samples = []
    for t in map(Q, (4, 8, 12, 24, 25)):
        candidate = [row[:] for row in target]
        i, j = next(iter(missing))
        candidate[i][j] = candidate[j][i] = t
        assert same_constraints(candidate, target, edges)
        result = inspect_metric(candidate)
        assert Q(result['gram_determinant']) == 2*t*(24-t)
        assert result['euclidean'] == (t <= 24)
        if t <= 24:
            assert result['affine_dimension'] == (2 if t == 24 else 3)
            assert result['distinct_vertices']
        samples.append({'CD_squared': str(t), **result})
    assert inspect_metric(target)['affine_dimension'] == 3
    # Positive control: impose the original cycle-permutations as isometries.
    # This is an additional rule, but it can derive CD rather than read it.
    directed = {tuple(e) for e in source['arrows']}
    cycle_permutations = []
    for a, b, c in permutations(labels, 3):
        if {(a, b), (b, c), (c, a)} <= directed:
            rename = {a: b, b: c, c: a}
            cycle_permutations.append(tuple(labels.index(rename.get(k, k)) for k in labels))
    propagated = {e: Q(8) for e in edges}
    while True:
        previous = dict(propagated)
        for permutation in cycle_permutations:
            for (i, j), distance in previous.items():
                e = tuple(sorted((permutation[i], permutation[j])))
                assert e not in propagated or propagated[e] == distance
                propagated[e] = distance
        if previous == propagated:
            break
    assert set(propagated) == set(combinations(range(4), 2))
    assert propagated[next(iter(missing))] == 8
    completed = [[Q(0) if i == j else propagated[tuple(sorted((i, j)))] for j in range(4)] for i in range(4)]
    assert completed == target and inspect_metric(completed)['affine_dimension'] == 3
    return {'directed_seed_arrows': len(source['arrows']), 'undirected_length_constraints': len(edges),
            'unspecified_distance': 'CD', 'target_CD_squared': '8',
            'gram_determinant_formula': '2*t*(24-t), t=CD_squared',
            'samples': samples,
            'cycle_isometry_control': {'all_six_distances_recovered': True, 'derived_CD_squared': '8', 'dimension': 3},
            'finding': 'Even granting squared length 8 to each seed edge, a continuum of noncongruent tetrahedra and a planar realization satisfy all five constraints. Minimal affine dimension alone does not select the target. Declaring the two source cycles to act as isometries does propagate the missing CD distance to 8 and recovers the regular tetrahedral metric without reading CD.'}


def electron_test(target):
    results = []
    for s in map(Q, (2, 3, 4, 8, 12)):
        candidate = [row[:] for row in target]
        for i in range(4):
            candidate[i][4] = candidate[4][i] = s
        result = inspect_metric(candidate)
        assert Q(result['gram_determinant']) == 256*(s-3)
        assert result['euclidean'] == (s >= 3)
        if s >= 3:
            assert result['affine_dimension'] == (3 if s == 3 else 4)
            assert result['distinct_vertices']
        results.append({'equal_apex_distance_squared': str(s), 'height_squared': str(s-3), **result})
    assert all(target[i][j] == 8 for i, j in combinations(range(5), 2))
    assert inspect_metric(target)['affine_dimension'] == 4
    return {'base_squared_edge_length': '8', 'base_circumradius_squared': '3',
            'gram_determinant_formula': '256*(s-3), s=distance_squared(E,base_vertex)',
            'samples': results, 'full_ten_equal_length_constraints_force_dimension': 4,
            'finding': 'Equidistance of E alone permits variable height, including height zero. Requiring all ten edges to have the same squared length 8 forces height_squared=5 and dimension four, up to Euclidean isometry. This equal-length completion is extra source structure, not implied by incidence.'}


def neutron_test(target):
    source = json.loads((BASE/'results/four_six_center_cones.json').read_text())
    labels = [k for k in source['belt_scaled_coordinates'] if k != 'O']
    points = [tuple(map(Q, source['belt_scaled_coordinates'][k])) for k in labels]
    faces = [tuple(labels.index(k) for k in f) for f in source['belt_faces']]
    edges = {tuple(sorted(e)) for face in faces for e in combinations(face, 2)}
    weights = [Q(3), Q(1), Q(1)]
    g = Q(source['gap'])
    assert metric(points, weights) == target
    assert len(edges) == 12
    assert rigidity_rank(points, edges, weights) == 12
    gap_samples = []
    for h in (Q(1, 2), g, Q(1)):
        candidate = [(x, y*h/g, z) for x, y, z in points]
        distances = metric(candidate, weights)
        for i, j in edges:
            expected = Q(3) if labels[i][0] == labels[j][0] else 1+h*h
            assert distances[i][j] == expected
        assert len(supporting_faces(candidate, faces)) == 6
        gap_samples.append({'gap': str(h), 'side_squared_length': str(1+h*h),
                            'all_rim_squared_lengths': '3', **inspect_metric(distances)})
    # A noncongruent exact folded solution with ALL TWELVE edge lengths fixed:
    # U0's four neighbors lie in y+g*z=0. Reflect U0 through that plane.
    apex = labels.index('U0')
    opposite = labels.index('L0')
    neighbors = {j if i == apex else i for i, j in edges if apex in (i, j)}
    assert len(neighbors) == 4
    assert all(points[i][1]+g*points[i][2] == 0 for i in neighbors)
    x, y, z = points[apex]
    factor = 2*(y+g*z)/(1+g*g)
    folded = list(points)
    folded[apex] = (x, y-factor, z-factor*g)
    folded_metric = metric(folded, weights)
    assert same_constraints(folded_metric, target, edges)
    assert folded_metric[apex][opposite] != target[apex][opposite]
    assert folded_metric[apex][opposite] == (g*g-2)**2/(1+g*g)
    assert inspect_metric(folded_metric)['affine_dimension'] == 3
    assert inspect_metric(folded_metric)['distinct_vertices']
    # All side triangles remain nondegenerate: use their exact positive 2x2 Gram determinant.
    for i, j, k in faces:
        aa, bb = folded_metric[i][j], folded_metric[i][k]
        ab = (aa+bb-folded_metric[j][k])/2
        assert aa*bb-ab*ab > 0
    kept = supporting_faces(folded, faces)
    # Unoriented supporting-plane tests are insufficient: all six still pass.
    assert len(kept) == len(faces)
    oriented_kept = supporting_faces(folded, faces, preserve_outward_orientation=True)
    assert len(supporting_faces(points, faces, preserve_outward_orientation=True)) == 6
    assert len(oriented_kept) == 3
    caps = [tuple(labels.index(k) for k in rim) for rim in (
        ('U0', 'U1', 'U2'), ('L0', 'L1', 'L2'))]
    assert not supporting_faces(folded, caps)
    hull_faces = supporting_faces(points, list(combinations(range(6), 3)))
    assert {frozenset(f) for f in hull_faces} == {frozenset(f) for f in faces+caps}
    return {'surface_edges': len(edges), 'rigidity_matrix_rank': 12,
            'rigid_motion_dimension': 6, 'infinitesimal_flexes_beyond_rigid_motion': 0,
            'gap_samples_with_same_incidence_and_rim_lengths': gap_samples,
            'fixed_twelve_length_counterexample': {
                'moved_vertex': 'U0', 'operation': 'reflection through its four-neighbor plane y+g*z=0',
                'new_scaled_coordinates': list(map(str, folded[apex])),
                'all_source_edge_lengths_preserved': True,
                'old_missing_U0_L0_squared_distance': str(target[apex][opposite]),
                'new_missing_U0_L0_squared_distance': str(folded_metric[apex][opposite]),
                'remaining_unoriented_supporting_side_faces': len(kept),
                'remaining_source_oriented_supporting_side_faces': len(oriented_kept),
                'supporting_rim_planes': 0,
                'metric_check': inspect_metric(folded_metric)},
            'convex_hull_facets': len(hull_faces), 'stored_side_facets': len(faces),
            'finding': 'Incidence and rim lengths leave the gap free. Fixing all twelve surface lengths gives local rigidity but still admits a distinct folded realization. Unoriented side supporting-plane tests also pass that witness; source-preserving outward orientations or supporting rim planes reject it. The target convex hull has eight facets; marking two rims as open is still needed to select the six-panel belt.'}


def main():
    targets, evidence = load_targets()
    full = {name: inspect_metric(d) for name, (d, _, _) in targets.items()}
    assert [full[name]['affine_dimension'] for name in targets] == [3, 3, 4]
    report = {'hypothesis': 5, 'status': 'tested', 'full_target_metrics': full,
              'proton_seed_constraints': proton_test(targets['proton'][0]),
              'electron_equal_distance_constraints': electron_test(targets['electron_pentachoron'][0]),
              'neutron_belt_constraints': neutron_test(targets['neutron_belt'][0]),
              'sources': evidence,
              'implementation_sha256': {name: hashlib.sha256((BASE/'checkers'/name).read_bytes()).hexdigest()
                  for name in ('check_common_assembly_constraints.py', 'check_common_assembly_symmetry.py', 'check_common_assembly_cones.py')},
              'conclusion': 'Full metrics recover target dimensions 3,3,4, but bare incidence or seed-edge lengths do not select those metrics. Exact flat and folded counterexamples defeat naive minimum-dimension and distance-only assembly. Declaring the proton cycles to be isometries recovers its missing metric relation. Equal-length simplex completion forces the electron dimension; the belt additionally needs oriented geometric selection and protected rims.',
              'scope': 'Exact rational witnesses and local rigidity; no exhaustive classification of all belt realizations or new coefficient count.'}
    (BASE/'results/common_assembly_constraints.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
