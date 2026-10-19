"""Reference transition cocycles, target retention obligations and naturality."""
from pathlib import Path
from dataclasses import replace
import contextlib,io,json,hashlib
from field_refibration import EDGES,encode
from reconstruction_aware_tower import (field_rows,observe_field_rows,make_packet,horizontal,vertical,
    raw_rows,operator_packet,verify,data_from_leaves)
from field_reference_transitions import change_reference,verify_change,compose,operator_core
ROOT=Path(__file__).resolve().parents[3];log=io.StringIO()
with contextlib.redirect_stdout(log):import check_reconstruction_aware_tower as baseline
previous=baseline.previous;A,Z,O=baseline.A,baseline.Z,baseline.O
context,owner,generator=baseline.context,baseline.owner,baseline.generator
source_reference=(0,2);deficient_reference=(0,1);third_reference=(2,3)
field=previous.blind

def prepare(field,reference,policy):
    rows=observe_field_rows(field_rows(encode(field,reference,generator)),context,owner['Row'],owner['mean'],Z)
    return make_packet(rows,field,reference,context,policy,owner,Z,O)

def terminal(packet):return vertical(vertical(horizontal(packet,owner),owner),owner)

def change(packet,reference):return change_reference(packet,reference,context,owner,Z,O)

def check(change_record):return verify_change(change_record,context,owner,Z,O)

sources={policy:prepare(field,source_reference,policy) for policy in ('inherited','common')}
assert all(p.certificate.status=='reconstructible' and not p.operator_fallback for p in sources.values())
source=sources['common'];core=operator_packet(field)
assert operator_core(source,context,owner,Z,O)==(core,'scalar-reconstruction')
# Census every possible directed mark, without changing the underlying field.
census=[];transitions={}
for reference in EDGES:
    transition=change(source,reference);target=transition.target
    assert operator_core(target,context,owner,Z,O)[0]==core
    assert data_from_leaves(owner['leaves'](raw_rows(target,owner)),reference)==previous.readout(field,previous.K,previous.ops,reference,Z)
    if reference==source_reference:assert target==source
    transitions[reference]=transition
    census.append({'reference':reference,'status':target.certificate.status,'fallback_blocks':len(target.operator_fallback),'target_obligation':transition.target_obligation})
first=transitions[deficient_reference]
assert first.source_route=='scalar-reconstruction'
assert first.target.certificate.status=='requires-retained-operator-data' and len(first.target.operator_fallback)==144
back=change(first.target,source_reference)
assert back.source_route=='retained-operator-data' and back.target==source
second=change(first.target,third_reference)
direct,path=compose((first,second),context,owner,Z,O)
assert direct.target==transitions[third_reference].target and len(path)==2
assert direct.target.operator_fallback==() and direct.target.certificate.status=='reconstructible'
identity,loop=compose((first,back),context,owner,Z,O)
assert identity.target==source and len(loop)==2
# The certificate and fallback must be recomputed for the NEW omitted arrow,
# not inherited from the prior good chart. They commute with retained transport.
naturality=0
for policy,start in sources.items():
    changed=change(start,deficient_reference).target
    assert horizontal(changed,owner)==change(horizontal(start,owner),deficient_reference).target; naturality+=1
    assert vertical(changed,owner)==change(vertical(start,owner),deficient_reference).target; naturality+=1
    assert terminal(changed)==change(terminal(start),deficient_reference).target; naturality+=1
    verify(terminal(changed),context,owner,Z,O)
# The zero stratum also changes references, using its explicit sidecar.
zero_source=baseline.packets['zero','common']
zero_change=change(zero_source,third_reference)
assert zero_change.source_route=='retained-operator-data'
assert change(zero_change.target,zero_source.reference).target==zero_source
# Two fields become identical scalar packets at the deficient reference but
# have different operator cores. They must not be glued along scalar equality.
other_source=prepare(previous.blind_other,source_reference,'common')
other_bad=change(other_source,deficient_reference)
assert owner['leaves'](raw_rows(first.target,owner))==owner['leaves'](raw_rows(other_bad.target,owner))
assert first.target.operator_fallback!=other_bad.target.operator_fallback
other_second=change(other_bad.target,third_reference)
negative_controls=0

def reject(call):
    global negative_controls
    try:call()
    except (ValueError,AssertionError):negative_controls+=1
    else:raise AssertionError('Invalid reference transition accepted')

reject(lambda:change(source,(0,0)))
reject(lambda:change(replace(first.target,operator_fallback=()),third_reference))
reject(lambda:check(replace(first,target=replace(first.target,certificate=source.certificate))))
reject(lambda:check(replace(first,target_obligation='scalar-packet-suffices')))
reject(lambda:check(replace(first,source_route='retained-operator-data')))
reject(lambda:compose((first,other_second),context,owner,Z,O))
reject(lambda:change(replace(source,context=replace(context,phase_policy='invented-anchor')),third_reference))
# Changing only the mark without regenerating its 121 leaf labels/values is invalid.
reject(lambda:change(replace(source,reference=deficient_reference),third_reference))
report={'schema':'marici.field-reference-transitions.v1','status':'pass','source_reference':source_reference,
 'reference_census':census,'identity_roundtrip_and_cocycle':True,'composition_history_retained_separately':True,
 'retained_transport_naturality_checks':naturality,'retention_policies':['inherited','common'],
 'good_to_deficient_to_good':{'references':[source_reference,deficient_reference,third_reference],'fallback_block_counts':[0,144,len(second.target.operator_fallback)],'direct_and_composite_packets_equal':True},
 'zero_stratum_roundtrip':True,'same_scalars_different_cores_cannot_compose':True,'negative_controls':negative_controls,
 'implementation_input':'validated packets only; no original field or amplitude anchor',
 'scope':'Exact reference changes through a complete unanchored operator core; scalar-only reference changes are partial. No uniform transition stability, minimal retention, physical d, instrument or fixed-2x2 DG binding claim.',
 'prerequisite_replay':log.getvalue()}
atlas_path=ROOT/'research/strominger/rung-symmetry-atlas-v3.json'
atlas=json.loads(atlas_path.read_text(encoding='utf8'))['readout_layers']['reference_transitions']
assert atlas['reference_census']==len(census) and atlas['retained_transport_naturality_checks']==naturality
assert atlas['target_retention_recomputed'] and not atlas['minimal_retention_claimed']
paths=[Path(__file__),Path(__file__).with_name('field_reference_transitions.py'),Path(__file__).with_name('reconstruction_aware_tower.py'),atlas_path,ROOT/'research/strominger/field-reference-transitions-v1.md']
report['direct_source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
out=ROOT/'research/strominger/results/field-reference-transitions';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ('prerequisite_replay','direct_source_hashes')},indent=2))
