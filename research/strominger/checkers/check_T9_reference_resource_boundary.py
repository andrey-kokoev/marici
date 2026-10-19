"""Audit the prior memory-generated reference against pinned T9's physical gap.

No new reference preparation, mixer, calibration or matrix/value type adapter
is introduced. Uses exact prior dynamics and writes a consumer-local receipt.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
NIMA=ROOT.parent/'nima'
HERE=NIMA/'checkers'
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import check_retained_memory_reference as memory
import check_four_packet_record_feedback as feedback

OUT=ROOT/'results/T9-reference-resource-boundary.json'
OUT.unlink(missing_ok=True)
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
# Exercise the existing exact source functions without invoking main() or
# overwriting the source owner's previous result receipt.
zero=(memory.Z4,memory.Z16)
state=zero
for depth in range(memory.MAX_DEPTH):
    state,delta=memory.compare_step(*state)
    check('zero-source-cannot-prepare-nonzero-reference/'+str(depth),state==zero and delta==memory.Z4)

lineage_columns=[]
for index,x in enumerate(feedback.basis(4)):
    initial=(x,memory.Z16)
    first,_=memory.compare_step(*initial)
    second,_=memory.compare_step(*first)
    third,_=memory.compare_step(*second)
    stored=feedback.readout(first[1])
    lineage_columns.append(stored)
    check('reference-created-from-initial-carrier/'+str(index),stored==memory.rotate(x))
    check('delayed-port-keeps-same-ancestry/'+str(index),feedback.readout(feedback.left_rotate(second[1]))==stored)
    check('reference-resource-moves-into-bank/'+str(index),first[0]==memory.Z4 and feedback.budget(*first)==feedback.budget(*initial))
    check('empty-bank-source-recovers-at-third-step/'+str(index),third==(memory.rotate(x),memory.Z16))
    check('all-three-parent-steps-invert/'+str(index),feedback.inverse_cycle(*third)==second and feedback.inverse_cycle(*second)==first and feedback.inverse_cycle(*first)==initial)
    for factor in (F(-2),F(1,2),F(3,2),F(2)):
        scaled=(feedback.scale(x,factor),memory.Z16)
        result,_=memory.compare_step(*scaled)
        check('source-scale-inherits-reference-scale/'+str((index,factor)),feedback.readout(result[1])==feedback.scale(stored,factor))
        check('coefficient-resource-scales-quadratically/'+str((index,factor)),feedback.budget(*result)==factor**2*feedback.budget(*initial))
check('memory-reference-map-is-rank4-not-fixed-value-selector',feedback.rank(lineage_columns)==4)
# General two-step ancestry on the full20-dimensional state space.
for index,v in enumerate(feedback.basis(20)):
    initial=(v[:4],v[4:])
    first,_=memory.compare_step(*initial)
    second,_=memory.compare_step(*first)
    check('full-state-first-lineage/'+str(index),feedback.readout(first[1])==memory.rotate(initial[0]))
    check('full-state-delayed-lineage/'+str(index),feedback.readout(feedback.left_rotate(second[1]))==memory.rotate(initial[0]))

contract_path=NIMA/'contracts/T9-exact-domain-software.v1.json'
contract=json.loads(contract_path.read_text(encoding='utf-8'))
check('software-contract-keeps-physical-boundary',not contract['physical_generator_identified'] and not contract['source_calibration_derived'])
result={
 'schema':'marici.strominger.T9-reference-resource-boundary.v1','verification_status':'pass','checks':checks,
 'existing_positive_source':'Prior conservative memory exchange creates and retains comparison VALUES from past carrier data, with exact inverse and budget lineage.',
 'preparation_controls':{'zero_resource_nonzero_reference':False,'reference_map_rank':4,
                         'reference_scale_selected':False,'reference_scale_inherited_from_source':True},
 'type_boundary':{'memory_reference':'4-component readable bank VALUE under supplied C,R,L',
                  'T9_reference':'fixed2x2 degree-zero comparison MAP d:A->B, plus reference attachments at carrier ports'},
 'missing_adapter':'A source-selected typed map relating the memory record/value task to the fixed direct-reference map and its port transports, with preparation and observation scope.',
 'not_inferred':['Memory data is not the certified target of the current comparison.',
                 'Conserved coefficient budget is not calibrated laboratory energy.',
                 'Rank4 reachability is not autonomous selection of2I or any prescribed reference.',
                 'Source initialization, C/R/L mixers and clock remain supplied.'],
 'source_owner_receipts_overwritten':False,
 'physical_T9_identified':False,
 'next_input':'Bind the declared memory value to a specified reference-port protocol; establish the source resource and scale rather than choose a coordinate reshape to manufacture2I.',
 'inputs_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                 (Path(__file__),HERE/'check_retained_memory_reference.py',HERE/'check_four_packet_record_feedback.py',HERE/'check_four_packet_cycle.py',contract_path)}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} prior-memory/T9 reference-resource checks')
print('Past carrier values generate memory references; zero input stays zero and source scaling survives exactly.')
print('This does not prepare the fixed T9 reference map or select physical calibration.')
