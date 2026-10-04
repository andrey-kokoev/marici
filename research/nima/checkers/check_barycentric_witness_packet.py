"""Exact finite barycentric subdivision, bound to checked Agda face supports."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, permutations
import hashlib
import json
import re
from agda_receipt_audit import OWNER, verify_receipt


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sign(order):
    inversions = sum(a > b for i, a in enumerate(order) for b in order[i + 1:])
    return (-1) ** inversions


def determinant(rows):
    return sum(sign(p) * rows[0][p[0]] * rows[1][p[1]] * rows[2][p[2]]
               for p in permutations(range(3)))


checked = verify_receipt('BarycentricWitnessPacket', 'barycentric-witness-packet', ['BarycentricBadMarkErasure'])
source = OWNER / 'agda/BarycentricWitnessPacket.agda'
text = source.read_text(encoding='utf-8')
# Accept only the displayed finite literal support grammar; no evaluation of Agda.
supports = {}
for name, rhs in re.findall(r'^support (\w+) = (.+)$', text, re.M):
    require(re.fullmatch(r'(?:[0-3] ∷ )+\[\]', rhs) is not None, 'nonliteral support')
    supports[name] = tuple(map(int, re.findall(r'[0-3]', rhs)))
faces = [f for n in range(1, 5) for f in combinations(range(4), n)]
require(len(supports) == 15 and set(supports.values()) == set(faces), 'face inventory differs')
name_of = {f: name for name, f in supports.items()}
centers = {f: tuple(Q(int(i in f), len(f)) for i in range(4)) for f in faces}
for f, point in centers.items():
    require(sum(point) == 1, 'barycentric weights')
    require(tuple(i for i, x in enumerate(point) if x > 0) == f, 'support recovery')
require(len(set(centers.values())) == 15, 'barycentric vertices must be distinct')

# Order complex: every simplex is a strictly nested chain of nonempty faces.
cells = {n: [chain for chain in combinations(faces, n + 1)
             if all(set(a) < set(b) for a, b in zip(chain, chain[1:]))]
         for n in range(4)}
counts = [len(cells[n]) for n in range(4)]
require(counts == [15, 50, 60, 24], 'subdivision f-vector')
for n in range(1, 4):
    lower = set(cells[n - 1])
    require(all(chain[:i] + chain[i + 1:] in lower for chain in cells[n] for i in range(n + 1)),
            'face closure')

incidences = Counter()
boundary = Counter()
volumes = []
flag_records = []
for order in permutations(range(4)):
    flag = tuple(tuple(sorted(order[:n])) for n in range(1, 5))
    require(flag in cells[3], 'maximal flag')
    # Inverse affine coordinates: lambda_j = j*(x_order[j-1]-x_order[j]),
    # with x_order[4] taken as zero. Nonnegativity is exactly sorted x.
    inverse = [[Q(j * (int(i == order[j-1]) - int(j < 4 and i == order[j])))
                for i in range(4)] for j in range(1, 5)]
    require(all(sum(centers[flag[j]][i] * inverse[j][k] for j in range(4)) == int(i == k)
                for i in range(4) for k in range(4)), 'affine reconstruction')
    require(all(sum(inverse[j][i] for j in range(4)) == 1 for i in range(4)), 'affine weight sum')
    points = [centers[f][1:] for f in flag]
    rows = [[points[j + 1][i] - points[0][i] for j in range(3)] for i in range(3)]
    signed_volume = determinant(rows) / 6
    orientation = sign(order)
    volume = orientation * signed_volume
    require(volume == Q(1, 144), 'oriented child volume')
    volumes.append(volume)
    flag_records.append({'faces': [name_of[f] for f in flag], 'orientation': orientation, 'volume': str(volume)})
    for i in range(4):
        triangle = flag[:i] + flag[i + 1:]
        incidences[triangle] += 1
        boundary[triangle] += orientation * (-1) ** i

require(sum(volumes) == Q(1, 6), 'volume conservation')
require(set(incidences) == set(cells[2]), 'all triangles covered')
full = (0, 1, 2, 3)
for triangle in cells[2]:
    internal = full in triangle
    require(incidences[triangle] == (2 if internal else 1), 'facet incidence count')
    require(boundary[triangle] == 0 if internal else abs(boundary[triangle]) == 1,
            'oriented boundary cancellation')
expected_boundary = Counter()
for missing in range(4):
    outer = tuple(i for i in range(4) if i != missing)
    for order in permutations(outer):
        flag = tuple(tuple(sorted(order[:n])) for n in range(1, 4))
        expected_boundary[flag] += (-1) ** missing * sign(order)
require({k: v for k, v in boundary.items() if v} == dict(expected_boundary), 'outer boundary agreement')
require(sum((-1) ** n * counts[n] for n in range(4)) == 1, 'ball Euler characteristic')
boundary_counts = [sum(full not in chain for chain in cells[n]) for n in range(3)]
require(boundary_counts == [14, 36, 24], 'boundary f-vector')
require(sum((-1) ** n * boundary_counts[n] for n in range(3)) == 2, 'boundary Euler characteristic')
# A volume score determines no unique accumulated flag.
require(len(set(volumes)) == 1 and len(flag_records) == 24, 'score collision control')

# A 2D projection for inspection only. All geometry checks above use exact 3D coordinates.
anchors = [(45, 240), (410, 235), (170, 50), (295, 390)]
def project(f):
    return tuple(float(sum(centers[f][i] * anchors[i][j] for i in range(4))) for j in range(2))
svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="500" viewBox="0 0 1000 500">',
       '<rect width="1000" height="500" fill="white"/>',
       '<g font-family="sans-serif" font-size="14" fill="#222">',
       '<text x="25" y="25">Four retained state occurrences</text>',
       '<text x="520" y="25">Barycentric face-incidence graph</text>']
for a, b in combinations(range(4), 2):
    x, y = anchors[a]; xx, yy = anchors[b]
    svg.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="#777"/>')
for i, (x, y) in enumerate(anchors):
    svg.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#222"/><text x="{x+8}" y="{y-8}">{i}</text>')
for a, b in cells[1]:
    x, y = project(a); xx, yy = project(b)
    svg.append(f'<line x1="{x+500}" y1="{y}" x2="{xx+500}" y2="{yy}" stroke="#999" stroke-width="0.7"/>')
colors = ['#222', '#2563eb', '#15803d', '#c2410c']
for f in faces:
    x, y = project(f); name = name_of[f]
    svg.append(f'<circle cx="{x+500}" cy="{y}" r="4" fill="{colors[len(f)-1]}"><title>{name}: retained face, CellType, cell</title></circle>')
    svg.append(f'<text x="{x+506}" y="{y-5}" font-size="11">{name}</text>')
svg += ['<text x="25" y="450">15 vertices; 50 edges; 60 triangles; 24 tetrahedra. Each small tetrahedron has volume 1/144.</text>',
        '<text x="25" y="475">Drawing is a projection. Face marks remain distinct even when their state values coincide.</text>', '</g></svg>']
(OWNER / 'results/barycentric-witness-packet.svg').write_text('\n'.join(svg) + '\n', encoding='utf-8')
result = {
    'schema': 'marici.nima.barycentric-witness-packet.v1', 'passed': True, **checked,
    'support_source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'subdivision_counts': counts, 'boundary_counts': boundary_counts,
    'interior_triangle_pairs_cancelled': 36, 'boundary_triangles': 24,
    'total_volume': str(sum(volumes)), 'volume_score_preimage_count': 24,
    'vertices': [{'face': name_of[f], 'support': list(f), 'weights': list(map(str, centers[f])),
                  'type_ref': f'BarycentricWitnessPacket.Example.CellType {name_of[f]}',
                  'term_ref': f'BarycentricWitnessPacket.Example.cell {name_of[f]}'} for f in faces],
    'maximal_flags': flag_records,
    'scope': 'Exact subdivision of one abstract occurrence-labelled tetrahedron; Agda binds each face to its Layer 2 type and witness. Coordinates are a chosen geometric realization, not inferred from arbitrary types or physical data.'
}
(OWNER / 'results/barycentric-witness-packet.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('PASS: typed face retention; exact barycentric subdivision [15,50,60,24]; oriented boundary cancellation; volume and score controls.')
