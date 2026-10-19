"""Exact source-typed reference protocol; calibration remains supplied."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import sys

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
from retained_reference_protocol import prepare,inverse_operator,algebra,memory
ROOT=HERE.parent
NIMA=ROOT.parent/'nima'
OUT=ROOT/'results/retained-reference-protocol.json'
OUT.unlink(missing_ok=True)
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def rejects(name,thunk):
    try: thunk()
    except ValueError: check(name,True)
    else: raise AssertionError(name)
I=algebra.matrix(algebra.UNIT)
for i,(a,b) in enumerate(product(algebra.BASIS,repeat=2)):
    check('actual-source-representation-preserves-product/'+str(i),algebra.matrix(algebra.multiply(a,b))==algebra.mm(algebra.matrix(a),algebra.matrix(b)))
check('source-unit-is-matrix-identity',I==((F(1),F(0)),(F(0),F(1))))
# Existing source representation is an invertible linear value/operator map.
columns=[tuple(v for row in algebra.matrix(e) for v in row) for e in algebra.BASIS]
check('source-representation-rank4',memory.rank(columns)==4)
J=algebra.matrix(algebra.J)
for i,x in enumerate(algebra.BASIS):
    initial=prepare(x,memory.ZERO16,('declared-basis-resource',i))
    first=initial.advance();second=first.advance();third=second.advance()
    stored=first.interrogate('stored');delayed=second.interrogate('delayed')
    check('represented-source-lineage/'+str(i),stored['operator']==algebra.matrix(algebra.rotate(x))==algebra.mm(algebra.mm(J,algebra.matrix(x)),inverse_operator(J)))
    check('delayed-operator-retains-lineage/'+str(i),delayed['operator']==stored['operator'])
    check('interrogation-keeps-preparation-and-events/'+str(i),stored['preparation']==initial.preparation and len(delayed['events'])==2)
    recovered=third.recover_initial()
    check('protocol-recovers-original-resource/'+str(i),(recovered.carrier,recovered.record)==(x,memory.ZERO16))
    check('budget-conserved-through-protocol/'+str(i),memory.budget(third.state.carrier,third.state.record)==memory.budget(initial.state.carrier,initial.state.record))

# The target2I is realized only by EXPLICIT source resource2*unit, not picked
# by the protocol. The fixed-input preparation is part of this conditional map.
resource=memory.scale(algebra.UNIT,F(2))
prepared=prepare(resource,memory.ZERO16,('explicit-two-unit-resource','empty-bank'))
first=prepared.advance();second=first.advance();third=second.advance()
reference=first.interrogate('stored')['operator']
check('explicit-two-unit-resource-produces2I',reference==((F(2),F(0)),(F(0),F(2))))
check('explicit-reference-has-required-strict-return',algebra.mm(reference,inverse_operator(reference))==I and inverse_operator(reference)==((F(1,2),F(0)),(F(0),F(1,2))))
check('resource-coefficient-budget4',memory.budget(prepared.state.carrier,prepared.state.record)==4)
check('represented-reference-Frobenius-norm8',sum(v*v for row in reference for v in row)==8)
check('same-resource-returned-after-three-steps',(third.state.carrier,third.state.record)==(resource,memory.ZERO16))
check('reference-no-longer-in-bank-after-return',third.interrogate('stored')['operator']==((F(0),F(0)),(F(0),F(0))))
check('history-not-erased-by-numerical-return',third.events!=prepared.events and third.recover_initial()==prepared.state)
# Scale and singular controls prevent mistaking a conditional source map for
# universal calibration or an always-invertible reference preparation.
for factor in (F(0),F(1),F(3)):
    protocol=prepare(memory.scale(algebra.UNIT,factor),memory.ZERO16,('scale-control',str(factor))).advance()
    check('protocol-does-not-select-amplitude/'+str(factor),protocol.interrogate('stored')['operator']==((factor,F(0)),(F(0),factor)))
singular=prepare((F(1),F(1),F(0),F(0)),memory.ZERO16,('noninvertible-control',)).advance().interrogate('stored')['operator']
rejects('singular-record-does-not-supply-inverse',lambda:inverse_operator(singular))
rejects('preparation-needs-explicit-provenance',lambda:prepare(resource,memory.ZERO16,()))
rejects('interrogation-needs-declared-port',lambda:first.interrogate('unspecified'))
rejects('retained-depth-limit-kept',lambda:third.advance())
# The pinned software reference matches this conditional representation value,
# not the physical type A->B until boundary identifications are supplied.
contract=json.loads((NIMA/'contracts/T9-exact-domain-software.v1.json').read_text(encoding='utf-8'))
check('software-physical-boundary-not-promoted',not contract['physical_generator_identified'] and not contract['source_calibration_derived'])
result={
 'schema':'marici.strominger.retained-reference-protocol.v1','verification_status':'pass','checks':checks,
 'protocol':'explicit input carrier/bank -> existing conservative exchange -> retained stored/delayed readout -> existing Cl(2,0)2x2 operator representation -> recover supplied input resource',
 'source_adapter':'matrix(s,q,p,z)=((s+q,p+z),(p-z,s-q)), copied by REUSING actual source function; product-preserving and rank4.',
 'conditional_target_preparation':{'resource':'2*Clifford unit','bank':'explicitly empty','record_operator':'2I',
                                   'coefficient_budget':4,'matrix_Frobenius_norm_squared':8,
                                   'third_step_returns_same_resource':True},
 'source_type':'Memory value in Cl(2,0) represented as End(R^2).',
 'target_type_boundary':'Identifying End(R^2) with comparison maps A->B still requires declared boundary identifications/port attachments.',
 'record_lifecycle':'Stored after one exchange, delayed after two, transferred back after three; parent history retained. No permanent reference catalyst is asserted.',
 'calibration_derived':False,'physical_protocol_realized':False,'physical_T9_identified':False,
 'remaining_inputs':['Preparation and units of the explicit two-unit carrier resource',
                     'Physical realization/selection of supplied C,R,L and event clock',
                     'Boundary and record-port identifications to the pinned T9 fixture',
                     'Detector/readout and reset/reuse/degradation semantics'],
 'source_owner_receipts_overwritten':False,
 'inputs_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                 (Path(__file__),HERE/'retained_reference_protocol.py',NIMA/'checkers/check_four_packet_cycle.py',NIMA/'checkers/check_four_packet_record_feedback.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} retained source-typed reference protocol checks')
print('Existing Clifford representation maps memory references to operators; explicit2*unit resource gives2I.')
print('Scale, boundary identification and physical apparatus remain supplied; numerical return retains its history.')
