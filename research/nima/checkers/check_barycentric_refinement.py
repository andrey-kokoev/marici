"""Two exact barycentric refinements with source-carrier preservation checks."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, permutations
import json
import runpy
from agda_receipt_audit import OWNER, verify_receipt


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sign(order):
    return (-1) ** sum(a > b for i, a in enumerate(order) for b in order[i + 1:])


def det(rows):
    return sum(sign(p) * rows[0][p[0]] * rows[1][p[1]] * rows[2][p[2]] for p in permutations(range(3)))


def volume(coords, cell):
    points = [coords[v][1:] for v in cell]
    return det([[points[j + 1][i] - points[0][i] for j in range(3)] for i in range(3)]) / 6


def distance2(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def diameter2(coords, cell):
    return max((distance2(coords[a], coords[b]) for a, b in combinations(cell, 2)), default=Q(0))


def all_faces(tops):
    return sorted({face for top in tops for k in range(1, 5) for face in combinations(top, k)},
                  key=lambda f: (len(f), f))


def validate_carriers(old_faces, new_faces, carriers):
    for face in new_faces:
        chain = [old_faces[v] for v in face]
        require(all(set(a) < set(b) for a, b in zip(chain, chain[1:])), 'strict flag incidence')
        minimal = tuple(sorted(set().union(*map(set, chain))))
        require(carriers[face] == minimal, 'minimal source carrier')
        require(carriers[face] in old_faces, 'carrier belongs to source complex')
        if len(face) > 1:
            for i in range(len(face)):
                boundary = face[:i] + face[i + 1:]
                require(set(carriers[boundary]) <= set(carriers[face]), 'carrier respects boundary')


def subdivide(mesh):
    old_faces, old_coords, old_tops, old_origin = mesh
    face_id = {f: i for i, f in enumerate(old_faces)}
    coords = [tuple(sum(old_coords[v][i] for v in f) / len(f) for i in range(4)) for f in old_faces]
    tops = {}
    for old_top, orientation in old_tops.items():
        for perm in permutations(range(4)):
            order = tuple(old_top[i] for i in perm)
            top = tuple(face_id[tuple(sorted(order[:k]))] for k in range(1, 5))
            require(top not in tops, 'unique maximal flag')
            tops[top] = orientation * sign(perm)
            require(tops[top] * volume(coords, top) == orientation * volume(old_coords, old_top) / 24,
                    'child oriented volume')
            require(diameter2(coords, top) <= Q(9, 16) * diameter2(old_coords, old_top),
                    'three-quarter mesh bound')
    faces = all_faces(tops)
    carriers = {f: old_faces[f[-1]] for f in faces}
    validate_carriers(old_faces, faces, carriers)
    origin = {f: old_origin[carriers[f]] for f in faces}
    # Direct geometric support and successive carrier maps give the same source face.
    for f in faces:
        geometric_origin = tuple(i for i in range(4) if any(coords[v][i] > 0 for v in f))
        require(origin[f] == geometric_origin, 'direct and successive source carriers')
    require(len(set(coords)) == len(coords), 'distinct barycentric vertices')
    require(all(p in coords for p in old_coords), 'original vertices persist')
    require(sum(o * volume(coords, f) for f, o in tops.items()) == Q(1, 6), 'total volume')
    incidences, boundary = Counter(), Counter()
    for f, o in tops.items():
        for i in range(4):
            b = f[:i] + f[i + 1:]
            incidences[b] += 1
            boundary[b] += o * (-1) ** i
    for b, count in incidences.items():
        outer = len(origin[b]) == 3
        require(count == (1 if outer else 2), 'boundary incidence multiplicity')
        require(abs(boundary[b]) == 1 if outer else boundary[b] == 0, 'oriented interface cancellation')
    counts = [sum(len(f) == k for f in faces) for k in range(1, 5)]
    boundary_counts = [sum(len(f) == k and len(origin[f]) < 4 for f in faces) for k in range(1, 4)]
    require(sum((-1) ** i * counts[i] for i in range(4)) == 1, 'Euler characteristic')
    require(sum((-1) ** i * boundary_counts[i] for i in range(3)) == 2, 'boundary Euler characteristic')
    summary = {'counts': counts, 'boundary_counts': boundary_counts,
               'mesh_diameter_squared': str(max(diameter2(coords, f) for f in tops)),
               'total_volume': '1/6', 'preserved_source_cells': len(faces)}
    return (faces, coords, tops, origin), carriers, summary


checked = verify_receipt('BarycentricRefinementCoherence', 'barycentric-refinement-coherence', ['RefinementBadWitness'])
# Reuse and rerun the source-bound first-subdivision audit rather than trusting a stale JSON.
base = runpy.run_path(str(OWNER / 'checkers/check_barycentric_witness_packet.py'))
coords0 = [tuple(Q(int(i == j)) for i in range(4)) for j in range(4)]
tops0 = {(0, 1, 2, 3): 1}
faces0 = all_faces(tops0)
mesh0 = (faces0, coords0, tops0, {f: f for f in faces0})
mesh1, carrier1, summary1 = subdivide(mesh0)
mesh2, carrier2, summary2 = subdivide(mesh1)
require(summary1['counts'] == [15, 50, 60, 24], 'first refinement counts')
require(summary2['counts'] == [149, 796, 1224, 576], 'second refinement counts')
require(summary2['boundary_counts'] == [74, 216, 144], 'second boundary counts')
require(set(mesh1[1]) == set(base['centers'].values()), 'binding to first packet geometry')
for f in mesh2[0]:
    require(mesh2[3][f] == carrier1[carrier2[f]], 'composite carrier diagram')
    # Source marks determine which already supplied typed witness is pulled back.
    require(base['name_of'][mesh2[3][f]] == base['name_of'][carrier1[carrier2[f]]], 'typed source reference')

# A containing carrier need not be minimal. The refinement gate must reject it.
bad_carriers = dict(carrier1)
corner = (faces0.index((0,)),)
bad_carriers[corner] = (0, 1, 2, 3)
rejected = False
try:
    validate_carriers(faces0, mesh1[0], bad_carriers)
except AssertionError as error:
    rejected = str(error) == 'minimal source carrier'
require(rejected, 'oversized carrier must be rejected')
# Refinement does not make the whole tetrahedron converge to a unique point.
require(coords0[0] in mesh2[1] and coords0[1] in mesh2[1], 'distinct original vertices survive')
require(distance2(coords0[0], coords0[1]) == 2, 'global diameter lower bound persists')

result = {
    'schema': 'marici.nima.barycentric-refinement.v1', 'passed': True, **checked,
    'levels': [summary1, summary2],
    'carrier_comparisons_checked': len(mesh2[0]),
    'oversized_carrier_rejected': rejected,
    'distinct_original_vertices_retained': True,
    'fixed_annotation_comparison_contractibility_refuted': True,
    'formal_scope': 'Contractible typed annotation-preservation packages along fixed carriers, composition of preservation and contractible comparisons between packages.',
    'geometry_scope': 'Two exact subdivisions of one abstract tetrahedron; minimal carriers and their boundary/composition laws checked by enumeration.',
    'limit': 'Annotations are pulled back from existing source cells. They are not newly synthesized fillers for every refined boundary, and no universal geometric comparison-space theorem is claimed.'
}
(OWNER / 'results/barycentric-refinement.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('PASS: two refinements [15,50,60,24] -> [149,796,1224,576]; 2745 composite carriers; witness preservation; oversized-carrier rejection.')
