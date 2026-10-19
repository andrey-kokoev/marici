# /// script
# dependencies = ["sympy"]
# ///
"""End-to-end conditional source protocol -> boundaries -> pinned T9 ports."""
from contextlib import redirect_stdout
from dataclasses import replace
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
from retained_reference_protocol import prepare,algebra,memory
from reference_port_binding import BoundaryIdentification,bind
ROOT=HERE.parent
NIMA=ROOT.parent/'nima'
if str(NIMA/'checkers') not in sys.path: sys.path.insert(0,str(NIMA/'checkers'))
from retained_rung_transport import T9
OUT=ROOT/'results/reference-port-binding.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    software=runpy.run_path(str(NIMA/'checkers/check_pinned_T9_software_contract.py'))
    protocol_audit=runpy.run_path(str(HERE/'check_retained_reference_protocol.py'))
flat=software['flat']; m=software['m']; rows=m['source']
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def rejects(name,thunk):
    try: thunk()
    except ValueError: check(name,True)
    else: raise AssertionError(name)
check('pinned-software-checks-pass',software['result']['verification_status']=='pass')
check('source-protocol-checks-pass',protocol_audit['result']['verification_status']=='pass')
I=algebra.matrix(algebra.UNIT)
boundary=BoundaryIdentification('A','B','source-Clifford-R2',I,I,
                                ('declared-comparison-boundary-identifications',))
resource=memory.scale(algebra.UNIT,F(2))
initial=prepare(resource,memory.ZERO16,('explicit-two-unit-resource','empty-bank'))
first=initial.advance(); second=first.advance();third=second.advance()
ref=bind(first,'stored',boundary,flat)
delayed=bind(second,'delayed',boundary,flat)
check('reference-and-inverse-match-without-rescaling',ref.reference==flat['d'] and ref.inverse==flat['r'])
check('boundary-and-source-history-retained',ref.boundary==boundary and ref.input_carrier==resource and ref.input_bank==memory.ZERO16 and ref.events==first.events)
check('same-reference-different-lifecycle-retained',ref.reference==delayed.reference and (ref.depth,ref.readout_mode,ref.events)!=(delayed.depth,delayed.readout_mode,delayed.events))
output=T9(rows,m)
for index,row in enumerate(rows+output.final):
    for frames in (flat['frames'],flat['changed']):
        actual,reference,ret=ref.attach(row,frames,flat)
        check('existing-port-attachment-identical/'+str((index,frames is flat['changed'])),(actual,reference,ret)==flat['realization'](row,frames))
        check('comparison-decodes-unchanged/'+str((index,frames is flat['changed'])),ref.decode(actual,row.source,row.target,frames,flat)==row.value)
        check('port-reference-decodes-to-source-bound-reference/'+str((index,frames is flat['changed'])),ref.decode(reference,row.source,row.target,frames,flat)==ref.reference)
count=0
for family in m['indexed'](rows,'target').values():
    for a in family:
        for b in family:
            av,_,_=ref.attach(a,flat['frames'],flat)
            bv,_,br=ref.attach(b,flat['frames'],flat)
            composed=flat['chain'](bv,br,av)
            check('all-original-compositions-with-source-bound-reference/'+str((a.label,b.label)),ref.decode(composed,a.source,a.target,flat['frames'],flat)==flat['chain'](b.value,ref.inverse,a.value))
            count+=1
check('977-original-pairs-checked',count==977)
check('pinned-T9-J4-unchanged',output.observe(m)['J4']==m['read_at_four'](output.target_view(m)))
rejects('wrong-resource-not-rescaled',lambda:bind(prepare(algebra.UNIT,memory.ZERO16,('one-unit-control',)).advance(),'stored',boundary,flat))
rejects('consumed-bank-reference-not-fabricated',lambda:bind(third,'stored',boundary,flat))
rejects('boundary-change-not-hidden-by-matching-coordinates',lambda:bind(first,'stored',replace(boundary,target_to_operator=((F(2),F(0)),(F(0),F(1)))),flat))
rejects('boundary-provenance-required',lambda:bind(first,'stored',replace(boundary,provenance=()),flat))
rejects('wrong-object-roles-rejected',lambda:bind(first,'stored',replace(boundary,source='carrier-port'),flat))
# Passive change of source operator-space coordinates: scalar2I stays2I;
# transform BOTH boundary identifications, not the reference scale.
G=((F(1),F(1)),(F(0),F(1)))
changed_boundary=replace(boundary,source_to_operator=G,target_to_operator=G,
                         provenance=('declared-passive-operator-space-coordinate-change',))
ref2=bind(first,'stored',changed_boundary,flat)
check('passive-boundary-coordinate-change-not-normalization-knob',ref2.reference==ref.reference)
result={
 'schema':'marici.strominger.reference-port-binding.v1','verification_status':'pass','checks':checks,
 'positive_chain':'Explicit source resource -> conservative retained memory -> existing algebraic operator representation -> declared A,B identifications -> existing flat record attachments -> pinned exact-domain T9.',
 'reference':'2I from explicit2*unit source; inverseI/2; no mismatch rescaling',
 'original_records':137,'selected_final_records':32,'original_compositions_checked':977,
 'source_history_and_boundary_provenance_retained':True,
 'software_binding_complete':True,'conditional_reference_binding_complete':True,
 'physical_source_calibration_derived':False,'physical_generator_identified':False,
 'remaining_supplied':['two-unit preparation/units','physical C,R,L realization and event clock',
                      'A,B/operator-space identifications','flat port frames/physical reference connection',
                      'detector/back-action and resource reuse/reset/degradation'],
 'lifecycle':'Stored and delayed snapshots have equal operators but different retained histories. Third-step active-bank depletion is not ignored.',
 'scope':'Exact mathematical protocol binding, not an empirical apparatus or source-derived physical normalization.',
 'inputs_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                 (Path(__file__),HERE/'reference_port_binding.py',HERE/'retained_reference_protocol.py',NIMA/'contracts/T9-exact-domain-software.v1.json')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} retained source-reference/port/T9 binding checks')
print('Source-prepared2I binds without rescaling to all137 leaf ports,32 final families and977 compositions.')
print('Boundary identities, resource scale, flat physical transport and apparatus remain supplied.')
