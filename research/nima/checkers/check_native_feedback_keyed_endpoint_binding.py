# /// script
# dependencies = ["sympy"]
# ///
"""Exact context-domain audit of the asymmetric native endpoint interface.

The finite analogue uses existing decorated records, not an asserted encoding
of matrix records as native Compared values. The native theorem is universal
conditional on the key and any such encoding.
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/native-feedback-keyed-endpoint-binding.json'
OUT.unlink(missing_ok=True)
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
receipt=ROOT/'results/agda-NativeFeedbackKeyedEndpointBinding.json'
formal=json.loads(receipt.read_text(encoding='utf-8-sig'))
check('fresh-safe-keyed-endpoint-closure',formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'])
for name in ('NativeFeedbackKeyedEndpointBinding','NativeFeedbackEndpointBindingGate','TriangleComparisonFeedbackRegression'):
    path=ROOT/'agda'/f'{name}.agda'
    check('formal-source-current/'+name,formal['owner_source_inventory_sha256'][path.name]==hashlib.sha256(path.read_bytes()).hexdigest())
with redirect_stdout(io.StringIO()):
    gate=runpy.run_path(str(HERE/'check_native_feedback_endpoint_binding_gate.py'))
bound=gate['bound']; m=bound['m']; rows=m['source']
check('prior-endpoint-and-operation-gates-current',gate['result']['verification_status']=='pass')
labels={r.label for r in rows}
original={(a.label,b.label) for a,b in product(rows,repeat=2) if a.target==b.target}
full=set(product(labels,repeat=2)); diagonal={(label,label) for label in labels}
key_functions={'original-target':lambda row:row.target,'constant':lambda row:('common',),
               'payload-identity':lambda row:row.label}
expected={'original-target':original,'constant':full,'payload-identity':diagonal}
profiles={}
for name,key in key_functions.items():
    # This is the finite decorated analogue of source=(A,payload),
    # target=(C,key(payload)). Label indexes the entire retained packet.
    ports={row.label:(('payload-source',row.label),('keyed-target',key(row))) for row in rows}
    check('unique-asymmetric-endpoint-pairs/'+name,len(set(ports.values()))==137)
    supported={(a.label,b.label) for a,b in product(rows,repeat=2) if ports[a.label][1]==ports[b.label][1]}
    check('exact-common-target-relation/'+name,supported==expected[name])
    check('source-payload-recovery/'+name,{port[0][1] for port in ports.values()}==labels)
    # Keeping ORIGINAL source fields is a stronger, different contract.
    old_source_pairs={(row.source,key(row)) for row in rows}
    profiles[name]={'retained_rows':137,'target_fibres':len({key(row) for row in rows}),
                    'supported_pairs':len(supported),'original_source_endpoint_pairs':len(old_source_pairs),
                    'original_source_uniqueness':len(old_source_pairs)==137}
check('relation-hierarchy',diagonal < original < full)
check('exact-context-profile',[(profiles[k]['target_fibres'],profiles[k]['supported_pairs']) for k in key_functions]==[(32,977),(1,18769),(137,137)])
check('original-source-contract-excludes-constant-key',not profiles['constant']['original_source_uniqueness'])
check('original-source-contract-allows-inherited-key',profiles['original-target']['original_source_uniqueness'])

# Relate keys to ACTUAL final promoted membership, not a made-up partition.
for policy,keyname in (('inherited','original-target'),('common','constant')):
    first=m['incoming_promotion'](rows,1,policy)
    final=m['incoming_promotion'](first,2,policy)
    actual=set()
    for family in final:
        leaves=m['leaves']((family,))
        actual.update((a.label,b.label) for a,b in product(leaves,repeat=2))
    check('native-key-analogue-matches-promoted-context/'+policy,actual==expected[keyname])
    check('pointwise-lift-is-not-family-promotion/'+policy,len(final)!=137)

# Concrete false-positive and false-negative endpoint-binding witnesses.
a=rows[0]
b=next(row for row in rows if row.label!=a.label and row.target==a.target)
c=next(row for row in rows if row.target!=a.target)
check('payload-key-loses-admitted-nondiagonal-context',(a.label,b.label) in original-diagonal)
check('constant-key-adds-unadmitted-cross-target-context',(a.label,c.label) in full-original)

result={
 'schema':'marici.nima.native-feedback-keyed-endpoint-binding.v1','verification_status':'pass',
 'checks':checks,'formal_receipt_sha256':hashlib.sha256(receipt.read_bytes()).hexdigest(),
 'profiles':profiles,
 'witnesses':{'lost_by_payload_key':{'labels':[a.label,b.label],'target':a.target},
              'added_by_constant_key':{'labels':[a.label,c.label],'targets':[a.target,c.target]}},
 'native_formal_contract':'Full decoded source payload guarantees uniqueness; keyed decoded target preserves and reflects exactly key equality.',
 'binding_status':'Composition-domain-preserving endpoint refinement is available CONDITIONAL on a native payload encoding and declared context key.',
 'constructor_distinction':'Pointwise native run retains one output per input; matrix T9 aggregates137 inputs into32 or1 family rows. Matching context does not identify these constructors.',
 'source_preservation_note':'If original source columns are additionally required unchanged, the constant-key137-row lift violates uniqueness. The existing T9s use fresh assembly sources, so this additional requirement cannot be assumed.',
 'intended_T9_status':'Still unselected: the generic keyed theorem realizes either context policy.',
 'objective_complete':False,
 'next_obligation':'Bind at FAMILY level, with a specified member measure and decoded field, rather than identify pointwise run with mean aggregation.',
 'scope':'No native encoding of137 matrix records, physical task selection or new connector authorization is asserted.'}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} keyed native/record composition-domain checks')
print('Asymmetric endpoint refinement preserves any declared key relation without losing uniqueness.')
print('Original-target key matches977 pairs; constant key matches18769; pointwise feedback still is not family aggregation.')
