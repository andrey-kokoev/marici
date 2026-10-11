"""Payload-preserving history-dependent realization of actual source swap.

Native route-count difference drives a declared field readout. The existing
numerical update is reused unchanged. This changes the INITIAL ENCODING:
it is not an energy-free preparation from the old empty-bank baseline.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import re
from check_phase_memory_first_moment import step, total, moments, add, project
from check_twelve_triangle_positive_geometry import POINTS, mean

ROOT = Path(__file__).resolve().parents[1]
source = ROOT/'agda/NativeFeedbackRouteReadout.agda'
proof_path = ROOT/'results/agda-NativeFeedbackRouteReadout.json'
proof = json.loads(proof_path.read_text(encoding='utf-8-sig'))
assert proof['passed'] and proof['ignore_interfaces'] and proof['inputs_stable_during_check']
assert proof['source_sha256'] == hashlib.sha256(source.read_bytes()).hexdigest()
text = source.read_text(encoding='utf-8')
initial_counts = tuple(map(int,re.search(r'initial-reading : reading input ≡ \((\d+) , (\d+)\)',text).groups()))
returned_counts = tuple(map(int,re.search(r'returned-reading : reading \(F.F.exchange input\) ≡ \((\d+) , (\d+)\)',text).groups()))
assert returned_counts == initial_counts[::-1]
geometry_path = ROOT/'results/twelve-triangle-positive-geometry.json'
rows = json.loads(geometry_path.read_text())['triangles_and_transports']
i = next(k for k,r in enumerate(rows) if r['outer_arrow']=='AB')
j = next(k for k,r in enumerate(rows) if r['outer_arrow']=='BA')
d = tuple(F(int(k==i)-int(k==j)) for k in range(12))
u = (F(1),)*12
zero = (F(0),)*12


def encode(counts, gain):
    beta = gain*(counts[0]-counts[1])
    contrast = tuple(beta*v for v in d)
    return add(u,contrast),tuple(-v for v in contrast)


checks=[]
def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


check('existing-empty-bank-fixed', step(u,zero)==(u,zero))
check('contrast-is-unread-mean-zero', project(d)==zero)
for a,b,gain in product(range(4),range(4),(F(0),F(1,2),F(1),F(2))):
    state = encode((a,b),gain)
    name = f'{a}/{b}/{gain}'
    beta = gain*(a-b)
    check('intertwining/'+name, step(*state)==encode((b,a),gain))
    check('baseline-payload-preserved/'+name, add(*state)==u)
    check('budget/'+name,total(*state)==F(80)+F(80,3)*beta*beta)
    check('nonempty-bank-explicit/'+name,(state[1]==zero)==(beta==0))
    check('update-is-conservative/'+name,total(*step(*state))==total(*state))

first = encode(initial_counts,F(1))
second = encode(returned_counts,F(1))
check('actual-native-orbit-visible', first != second and step(*first)==second and step(*second)==first)
check('not-old-empty-bank-initialization', first != (u,zero))
check('preparation-budget-not-free',total(*first)-total(u,zero)==F(80,3))
check('record-erasure-changes-decoded-payload',add(first[0],zero)!=u)

# Existing positional diagnostics, with their previous source geometry and
# conventions. These are amplitude-intensity centers, NOT particle positions.
pts=dict(POINTS)
for row in rows:
    label=row['triangle'][0]
    pts[label]=mean([POINTS[k] for k in label[2:]])
positions=[mean([(F(0),)*3]+[pts[k] for k in row['triangle']]) for row in rows]
readings=[moments(*state,positions) for state in (first,second)]
check('existing-active-center-detects-history-swap',readings[0]['active_center']!=readings[1]['active_center'])
check('coherent-payload-first-moment-fixed',readings[0]['recombined_first_moment']==readings[1]['recombined_first_moment'])
# Coarse field coordinates do not replace the source comparison: translated
# count pairs have the same difference, despite different retained routes.
check('numeric-map-is-not-full-history-encoding',encode((1,2),F(1))==encode((2,3),F(1)))

result={
    'schema':'marici.nima.native-history-memory-realization.v1','status':'pass','checks':checks,
    'source_readings':[list(initial_counts),list(returned_counts)],
    'encoding':'beta=gain*(first_route_steps-second_route_steps); x=u+beta*d; r=-beta*d',
    'd':'the prior twelve-mode AB-minus-BA contrast',
    'gain':'declared readout conversion, not source-selected amplitude or physical unit',
    'decoded_payload':'x+r=u, the prior unperturbed numerical payload',
    'quadratic_budget':'80+(80/3)*beta^2 in inherited model normalization',
    'actual_gain_one_extra_budget':'80/3',
    'diagnostics':readings,
    'source_attachment':'retain the actual full comparison together with this coarse field readout; route counts alone are not faithful',
    'scope':'conditional history-sensitive representation and existing intensity diagnostics; no physical momentum, mass, charge, duration or autonomous preparation derived',
    'fixed_point_boundary':'the original obstruction is unchanged: no nontrivial image if the initial comparison is forced to map to (u,0)',
    'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
       for p in (source,geometry_path,ROOT/'checkers/check_phase_memory_first_moment.py',Path(__file__))},
}
(ROOT/'results/native-history-memory-realization.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact history-to-memory checks, formal source receipt verified')
print('Actual native history swap now has a nonconstant numerical orbit with decoded payload u unchanged.')
print('Nonempty prepared bank and gain are explicit; excess budget at gain one is 80/3, not free excitation.')
print('Active centers:',[r['active_center'] for r in readings])
