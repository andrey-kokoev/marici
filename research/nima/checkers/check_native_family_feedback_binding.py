# /// script
# dependencies = ["sympy"]
# ///
"""Validate actual family inputs to the freshly proved native family adapter.

No Python substitute for native run is executed: its recovery/readout contract
is proved in Agda. This audit checks actual fixture family/port/measure fields.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/native-family-feedback-binding.json'
OUT.unlink(missing_ok=True)
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
receipt=ROOT/'results/agda-NativeFamilyFeedbackBinding.json'
formal=json.loads(receipt.read_text(encoding='utf-8-sig'))
check('fresh-safe-family-adapter-closure',formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'])
for name in ('NativeFamilyFeedbackBinding','TriangleComparisonFeedbackRegression','NativeNormalizationRouteCompiler'):
    path=ROOT/'agda'/f'{name}.agda'
    check('formal-source-current/'+name,formal['owner_source_inventory_sha256'][path.name]==hashlib.sha256(path.read_bytes()).hexdigest())
with redirect_stdout(io.StringIO()):
    binding=runpy.run_path(str(HERE/'check_geometric_record_endpoint_binding.py'))
m=binding['m']; flat=binding['flat']; rows=m['source']
check('typed-record-response-binding-fresh',binding['result']['verification_status']=='pass')
profiles={}; packets={}
for policy in ('inherited','common'):
    first=m['incoming_promotion'](rows,1,policy)
    final=m['incoming_promotion'](first,2,policy)
    packets[policy]=[]
    for depth,stage in enumerate((first,final),1):
        stage_packets=[]
        for family in stage:
            grouping_key=family.members[0].target
            check('family-belongs/'+str((policy,depth,family.label)),all(member.target==grouping_key for member in family.members))
            check('family-measure/'+str((policy,depth,family.label)),family.mass==sum(member.mass for member in family.members)>0)
            check('family-weighted-response/'+str((policy,depth,family.label)),family.value==m['mean'](family.members))
            generated_target=('retained-key',depth,grouping_key) if policy=='inherited' else ('common-target',depth)
            check('grouping-vs-successor-key/'+str((policy,depth,family.label)),family.target==generated_target and grouping_key!=generated_target)
            # Reuse existing flat attachment's exact promotion law.
            target=flat['frames'][family.target]; terms=[]
            for member in family.members:
                actual,_,ret=flat['realization'](member,flat['frames'])
                transport=flat['chain'](target,flat['inverse'](flat['frames'][member.target]))
                terms.append(flat['scale'](F(member.mass,family.mass),flat['chain'](transport,actual,ret,flat['inverse'](transport))))
            typed=flat['chain'](flat['total'](terms),target,flat['inverse'](flat['frames'][family.source]))
            check('native-supplied-family-reader-typed/'+str((policy,depth,family.label)),typed==flat['realization'](family,flat['frames'])[0])
            stage_packets.append({'label':family.label,'grouping_key':grouping_key,'generated_source':family.source,
                                  'generated_target':family.target,'mass':family.mass,
                                  'members':[member.label for member in family.members]})
        packets[policy].append(stage_packets)
    check('complete-family-leaf-retention/'+policy,m['leaves'](final)==rows)
    check('family-reader-J4/'+policy,m['read_at_four'](m['indexed'](final,'target'))==m['read_at_four'](m['indexed'](rows,'target')))
    profiles[policy]={'first_family_count':len(first),'final_family_count':len(final),
                      'second_member_counts':[len(f.members) for f in final]}
check('native-adapter-does-not-select-successor-policy',profiles['inherited']['second_member_counts']==[1]*32 and profiles['common']['second_member_counts']==[32])
# Feedback consumes a family; it does not perform the incoming fibre former.
# Under inherited keys round2 is singleton wrapping; under common keys it is
# averaging32 families. These are different supplied inputs to the same adapter.
check('constructor-factorization-witness',len(packets['inherited'][1])!=len(packets['common'][1]))
result={
 'schema':'marici.nima.native-family-feedback-binding.v1','verification_status':'pass','checks':checks,
 'formal_receipt_sha256':hashlib.sha256(receipt.read_bytes()).hexdigest(),
 'family_profiles':profiles,'family_packets':packets,
 'positive_binding':'Existing Feedback.run accepts atomic target-keyed families with no tetrahedral faces; actual decode recovers members, key and every supplied family readout.',
 'constructor_factorization':'rows --incoming fibres and supplied successor policy--> families --explicit empty-route embedding--> native Compared --actual Feedback.run--> next Compared',
 'grouping_port_distinction':'The old target key defines membership; the supplied successor map defines the generated next target. They are not equal in either actual policy.',
 'measure_status':'Original member masses and weighted matrix means checked and inherited; not selected by native feedback.',
 'intended_T9_status':'No selection: native run is a faithful wrapper for either already-chosen family former, not a derivation of that former.',
 'objective_complete':False,
 'next_obligation':'Determine which source contract fixes the successor-key map and aggregation/member measure; inspect original constructor specifications rather than infer it from native recoverability.',
 'scope':'Concrete generic Agda adapter plus exact finite inputs. No formal rational-matrix instance or physical constructor identification is claimed.'}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} native-family/typed-promotion checks')
print('Actual keyed families fit native feedback; decoded family reader is formally preserved.')
print('Grouping keys and generated next ports are distinct; both successor policies remain possible.')
