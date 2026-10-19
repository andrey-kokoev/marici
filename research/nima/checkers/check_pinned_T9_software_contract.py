# /// script
# dependencies = ["sympy"]
# ///
"""End-to-end verification of the operator-selected local SOFTWARE contract."""
from contextlib import redirect_stdout
from dataclasses import replace
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
from retained_rung_transport import CONTRACT_ID, transport, T9, T8, T7
from record_context_transport import ContextTransport
from branch_response_summary import recover
ROOT=HERE.parent
OUT=ROOT/'results/pinned-T9-software-contract.json'
OUT.unlink(missing_ok=True)
contract_path=ROOT/'contracts/T9-exact-domain-software.v1.json'
contract=json.loads(contract_path.read_text(encoding='utf-8'))
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def rejects(name,thunk):
    try: thunk()
    except ValueError: check(name,True)
    else: raise AssertionError(name)
check('pinned-contract-identity',contract['contract_id']==CONTRACT_ID)
check('software-selection-not-physical-identification',not contract['physical_generator_identified'] and not contract['source_calibration_derived'])
check('pinned-endpoint-role',contract['endpoint_role']=='carrier-index columns with retained original label/source/target fields')
formal_receipts={}
for name in ('SuccessorContextReflection','NativeFamilyFeedbackBinding'):
    receipt=ROOT/'results'/f'agda-{name}.json'
    formal=json.loads(receipt.read_text(encoding='utf-8-sig'))
    check('fresh-safe-proof/'+name,formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'])
    source=ROOT/'agda'/f'{name}.agda'
    check('proof-source-current/'+name,formal['owner_source_inventory_sha256'][source.name]==hashlib.sha256(source.read_bytes()).hexdigest())
    formal_receipts[name]=hashlib.sha256(receipt.read_bytes()).hexdigest()
# Run both prior operation/connector and observer controls, without changing
# their historical conditional-selection claims.
with redirect_stdout(io.StringIO()):
    contexts=runpy.run_path(str(HERE/'check_explicit_context_transport.py'))
    branches=runpy.run_path(str(HERE/'check_branch_response_summary.py'))
m=contexts['m']; rows=m['source']; flat=contexts['flat']
check('existing-explicit-context-checks-pass',contexts['result_json']['verification_status']=='pass')
check('existing-branch-summary-checks-pass',branches['result']['verification_status']=='pass')
output=T9(rows,m); observed=output.observe(m)
check('public-T9-entrypoint',output==transport(rows,m))
expected=contract['fixture_expectations']
check('137-original-records',len(output.original)==expected['original_records'])
check('32-final-families',len(output.final)==expected['final_families'])
check('original-labelled-endpoints-and-values-recover',m['leaves'](output.final)==rows)
check('original-member-masses',sum(row.mass for row in output.final)==137)
check('original-branch-masses',list(observed['masses'])==expected['branch_masses'])
left11=m['indexed'](rows,'source'); left10=m['indexed'](m['unindex'](left11),'target')
check('upper-square',T8(left11,m)==output.source_view(m))
check('lower-square',T7(left10,m)==m['indexed'](m['unindex'](T8(left11,m)),'target'))
check('same-complete-rung4-route',T7(left10,m)==output.target_view(m))
check('unchanged-fixed-reference-J4',observed['J4']==m['read_at_four'](output.target_view(m))==m['read_at_four'](left10))
check('outer-branch-readout-recovery',recover(observed['J4'],observed['contrast'],observed['masses'],m['m'])==observed['branch_residuals'])
# Domain equality, not just support cardinality.
old={(a.label,b.label) for a in rows for b in rows if a.target==b.target}
new=set()
for family in output.final:
    leaves=m['leaves']((family,))
    new.update((a.label,b.label) for a in leaves for b in leaves)
check('exact-original-domain-preserved-and-reflected',new==old and len(new)==expected['admitted_original_leaf_pairs'])
ctx=ContextTransport(flat)
a=rows[0]; b=next(row for row in rows if row.target!=a.target)
rejects('transport-does-not-admit-cross-context',lambda:ctx.compose(a,b))
rejects('duplicate-label-source-rejected',lambda:transport(rows+(rows[0],),m))
rejects('common-assembly-endpoint-role-rejected',lambda:transport(tuple(replace(row,source=('assembly','A'),target=('assembly','B')) for row in rows),m))
rejects('promoted-input-role-rejected',lambda:transport(output.final,m))
rejects('nonpositive-member-mass-rejected',lambda:transport((replace(rows[0],mass=0),)+rows[1:],m))
# Guard against a corrupted supplied constructor even though inherited is
# pinned: provenance recovery alone cannot hide changed response coordinates.
corrupt=dict(m)
def bad_promotion(input_rows,depth,policy):
    output_rows=list(m['incoming_promotion'](input_rows,depth,policy))
    if depth==2:
        output_rows[0]=replace(output_rows[0],value=m['m']['add'](output_rows[0].value,m['m']['H']))
    return tuple(output_rows)
corrupt['incoming_promotion']=bad_promotion
rejects('corrupted-response-constructor-rejected',lambda:transport(rows,corrupt))
result={
 'schema':'marici.nima.pinned-T9-software-contract.v1','verification_status':'pass','checks':checks,
 'contract_id':CONTRACT_ID,'contract_sha256':hashlib.sha256(contract_path.read_bytes()).hexdigest(),
 'selection_status':'operator-confirmed SOFTWARE exact-domain policy',
 'software_endpoint_and_T9_binding_complete':True,
 'physical_generator_identified':False,'source_calibration_derived':False,
 'end_to_end':{'original_rows':137,'final_families':32,'exact_admitted_leaf_pairs':977,
               'both_squares':True,'original_J4_unchanged':True,'outer_branch_readout':True,
               'context_creation_separate':True},
 'formal_receipts_sha256':formal_receipts,
 'remaining_physical_obligations':['Source selection of the supplied numerical response and reference attachments',
                                  'Instrument/clock/preparation/readout realization',
                                  'Any intended context creation requires separately sourced connector admission'],
 'inputs_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'retained_rung_transport.py',HERE/'record_context_transport.py',HERE/'branch_response_summary.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} consolidated pinned-T9 software checks')
print('Software contract bound:137->32->32; exact977-pair domain, original J4, outer branch response.')
print('Connector context creation remains separate. Physical generator/calibration identification is not claimed.')
