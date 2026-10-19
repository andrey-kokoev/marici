"""Research atlas: distinguish presentation covariance, stabilizers and field actions.
No physical group assignment or change to the owning rung constructors.
"""
from pathlib import Path
from itertools import permutations
from fractions import Fraction
import contextlib, io, json, hashlib, runpy, subprocess, sys

ROOT = Path(__file__).resolve().parents[3]
atlas_path = ROOT / 'research/strominger/rung-symmetry-atlas-v1.json'
atlas = json.loads(atlas_path.read_text(encoding='utf8'))
assert atlas['schema'] == 'marici.rung-symmetry-atlas.v1'
assert sorted(r['rung'] for r in atlas['rungs']) == list(range(4, 13))
for entry in atlas['rungs']:
    assert entry['object'] and entry['retained_structure'] and entry['boundary']
    assert all((ROOT / p).is_file() for p in entry['sources'])

# Reuse the actual retained-index constructors and rerun their owning checks.
log = io.StringIO()
sys.path.insert(0, str(ROOT / 'research/nima/checkers'))
try:
    with contextlib.redirect_stdout(log):
        original = runpy.run_path(str(ROOT / 'research/nima/checkers/check_seed_cycle_response_transport.py'))
finally:
    sys.path.pop(0)
Row, indexed, unindex = original['Row'], original['indexed'], original['unindex']
S4 = list(permutations(range(4)))
def compose(p, q): return tuple(p[q[i]] for i in range(4))
def parity(p): return sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4)) % 2

def records(edges):
    return tuple(Row(('edge', a, b), ('vertex', a), ('vertex', b), ((Fraction(1),),)) for a,b in sorted(edges))
def move_row(row, p):
    _, a, b = row.label
    return Row(('edge', p[a], p[b]), ('vertex', p[a]), ('vertex', p[b]), row.value, row.mass, row.members)
def move_rows(rows, p): return tuple(sorted((move_row(r, p) for r in rows), key=lambda r:r.label))
def move_view(view, p):
    # Move the outer keys AND the member endpoints independently of indexed().
    return {('vertex', p[key[1]]): tuple(sorted((move_row(r,p) for r in members),key=lambda r:r.label)) for key,members in view.items()}
def normalize(view): return {key:tuple(sorted(rows,key=lambda r:r.label)) for key,rows in view.items()}
def presentations(rows):
    at11 = indexed(rows,'source')
    at10 = indexed(unindex(at11),'target')
    return rows, normalize(at11), normalize(at10)

edges = {(a,b) for a in range(4) for b in range(4) if a != b}
source = records(edges)
p12,p11,p10 = presentations(source)
assert unindex(p11) == unindex(p10) == source
for p in S4:
    moved12,moved11,moved10 = presentations(move_rows(source,p))
    assert moved11 == move_view(p11,p)
    assert moved10 == move_view(p10,p)
    assert unindex(move_view(p11,p)) == move_rows(unindex(p11),p)
    for q in S4:
        assert move_view(move_view(p11,q),p) == move_view(p11,compose(p,q))
        assert move_view(move_view(p10,q),p) == move_view(p10,compose(p,q))

# Stabilizers are measured for declared structures, not read off rung numbers.
seed = {(0,1),(1,2),(2,0),(0,3),(3,1),(1,0)}
profiles = {}
for name, support in [('complete_directed_support',edges),('six_arrow_seed',seed),('excluded_directed_edge',edges-{(0,1)})]:
    rows,by_source,by_target=presentations(records(support))
    stabilizers = [[p for p in S4 if move_rows(rows,p)==rows],
                   [p for p in S4 if move_view(by_source,p)==by_source],
                   [p for p in S4 if move_view(by_target,p)==by_target]]
    assert stabilizers[0] == stabilizers[1] == stabilizers[2]
    profiles[name] = {'rungs':[12,11,10], 'stabilizer_order':len(stabilizers[0]), 'permutations':stabilizers[0]}
assert profiles['complete_directed_support']['stabilizer_order']==24
assert profiles['six_arrow_seed']['stabilizer_order']==2
assert profiles['excluded_directed_edge']['stabilizer_order']==2
assert len([p for p in S4 if p[0]==0])==6
assert len([p for p in S4 if parity(p)==0])==12
assert len(original['ordered_autos'])==1
# Negative control: keeping folder names fixed while moving records breaks the square.
p=(1,0,2,3)
bad={key:tuple(sorted((move_row(r,p) for r in rows),key=lambda r:r.label)) for key,rows in p11.items()}
assert bad != normalize(indexed(move_rows(source,p),'source'))
# Aggregating to counts is NOT the retained indexing map.
assert tuple(len(rows) for rows in p11.values()) == (3,3,3,3)
assert all(set(r.source for r in rows)=={key} for key,rows in p11.items())

replays=[]
for relative in ['research/nima/checkers/check_equivariant_carrier_edge_lifts.py','research/strominger/checkers/check_simplex_interface_algebra.py']:
    result=subprocess.run([sys.executable,str(ROOT/relative)],cwd=ROOT,text=True,capture_output=True,check=True,timeout=180)
    replays.append({'checker':relative,'status':'pass','stdout':result.stdout})
field = json.loads((ROOT/'research/strominger/results/simplex-interface-algebra/verification.json').read_text(encoding='utf8'))
assert field['status']=='pass'
assert atlas['unassigned_field_action']['order']==field['combinedGroup']['order']
assert atlas['unassigned_field_action']['joint_sector_ranks']==field['projectorAlgebra']['jointSectorRanks']
assert atlas['unassigned_field_action']['numerical_rung'] is None
assert all(r['role']=='horizontal-transport' for r in atlas['rungs'] if r['rung'] in (7,8,9))
for p in atlas['unassigned_field_action']['sources']+[atlas['historical_assignment']['source'],atlas['general_method_source']]:
    assert (ROOT/p).is_file()
sources=[Path(__file__),atlas_path,ROOT/'research/strominger/rung-symmetry-atlas-v1.md',ROOT/'research/nima/checkers/check_seed_cycle_response_transport.py',ROOT/'research/nima/checkers/check_rung_transport_diagram.py']+[ROOT/r['checker'] for r in replays]
report={'schema':'marici.rung-symmetry-atlas-check.v1','status':'pass',
        'indexing_checks':{'relabelings':24,'composition_pairs_per_indexed_presentation':576,'retained_presentations':[12,11,10],'wrong_fixed_keys_rejected':True},
        'support_stabilizers':profiles,'marked_vertex_stabilizer_order':6,'oriented_tetrahedron_vertex_symmetry_order':12,'ordered_seed_generators_stabilizer_order':1,
        'owning_seed_and_rung_replay':log.getvalue(),'other_replays':replays,
        'scope':'New tests use constant-payload endpoint-labelled support records with the existing indexing constructors. They do not identify the full 137-slot payload automorphisms or attach the 36-component field action to a rung. Prior seed transport and simplex group suites are freshly replayed at their declared scopes.',
        'direct_audit_source_hashes':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
out=ROOT/'research/strominger/results/rung-symmetry-atlas';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:report[k] for k in ['status','indexing_checks','support_stabilizers','marked_vertex_stabilizer_order','oriented_tetrahedron_vertex_symmetry_order','ordered_seed_generators_stabilizer_order']},indent=2))
