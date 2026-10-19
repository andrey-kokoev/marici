# /// script
# dependencies = ["sympy"]
# ///
"""Same resource/dynamics, distinct source readout conventions for fixed2I.

The structural factor2 is audited, not adopted as a physical calibration law.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
from retained_reference_protocol import prepare,algebra,memory
from reference_port_binding import bind
ROOT=HERE.parent
OUT=ROOT/'results/raw-sewing-reference-convention.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    previous=runpy.run_path(str(HERE/'check_reference_port_binding.py'))
flat=previous['flat'];boundary=previous['boundary'];rows=previous['rows']
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def rejects(name,thunk):
    try: thunk()
    except ValueError: check(name,True)
    else: raise AssertionError(name)
check('previous-reference-port-suite-still-passes',previous['result']['verification_status']=='pass')
# Derive the factor from the ACTUAL signed sewing rows and coefficient metric.
mu=memory.transpose(tuple(algebra.sew(e) for e in memory.basis(16)))
C=memory.transpose(tuple(memory.readout(e) for e in memory.basis(16)))
check('raw-port-is-twice-normalized-port',mu==tuple(tuple(2*v for v in row) for row in C))
check('raw-row-Gram-is4I',memory.mm(mu,memory.transpose(mu))==tuple(tuple(F(4*(i==j)) for j in range(4)) for i in range(4)))
check('normalized-row-Gram-isI',memory.mm(C,memory.transpose(C))==memory.basis(4))
check('four-signed-terms-per-raw-coefficient',all(sum(v!=0 for v in row)==4 and all(v in (0,1,-1) for v in row) for row in mu))
# Full-bank equality, not just the scalar reference example.
for i,bank in enumerate(memory.basis(16)):
    protocol=prepare(memory.ZERO4,bank,('full-bank-readout-control',i))
    for mode in ('stored','delayed'):
        normalized=protocol.interrogate(mode)
        raw=protocol.interrogate(mode,'raw-sewing')
        check('full-bank-readout-scaling/'+str((i,mode)),raw['value']==memory.scale(normalized['value'],F(2)))
        check('full-bank-operator-scaling/'+str((i,mode)),raw['operator']==tuple(tuple(2*v for v in row) for row in normalized['operator']))

initial=prepare(algebra.UNIT,memory.ZERO16,('explicit-unit-resource','empty-bank'))
first=initial.advance();second=first.advance();third=second.advance()
normalized=first.interrogate('stored');raw=first.interrogate('stored','raw-sewing')
check('same-unit-state-givesI-and2I',normalized['operator']==algebra.matrix(algebra.UNIT) and raw['operator']==flat['d'])
check('same-history-not-two-preparations',normalized['events']==raw['events'] and normalized['preparation']==raw['preparation'])
check('readout-policy-retained',normalized['readout_policy']=='normalized' and raw['readout_policy']=='raw-sewing')
check('readout-does-not-modify-the-state',first.state.carrier==memory.ZERO4 and memory.budget(first.state.carrier,first.state.record)==1)
check('raw-output-norm-is-not-stored-coefficient-resource',algebra.norm2(raw['value'])==4 and algebra.norm2(first.state.record)==1)
check('raw-port-cannot-be-isometric-carrier-output-with-positive-remainder',algebra.norm2(raw['value'])>memory.budget(first.state.carrier,first.state.record))
check('existing-conservative-state-return-unchanged',(third.state.carrier,third.state.record)==(algebra.UNIT,memory.ZERO16))
check('delayed-raw-reference-keeps-same-lineage',second.interrogate('delayed','raw-sewing')['operator']==raw['operator'])
rejects('normalized-unit-reference-is-not-retuned',lambda:bind(first,'stored',boundary,flat))
raw_ref=bind(first,'stored',boundary,flat,'raw-sewing')
two_unit=prepare(memory.scale(algebra.UNIT,F(2)),memory.ZERO16,('explicit-two-unit-control','empty-bank')).advance()
norm_ref=bind(two_unit,'stored',boundary,flat)
check('equal2I-values-different-resource-and-port-contracts',raw_ref.reference==norm_ref.reference and raw_ref.readout_policy!=norm_ref.readout_policy and raw_ref.input_carrier!=norm_ref.input_carrier)
check('normalized-two-unit-budget-is4',memory.budget(two_unit.state.carrier,two_unit.state.record)==4)
check('bound-reference-does-not-erase-readout-convention',raw_ref.readout_policy=='raw-sewing' and norm_ref.readout_policy=='normalized')
for i,row in enumerate(rows+previous['output'].final):
    check('all-existing-record-attachments-numerically-agree/'+str(i),raw_ref.attach(row,flat['frames'],flat)==norm_ref.attach(row,flat['frames'],flat))
rejects('raw-two-unit-reference-is-not-divided-to-fit',lambda:bind(two_unit,'stored',boundary,flat,'raw-sewing'))
rejects('unknown-readout-policy-rejected',lambda:first.interrogate('stored','fitted-gain'))
rejects('consumed-raw-bank-not-permanent-reference',lambda:bind(third,'stored',boundary,flat,'raw-sewing'))
check('source-parent-recovery-kept',third.recover_initial()==initial.state)

result={
 'schema':'marici.strominger.raw-sewing-reference-convention.v1','verification_status':'pass','checks':checks,
 'source_derived_relation':'mu=2C, mu mu^T=4I, C C^T=I under the supplied orthonormal coefficient metrics',
 'same_unit_execution':{'coefficient_budget':1,'normalized_operator':'I','raw_operator':'2I',
                        'raw_value_norm_squared':4,'dynamics_unchanged':True},
 'two_equal_reference_implementations':[{'resource':'unit','readout':'raw-sewing','budget':1},
                                       {'resource':'2*unit','readout':'normalized','budget':4}],
 'value_and_attachment_agreement':True,'provenance_and_resource_contract_agreement':False,
 'positive_result':'The numerical2I fixture can be matched from a unit resource via an existing source readout, without a newly fitted gain or altered conservative update.',
 'selection_boundary':'No prior source assertion identifies fixed d:A->B with raw sewing rather than a normalized prepared map. Matching2I does not select either role.',
 'physical_calibration_derived':False,'raw_port_is_conservative_output_block':False,
 'reference_policy_changed':False,
 'next_input':'Specify whether the intended reference denotes stored/prepared amplitude or raw comparison response; if raw, account for detector gain and its metric separately from state resource.',
 'inputs_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                 (Path(__file__),HERE/'retained_reference_protocol.py',HERE/'reference_port_binding.py',
                  ROOT.parent/'nima/checkers/check_four_packet_cycle.py',ROOT.parent/'nima/checkers/check_four_packet_record_feedback.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} raw/normalized same-resource reference checks')
print('Existing raw sewing produces2I from a unit record; normalized readout producesI on the same state.')
print('Equal2I port attachments retain distinct resource/readout contracts. No physical calibration or conservative gain is inferred.')
