"""Hypothesis 4: one exact symmetry/orbit operation on three stored targets.

This is an inverse reconstruction test, not derivation from minimal arrows:
metrics and cells are read from the target records. Barycentric cell vertices
allow the same permutation action in every dimension. Attachment marks are
also tested, rather than silently erased to obtain a larger symmetry group.
"""
from fractions import Fraction as Q
from itertools import permutations, combinations
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parents[1]
RESEARCH = BASE.parent


def determinant(matrix):
    a = [list(row) for row in matrix]
    result = Q(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        v = a[j][j]
        result *= v
        for i in range(j+1, len(a)):
            c = a[i][j]/v
            for k in range(j+1, len(a)):
                a[i][k] -= c*a[j][k]
    return result


def inverse(matrix):
    n = len(matrix)
    a = [list(row)+[Q(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for j in range(n):
        p = next(i for i in range(j, n) if a[i][j])
        a[j], a[p] = a[p], a[j]
        v = a[j][j]
        a[j] = [x/v for x in a[j]]
        for i in range(n):
            if i != j:
                v = a[i][j]
                a[i] = [x-v*y for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a]


def affine_coordinates(distances):
    n = len(distances)
    gram = [[(distances[0][i]+distances[0][j]-distances[i][j])/2
             for j in range(n)] for i in range(n)]
    basis = []
    for i in range(1, n):
        candidate = basis+[i]
        if determinant([[gram[j][k] for k in candidate] for j in candidate]):
            basis = candidate
    inv = inverse([[gram[i][j] for j in basis] for i in basis])
    coordinates = [tuple(sum(inv[i][j]*gram[basis[j]][k] for j in range(len(basis)))
                         for i in range(len(basis))) for k in range(n)]
    return basis, coordinates


def vertex(n, i):
    return tuple(Q(i == j) for j in range(n))


def cell(vertices):
    return tuple(sorted(vertices))


def act_vertex(v, p):
    out = [Q(0)]*len(p)
    for i, j in enumerate(p):
        out[j] = v[i]
    return tuple(out)


def act_cell(c, p):
    return cell(act_vertex(v, p) for v in c)


def analyze(distances, cells, marks=()):
    """Identical operation; no particle label or expected cardinality argument."""
    n = len(distances)
    basis, coordinates = affine_coordinates(distances)
    cells = set(cells)
    group = []
    for p in permutations(range(n)):
        if any(distances[i][j] != distances[p[i]][p[j]] for i in range(n) for j in range(n)):
            continue
        matrix = [[coordinates[p[b]][k]-coordinates[p[0]][k] for b in basis]
                  for k in range(len(basis))]
        if determinant(matrix) != 1:
            continue
        if any({p[i] for i in mark} != set(mark) for mark in marks):
            continue
        if {act_cell(c, p) for c in cells} != cells:
            continue
        group.append(p)
    group_set = set(group)
    assert all(tuple(p[q[i]] for i in range(n)) in group_set for p in group for q in group)
    unseen, orbits = set(cells), []
    while unseen:
        seed = min(unseen)
        orbit = {act_cell(seed, p) for p in group}
        assert orbit <= unseen
        unseen -= orbit
        orbits.append(orbit)
    rebuilt = set().union(*orbits)
    assert rebuilt == cells
    # Preserve all shared codimension-one interfaces, not merely cell counts.
    def seams(complex_cells):
        return {tuple(sorted((a, b))) for a, b in combinations(complex_cells, 2)
                if len(set(a) & set(b)) == min(len(a), len(b))-1}
    expected_seams = seams(cells)
    assert seams(rebuilt) == expected_seams
    connected = {min(cells)}
    while True:
        extended = connected | {b for a, b in expected_seams if a in connected} | {
            a for a, b in expected_seams if b in connected}
        if extended == connected:
            break
        connected = extended
    # Orbit adjacency exposes geometrically joined but symmetry-distinct sectors.
    cross_orbit_seams = []
    for i, left in enumerate(orbits):
        for j, right in enumerate(orbits):
            if i < j:
                count = sum(tuple(sorted((a, b))) in expected_seams for a in left for b in right)
                if count:
                    cross_orbit_seams.append([i, j, count])
    return {'affine_dimension': len(basis), 'proper_symmetries': len(group),
            'cells': len(cells), 'orbit_sizes': sorted(map(len, orbits)),
            'minimum_orbit_representatives': len(orbits),
            'exact_cells_and_seams_reconstructed': True,
            'shared_interfaces': len(expected_seams),
            'cell_adjacency_connected': len(connected) == len(cells),
            'cross_orbit_seams': cross_orbit_seams,
            'fixed_marks': [list(m) for m in marks]}


def metric(points, weights):
    return [[sum(w*(a-b)**2 for w, a, b in zip(weights, x, y)) for y in points] for x in points]


def load_targets():
    proton_source = RESEARCH/'nima/inputs/proton-six-arrows.json'
    proton_geometry = RESEARCH/'nima/results/twelve-triangle-positive-geometry.json'
    belt_source = BASE/'results/four_six_center_cones.json'
    electron_source = BASE/'electron-pentachoron-attachment.md'
    p = json.loads(proton_source.read_text())
    p_rows = json.loads(proton_geometry.read_text())['triangles_and_transports']
    labels = list(p['vertices'])
    pv = [tuple(map(Q, p['vertices'][k])) for k in labels]
    pc = []
    for row in p_rows:
        f, a, b = row['triangle']
        face = f.removeprefix('F_')
        centre = tuple(Q(k in face, len(face)) for k in labels)
        pc.append(cell((centre, vertex(4, labels.index(a)), vertex(4, labels.index(b)))))
    belt = json.loads(belt_source.read_text())
    assert belt['verification_passed']
    # Stored X is scaled: physical x = sqrt(3)*X. Use its exact metric.
    bl = [k for k in belt['belt_scaled_coordinates'] if k != 'O']
    bv = [tuple(map(Q, belt['belt_scaled_coordinates'][k])) for k in bl]
    bc = []
    for face in belt['belt_faces']:
        centre = tuple(Q(k in face, 3) for k in bl)
        for a, b in zip(face, face[1:]+face[:1]):
            bc.append(cell((centre, vertex(6, bl.index(a)), vertex(6, bl.index(b)))))
    # Exact metric from the documented 4D electron realization:
    # ABCD=(+/-1,+/-1,+/-1,0), E=(0,0,0,sqrt(5)).
    # Radicals cancel in squared distances; do not use its 3D projection.
    text = electron_source.read_text(encoding='utf-8')
    assert 'E=(0,0,0,√5)' in text and 'squared length 8' in text
    ed = [[Q(0 if i == j else 8) for j in range(5)] for i in range(5)]
    ec = [cell(vertex(5, i) for i in face) for face in combinations(range(5), 4)]
    targets = {
        'proton': (metric(pv, [1, 1, 1]), pc, ((0, 1, 2),)),
        'neutron_belt': (metric(bv, [3, 1, 1]), bc,
                         (tuple(i for i, k in enumerate(bl) if k.startswith('U')),
                          tuple(i for i, k in enumerate(bl) if k.startswith('L')))),
        'electron_pentachoron': (ed, ec, ((0, 1, 2, 3),)),
    }
    evidence = {str(path.relative_to(RESEARCH)): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in (proton_source, proton_geometry, belt_source, electron_source)}
    return targets, evidence


def main():
    targets, evidence = load_targets()
    results = {name: {'unmarked': analyze(d, c), 'attachment_preserving': analyze(d, c, marks)}
               for name, (d, c, marks) in targets.items()}
    assert results['proton']['unmarked']['orbit_sizes'] == [12]
    assert results['proton']['attachment_preserving']['orbit_sizes'] == [3, 3, 3, 3]
    assert results['neutron_belt']['unmarked']['orbit_sizes'] == [6, 6, 6]
    assert results['electron_pentachoron']['unmarked']['orbit_sizes'] == [5]
    assert results['electron_pentachoron']['attachment_preserving']['orbit_sizes'] == [1, 4]
    report = {'hypothesis': 4, 'status': 'tested', 'results': results, 'sources': evidence,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'conclusion': 'Common multi-orbit reconstruction succeeds on supplied target metrics and cells. Single-orbit assembly fails for the belt and for all three attachment-marked targets. Minimal source derivation and inter-orbit coefficient transport remain unproved.',
              'scope': 'Exact geometric inverse test; no new particle coefficient count or source-arrow constructor.'}
    dest = BASE/'results/common_assembly_symmetry.json'
    dest.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
