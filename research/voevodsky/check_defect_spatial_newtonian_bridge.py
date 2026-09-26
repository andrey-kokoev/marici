"""Exact finite tests of a defect-indexed Newtonian spatial realization.
Not a continuum proof or a Lorentz-covariant theory of Newtonian dynamics.
Run from any directory with Python 3; only the standard library is used.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]

def dot(v, w):
    return -v[0]*w[0] + sum(v[i]*w[i] for i in range(1, 4))

def scale(a, v):
    return tuple(a*x for x in v)

def sub(v, w):
    return tuple(a-b for a, b in zip(v, w))

def project(q, v):
    if dot(q, q) >= 0:
        raise ValueError('timelike defect required')
    return sub(v, scale(dot(v, q)/dot(q, q), q))

def boost(v):
    # Rational proper Lorentz boost, gamma=5/4, gamma*beta=3/4.
    t, x, y, z = v
    return (F(5,4)*t+F(3,4)*x, F(3,4)*t+F(5,4)*x, y, z)

def rotate(v):
    t, x, y, z = v
    return (t, -y, x, z)

q = (F(2), F(0), F(0), F(0))
frame = [tuple(F(i == j) for i in range(4)) for j in range(1, 4)]
basis = [tuple(F(i == j) for i in range(4)) for j in range(4)]
checks = {}
checks['boost_is_lorentz'] = all(dot(boost(v), boost(w)) == dot(v,w)
    for v in basis for w in basis)
checks['projector_idempotent_and_orthogonal'] = all(
    project(q, project(q,v)) == project(q,v) and dot(q,project(q,v)) == 0
    for v in basis)
checks['defect_scale_invariance'] = all(project(q,v) == project(scale(F(7),q),v) for v in basis)
checks['projector_naturality'] = all(
    project(boost(q),boost(v)) == boost(project(q,v)) for v in basis)
checks['boosted_frame_orthonormal'] = all(
    dot(boost(v),boost(w)) == F(i == j)
    for i,v in enumerate(frame) for j,w in enumerate(frame))

# Same source fixture as Nima's localization checker; compare its saved readout.
sources = [(F(2), scale(F(3), frame[0]), F(3)),
           (F(1), scale(F(4), frame[1]), F(4))]

def tidal(points, v, w):
    return sum(m*(dot(v,w)/r**3 - 3*dot(a,v)*dot(a,w)/r**5)
               for m,a,r in points)

def tensor(points, axes):
    return [[tidal(points,v,w) for w in axes] for v in axes]

receipt = ROOT / 'research/nima/results/machian-newtonian-localization.json'
old = json.loads(receipt.read_text(encoding='utf-8'))
e = tensor(sources,frame)
checks['radii_from_inherited_metric'] = all(dot(a,a) == r*r for _,a,r in sources)
checks['original_tidal_fixture_recovered'] = e == [[F(x) for x in row] for row in old['jet_a']['hessian']]
checks['original_potential_recovered'] = -sum(m/r for m,_,r in sources) == F(old['jet_a']['potential'])
checks['original_gradient_recovered'] = [
    -sum(m*dot(a,v)/r**3 for m,a,r in sources) for v in frame
] == [F(x) for x in old['jet_a']['gradient']]
boosted = [(m,boost(a),r) for m,a,r in sources]
checks['transported_tidal_components_equal'] = tensor(boosted,list(map(boost,frame))) == e
checks['vacuum_trace_zero'] = sum(e[i][i] for i in range(3)) == 0
checks['relative_acceleration_x'] = -e[0][0] == F(229,1728)
# Two isometries carry q to the same q': endpoints alone do not identify fibers.
checks['two_maps_same_defect_endpoint'] = boost(q) == boost(rotate(q))
checks['two_maps_different_spatial_transport'] = boost(frame[0]) != boost(rotate(frame[0]))
checks['naive_projection_not_isometry'] = dot(project(boost(q),frame[0]),project(boost(q),frame[0])) != 1
# Wrong-sign and coordinate-erasure controls must be distinguishable.
checks['wrong_tidal_sign_detected'] = [[-x for x in row] for row in e] != e
checks['dropping_boosted_time_coordinate_changes_metric'] = sum(x*x for x in boost(frame[0])[1:]) != 1
for label,bad in [('null',(F(1),F(1),F(0),F(0))), ('zero',(F(0),)*4),
                  ('spacelike',(F(0),F(1),F(0),F(0)))]:
    try:
        project(bad,frame[0])
    except ValueError:
        checks[label+'_defect_rejected'] = True
    else:
        checks[label+'_defect_rejected'] = False

paths = [Path(__file__), receipt,
    ROOT/'research/nima/checkers/check_machian_newtonian_localization.py',
    ROOT/'src/ledger/20260814-124 Spatial Geometry from the Cosmological Defect.md']
out = dict(schema='marici.defect-spatial-newtonian-bridge.v1', passed=all(checks.values()),
    checks=checks, tidal=[[str(x) for x in row] for row in e],
    source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
    scope='Exact finite fixtures; no physical identification of momentum and position, no dynamics selection.')
target = Path(__file__).with_name('defect-spatial-newtonian-bridge.json')
target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
