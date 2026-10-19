# /// script
# dependencies = ["sympy"]
# ///
"""Check the fresh native endpoint theorem and actual candidate table fields."""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/native-feedback-endpoint-binding-gate.json'
OUT.unlink(missing_ok=True)
formal_path=ROOT/'results/agda-NativeFeedbackEndpointBindingGate.json'
formal=json.loads(formal_path.read_text(encoding='utf-8-sig'))
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
check('fresh-safe-native-endpoint-closure',formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'])
for name in ('NativeFeedbackEndpointBindingGate','NativePromotionConstructorTrace',
             'NativeFeedbackRouteReadout','TriangleComparisonFeedbackRegression'):
    path=ROOT/'agda'/f'{name}.agda'
    check('formal-source-current/'+name,formal['owner_source_inventory_sha256'][path.name]==hashlib.sha256(path.read_bytes()).hexdigest())
with redirect_stdout(io.StringIO()):
    bound=runpy.run_path(str(HERE/'check_geometric_record_endpoint_binding.py'))
m=bound['m']; rows=m['source']
check('decorated-record-operation-binding-current',bound['result']['verification_status']=='pass')

def audit(stage,name):
    check('unique-labels/'+name,len({r.label for r in stage})==len(stage))
    check('unique-endpoint-pairs/'+name,len({(r.source,r.target) for r in stage})==len(stage))
    return {'rows':len(stage),'source_ports':len({r.source for r in stage}),
            'target_ports':len({r.target for r in stage}),
            'endpoint_pairs':len({(r.source,r.target) for r in stage})}
profiles={'input':audit(rows,'input')}
for policy in ('inherited','common'):
    first=m['incoming_promotion'](rows,1,policy)
    final=m['incoming_promotion'](first,2,policy)
    profiles[policy]={'first':audit(first,policy+'/first'),'final':audit(final,policy+'/final')}
check('endpoint-uniqueness-does-not-select-matrix-T9',profiles['inherited']['final']['rows']==32 and profiles['common']['final']['rows']==1)

result={
 'schema':'marici.nima.native-feedback-endpoint-binding-gate.v1','verification_status':'pass','checks':checks,
 'formal_receipt_sha256':hashlib.sha256(formal_path.read_bytes()).hexdigest(),
 'formal_results':{'unrefined_outer_endpoints':'not unique: input and exchanged input have identical presentation endpoints and distinct retained questions',
                   'payload_refinement':'unique: pair each presentation endpoint with the actual decoded native payload',
                   'constructor_unchanged':True},
 'matrix_table_profiles':profiles,
 'binding_comparison':{'matrix_promotions':'fresh assembly source keys make endpoint pairs unique under BOTH policies',
                       'native_feedback_outer_ports':'shared A,C presentations do not give unique endpoints on distinct inputs',
                       'native_feedback_payload_ports':'uniqueness restored, but full-payload fibre separation differs from matrix incoming-port grouping'},
 'intended_T9_status':'not established: endpoint uniqueness eliminates the unrefined native-table interpretation but selects neither matrix policy',
 'objective_complete':False,
 'next_obligation':'Compare retained-payload fibre incidence against the actual record-target family relation; an endpoint adapter must preserve the selected composition domain, not only inject labels.',
 'scope':'No claim that every table must have unique endpoints; the rejection is conditional on that existing table contract.'}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} native endpoint and candidate-table audits')
print('Native outer endpoint binding rejected under uniqueness; decoded-payload refinement proved unique.')
print('Both matrix T9 policies satisfy uniqueness: endpoint uniqueness alone does not select intended T9.')
