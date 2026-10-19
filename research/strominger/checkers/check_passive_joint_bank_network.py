# /// script
# dependencies = ["sympy"]
# ///
"""Exact ideal mode-network realization, not empirical calibration."""
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import passive_joint_bank_network as plant
import joint_bank_extraction as joint
from clifford_comparison_bank import algebra,memory
ROOT=HERE.parent
OUT=ROOT/'results/passive-joint-bank-network.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    previous=runpy.run_path(str(HERE/'check_joint_bank_extraction.py'))
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
check('previous-full-state-extraction-suite-passes',previous['result']['verification_status']=='pass')
check('four-disjoint64-mode-source-supports',list(map(len,plant.GROUPS))==[64]*4 and sorted(index for group in plant.GROUPS for index,_ in group)==list(range(256)))
for row,group in enumerate(plant.GROUPS):
    check('source-derived-router-coefficients/'+str(row),all(joint.PRODUCT_COLUMNS[index][row]/2==F(sign,8) for index,sign in group))
# Every stage consists of disjoint normalized H2 couplers. Track sqrt(2)
# analytically; after6 stages the combined coefficients are rational1/8.
for stage,pairs in enumerate(plant.router_layers()):
    check('32-independent-balanced-couplers-per-layer/'+str(stage),len(pairs)==32 and sorted(index for pair in pairs for index in pair)==list(range(64)))
for a,b in ((F(1),F(0)),(F(2),F(-3)),(F(1,3),F(2,7))):
    check('balanced-coupler-norm-identity/'+str((a,b)),(a+b)**2+(a-b)**2==2*(a*a+b*b))

for index,e in enumerate(memory.basis(256)):
    routed=plant.route(e)
    check('exact-source-supermode-extraction/'+str(index),routed[:4]==joint.readout(e))
    check('complete-router-inverse/'+str(index),plant.unroute(routed)==e)
    check('complete-router-budget/'+str(index),algebra.norm2(routed)==algebra.norm2(e))
for index,v in enumerate(memory.basis(260)):
    state=(v[:4],v[4:])
    actual=plant.extract(*state)
    expected=joint.exchange(*state)
    check('all260-mode-operator-columns-identical/'+str(index),actual==expected)
    check('physical-port-proposal-keeps-full-bank/'+str(index),len(actual[0])==4 and len(actual[1])==256)
# A populated hidden direction is retained, not treated as unused vacuum.
e=memory.basis(256)[0]
k=memory.sub(e,joint.lift(joint.readout(e)))
check('hidden-kernel-is-nonzero',algebra.norm2(k)>0)
check('hidden-kernel-survives-routing-and-swap',plant.extract(memory.ZERO4,k)==(memory.ZERO4,k))
# Hadamard-only routing without required source signs is a hostile, not an
# equivalent convention when the record-port query stays fixed.
row,group=next((row,group) for row,group in enumerate(plant.GROUPS) if any(sign<0 for _,sign in group))
index=next(index for index,sign in group if sign<0)
e=memory.basis(256)[index]
correct=plant.route(e)[row]
incorrect=plant.hadamard64(tuple(e[index] for index,_ in group))[0]
check('omitting-sign-phase-changes-selected-supermode',correct==-incorrect and correct!=0)
negative=sum(sign<0 for group in plant.GROUPS for _,sign in group)
result={
 'schema':'marici.strominger.passive-joint-bank-network.v1','verification_status':'pass','checks':checks,
 'ideal_network':{'modes':260,'router_blocks':4,'modes_per_router':64,'balanced_layers_per_router':6,
                  'balanced_couplers_per_router_pass':768,'router_passes':2,
                  'balanced_couplers_total':1536,'carrier_bank_swaps':4,
                  'source_sign_phases_per_pass':negative,'source_sign_phases_total':2*negative},
 'source_routing_groups':plant.GROUPS,'balanced_layer_pairs':plant.router_layers(),
 'exact_operator_factorization':'E=diag(I4,Q^T) S diag(I4,Q); Q first4 rows equal D, S swaps those4 bank outputs with carrier.',
 'full_state_operator_equal':True,'kernel_modes_retained':252,
 'primitive_controls':'Ideal normalized balanced H2 couplers, required0/pi sign phases, lossless swaps, full coherent routing and inverse; wiring permutations retained.',
 'preparation_supplied':True,'calibration_measured':False,'source_physical_admission_proved':False,
 'not_claimed':['No laboratory realization','No source-generated joint input','No energy calibration from coefficient norm',
                'No reset of252 unused modes','No transfer of an existing4-port certificate to this260-mode network'],
 'next_apparatus_inputs':['Joint-input preparation and all260 port normalizations',
                         'Independent full-port router/swap amplitude and phase calibration',
                         'Storage/delay/event timing and validity intervals',
                         'Detector convention for matrix(4*carrier) and environment/reset policy'],
 'inputs_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                 (Path(__file__),HERE/'passive_joint_bank_network.py',HERE/'joint_bank_extraction.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} ideal passive full-state network checks')
print('Four signed64-mode routers, four swaps and inverse routing exactly realize the260-mode extraction.')
print('1536 ideal balanced couplers; input preparation, hardware calibration and physical source admission remain open.')
