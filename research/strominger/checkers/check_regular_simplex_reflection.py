"""Execute and certify the complete regular 4-simplex reflection experiment."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from dataclasses import asdict, is_dataclass
import hashlib
import json
import math
import sys
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
sys.path.insert(0, str(BASE))
import regular_simplex_reflection as M
OUT = BASE / 'results/regular-simplex-reflection-v1'
OUT.mkdir(parents=True, exist_ok=True)


def encoded(x):
    if isinstance(x, Q):
        return str(x)
    if is_dataclass(x):
        return encoded(asdict(x))
    if isinstance(x, dict):
        return {str(k): encoded(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [encoded(v) for v in x]
    return x


def regular(vertices):
    return all(M.inner(M.sub(a, b), M.sub(a, b)) == 2 for a, b in combinations(vertices, 2))


assert regular(M.SEED)
origin5 = M.embed5(M.ZERO)
basis5 = [M.sub(M.embed5(e), origin5) for e in M.IDENTITY]
assert tuple(tuple(sum(a*b for a,b in zip(x,y)) for y in basis5) for x in basis5) == M.GRAM
# The edge-coordinate matrix is triangular with diagonal 1: affine rank 4.
edges = [M.sub(p,M.SEED[0]) for p in M.SEED[1:]]
assert all(edges[i][i] == 1 and all(edges[i][j] == 0 for j in range(i+1,4)) for i in range(4))
for i, p in enumerate(M.SEED):
    assert M.embed5(p) == tuple(Q(int(i == j)) - Q(1, 5) for j in range(5))
    assert sum(M.embed5(p)) == 0
stages, operations, h, support = M.construct()
assert [len(s) for s in stages] == [1, 2, 4, 8, 16]
assert h == 1
assert {tuple(sorted(e['vertices'])) for e in support} == {tuple(sorted([M.SEED[1], M.SEED[2]]))}
for name, op in operations.items():
    assert op.isometry()
    if 'rotation' in name:
        assert op.after(op).after(op) == M.Affine() and op != M.Affine()
    else:
        assert op.after(op) == M.Affine()
for old, new in zip(stages, stages[1:]):
    assert new[:len(old)] == old
    assert len({c.id for c in new}) == len(new)
for c in stages[-1]:
    assert regular(c.vertices)
    assert c.frame.isometry()
    for a, b in combinations(c.vertices, 2):
        delta = M.sub(M.embed5(a), M.embed5(b))
        assert sum(x*x for x in delta) == 2
    assert all(sum(M.embed5(p)) == 0 for p in c.vertices)
groups, intersections, contacts, adjacency = M.contact_analysis(stages[-1])
assert len(groups) == 14 and len(contacts) == 14
seen, todo = set(), [0]
while todo:
    v = todo.pop()
    if v not in seen:
        seen.add(v)
        todo.extend(adjacency[v])
assert len(seen) == len(groups)
cycle = M.core_cycle(adjacency)
assert len(cycle) == 6
assert all(M.ZERO in groups[i][0].vertices for i in cycle)
product = M.Affine()
permutation = tuple(range(5))
seams = []
for a, b in zip(cycle, cycle[1:] + cycle[:1]):
    contact = next(e for e in contacts if set(e['cells']) == {a, b})
    seam = contact['map']
    source, target = groups[a][0].vertices, groups[b][0].vertices
    assert set(map(seam, source)) == set(target)
    local = tuple(target.index(seam(p)) for p in source)
    permutation = tuple(local[i] for i in permutation)
    product = seam.after(product)
    seams.append({'fromCell': a, 'toCell': b, 'edge': contact['vertices'], 'map': seam, 'labels': local})
assert product == M.Affine() and permutation == tuple(range(5))
for p in groups[cycle[0]][0].vertices:
    assert product(p) == p and M.embed5(product(p)) == M.embed5(p)
faces = [set() for _ in range(5)]
for group in groups:
    vs = group[0].vertices
    for d in range(5):
        faces[d].update(tuple(sorted(face)) for face in combinations(vs, d+1))
f_vector = list(map(len, faces))
euler = sum((-1)**i*n for i, n in enumerate(f_vector))
assert euler == 1
# Controls reject a corner substituted for an edge and projection-only identity.
try:
    M.construct(first_center=(Q(1, 2), Q(0)))
except ValueError as error:
    assert 'no actual simplex edge' in str(error)
else:
    raise AssertionError('Midpoint variant incorrectly admitted its red reflection')
changed = list(M.SEED)
changed[-1] = changed[-1][:3] + (Q(2),)
assert [p[:2] for p in changed] == [p[:2] for p in M.SEED]
assert set(changed) != set(M.SEED) and not regular(changed)
red_without_translation = M.Affine(operations['red'].linear)
assert any(red_without_translation(p) != p for p in (M.SEED[1], M.SEED[2]))

# Static rendering only: every geometric calculation above used Fractions.
def render():
    panels = []
    for hidden, title in [(False, 'Working-face projection: actual six-seam circuit'),
                          (True, 'Oblique 4D projection: all five vertices / ten edges')]:
        def project(p):
            u, v, s, t = map(float, p)
            return (u + v/2 + (0.31*s-0.28*t if hidden else 0),
                    -math.sqrt(3)*v/2 + (-0.25*s-0.34*t if hidden else 0))
        points = [project(p) for group in groups for p in group[0].vertices]
        lo = [min(p[i] for p in points) for i in range(2)]
        hi = [max(p[i] for p in points) for i in range(2)]
        scale = min(540/(hi[0]-lo[0]), 460/(hi[1]-lo[1]))
        def xy(p):
            x,y = project(p)
            return (30+(x-lo[0])*scale, 55+(y-lo[1])*scale)
        parts = [f'<text x="20" y="25" font-size="17">{title}</text>']
        for i, group in enumerate(groups):
            vs = group[0].vertices
            color = '#badcff' if i in cycle else '#e7e7ec'
            polygon = ' '.join(f'{x:.3f},{y:.3f}' for x,y in map(xy, vs[:3]))
            parts.append(f'<polygon points="{polygon}" fill="{color}" stroke="#455265" stroke-width="1.3"/>')
            if hidden:
                for a,b in combinations(vs,2):
                    x,y = xy(a); u,v = xy(b)
                    parts.append(f'<line x1="{x:.3f}" y1="{y:.3f}" x2="{u:.3f}" y2="{v:.3f}" stroke="#526b83" opacity="0.65"/>')
                for k,p in enumerate(vs):
                    x,y = xy(p)
                    parts.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{3 if k>2 else 2}" fill="{chr(35)+"c0427a" if k>2 else chr(35)+"334455"}"><title>Cell {i}, inherited vertex {k}: {p}</title></circle>')
            center = tuple(sum(v[k] for v in vs[:3])/3 for k in range(4))
            x,y = xy(center)
            parts.append(f'<text x="{x:.3f}" y="{y:.3f}" font-size="11">{i}</text>')
        if not hidden:
            centers = [tuple(sum(v[k] for v in groups[i][0].vertices[:3])/3 for k in range(4)) for i in cycle+cycle[:1]]
            path = ' '.join(f'{x:.3f},{y:.3f}' for x,y in map(xy, centers))
            parts.append(f'<polyline points="{path}" fill="none" stroke="#1672cf" stroke-width="3"/>')
        panels.append(''.join(parts))
    return '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="560" viewBox="0 0 1200 560"><rect width="1200" height="560" fill="white"/><g font-family="sans-serif">'+panels[0]+'<g transform="translate(600,0)">'+panels[1]+'</g></g></svg>\n'

svg = render()
ET.fromstring(svg)
(OUT/'assembly.svg').write_text(svg, encoding='utf-8')
paths = [Path(__file__).resolve(), BASE/'regular_simplex_reflection.py', ROOT/'research/chatgpt/reflection_experiment_note.md']
source_hashes = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
stage_records = []
for name, stage in zip(['seed','white clone','first rotation clone','outer red clone','second rotation clone'],stages):
    stage_records.append({'name':name,'histories':len(stage),'distinctCells':len(M.geometry_groups(stage)),
                          'copies':[{'id':c.id,'parent':c.parent,'word':c.word,'frame':c.frame,'vertices4':c.vertices,'vertices5':tuple(map(M.embed5,c.vertices))} for c in stage]})
result = {'passed':True,'schema':'regular-4-simplex.reflection-construction.v1',
          'seed':{'coordinates4':M.SEED,'coordinates5':tuple(map(M.embed5,M.SEED)),'gram':M.GRAM,'edgeSquared':2},
          'protocol':{'workingFace':[0,1,2],'whiteEdge':[0,1],'rotationCenters':[(0,0),(0,0)],'angleDegrees':120,
                      'redNormal':(1,1,0,0),'computedRedSupport':h,'actualSupportingEdges':support,'operations':operations},
          'stages':stage_records,'geometryGroups':[{'cell':i,'copies':[c.id for c in g]} for i,g in enumerate(groups)],
          'intersections':intersections,'contacts':contacts,'contactGraph':{'vertices':len(groups),'edges':len(contacts),'components':1,'cycleRank':1},
          'centralCircuit':{'cells':cycle,'seams':seams,'product':product,'labelReturn':permutation},
          'simplicialFVector':f_vector,'eulerCharacteristic':euler,
          'intersectionCertificate':'All hidden-vertex projections are strictly interior. Distinct projected triangles intersect only on boundaries; therefore full-simplex intersections equal the computed zero-hidden-coordinate edge/vertex intersections.',
          'negativeControls':['Midpoint rotation has no actual outer red supporting edge','Equal projections do not identify different complete 4D cells','Dropping red affine translation does not fix the supporting edge'],
          'conclusion':'The complete regular 4-simplex cloning sequence retains sixteen histories and produces fourteen distinct regular 4-simplexes. Its six-cell central shared-edge circuit closes exactly on the whole affine frame and all five vertex labels.',
          'sourceHashes':source_hashes}
(OUT/'verification.json').write_text(json.dumps(encoded(result),indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'stages':[(s['histories'],s['distinctCells']) for s in stage_records],
                  'fVector':f_vector,'contactGraph':result['contactGraph'],'centralCircuit':cycle,'wholeFrameReturn':'identity',
                  'conclusion':result['conclusion']},indent=2))
