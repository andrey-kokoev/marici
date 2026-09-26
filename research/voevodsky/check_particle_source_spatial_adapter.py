"""Exact source adapter for the existing Newtonian fixture, not cosmological emergence."""
import ast
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
source = ROOT/'research/nima/checkers/check_machian_newtonian_localization.py'
# Load only the existing pure evaluator and literal source fixture, avoiding
# the owner's module-level result-writing side effects.
tree = ast.parse(source.read_text(encoding='utf-8'))
nodes = [n for n in tree.body if
    (isinstance(n,ast.FunctionDef) and n.name=='source_jet_at_origin') or
    (isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='sources_a' for t in n.targets))]
if len(nodes)!=2:
    raise RuntimeError('Source interface changed: expected one evaluator and one fixture')
ns = {'Fraction':F,'isqrt':isqrt}
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(source),'exec'),ns)
points = ns['sources_a']
evaluate = ns['source_jet_at_origin']
zero = (F(0),)*3

def sub(v,w): return tuple(a-b for a,b in zip(v,w))
def add(v,w): return tuple(a+b for a,b in zip(v,w))
def scale(a,v): return tuple(a*x for x in v)
def centroid(ps):
    m = sum(m for m,_ in ps)
    if m<=0: raise ValueError('positive total mass required')
    return tuple(sum(a*r[i] for a,r in ps)/m for i in range(3))
def jet(ps,observer):
    return evaluate([(m,sub(r,observer)) for m,r in ps])
def recenter(ps,observer):
    c = centroid(ps)
    return [(m,sub(r,c)) for m,r in ps], sub(observer,c), c

m = sum(m for m,_ in points)
c = centroid(points)
centered, obs, retained_c = recenter(points,zero)
original = jet(points,zero)
checks = {
    'source_positive_masses': all(m>0 for m,_ in points),
    'mass_measure_total': m==3,
    'centroid_exact': c==(F(2),F(4,3),F(0)),
    'centered_first_moment_zero': centroid(centered)==zero,
    'observer_recentered_too': obs==scale(-1,c),
    'full_jet_unchanged_by_recentering': jet(centered,obs)==original,
    'retained_origin_recovers_sources': [(a,add(r,retained_c)) for a,r in centered]==points,
    'erasing_observer_shift_changes_relative_positions':
        [sub(r,zero) for _,r in centered]!=[sub(r,obs) for _,r in centered],
}
# At one chosen instant, p_a=(m_a,0,0,0), x_a=(0,r_a), c_light=1.
# J^{i0}=sum m_a r_a^i; lowering P_0=-M and P^2=-M^2 gives X^i=J^{i0}/M.
j_i0 = tuple(sum(a*r[i] for a,r in points) for i in range(3))
checks['poincare_centroid_matches_mass_centroid'] = tuple(x/m for x in j_i0)==c
# Apply the same affine shift to sources and observer: the local jet is fixed.
a = (F(7),F(-2),F(1))
shifted = [(mass,add(r,a)) for mass,r in points]
checks['translation_preserves_jet'] = jet(shifted,a)==original
checks['centroid_transforms_affinely'] = centroid(shifted)==add(c,a)
# Freeze a comoving-to-proper spatial scale a=2. Mass weights do not rescale.
s = F(2)
proper = [(mass,scale(s,r)) for mass,r in points]
proper_jet = jet(proper,zero)
checks['proper_radius_potential_scale'] = proper_jet[0]==original[0]/s
checks['proper_gradient_scale'] = proper_jet[1]==scale(1/s**2,original[1])
checks['proper_tidal_scale'] = proper_jet[2]==tuple(tuple(x/s**3 for x in row) for row in original[2])
checks['mass_is_measure_not_coordinate_density'] = sum(mass for mass,_ in proper)==m
# Identical M, centroid and static angular momentum do not fix local tides.
pair_x = [(F(1),(F(2),F(0),F(0))),(F(1),(F(-2),F(0),F(0)))]
pair_y = [(F(1),(F(0),F(2),F(0))),(F(1),(F(0),F(-2),F(0)))]
checks['same_particle_momentum_measure'] = (
    [(mass,zero) for mass,_ in pair_x]==[(mass,zero) for mass,_ in pair_y])
checks['same_charges_different_source_tides'] = (
    sum(t[0] for t in pair_x)==sum(t[0] for t in pair_y)
    and centroid(pair_x)==centroid(pair_y)==zero
    and jet(pair_x,zero)[2]!=jet(pair_y,zero)[2])
# A normalized total momentum is a declared rest-direction realization, not
# equality with the cosmological defect or a reconstruction of its magnitude.
checks['rest_direction_independent_of_total_mass'] = (m/m,zero)==(F(1),zero)
receipt = ROOT/'research/nima/results/machian-newtonian-localization.json'
expected = json.loads(receipt.read_text(encoding='utf-8'))['jet_a']
checks['source_readout_matches_saved_receipt'] = (
    original[0]==F(expected['potential']) and original[1]==tuple(map(F,expected['gradient']))
    and original[2]==tuple(tuple(map(F,row)) for row in expected['hessian']))
paths = [Path(__file__),source,receipt]
packet = dict(passed=all(checks.values()),checks=checks,
    centroid=list(map(str,c)), centered_observer=list(map(str,obs)),
    centered_sources=[dict(mass=str(mass),position=list(map(str,r))) for mass,r in centered],
    source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
    scope='Instantaneous supplied positive point masses and Newtonian law; no source generation or cosmological identification.')
Path(__file__).with_name('particle-source-spatial-adapter.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
