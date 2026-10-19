"""Direct compact charts: oracle agreement, exact laws, weak/zero anchor gates."""
from pathlib import Path
from dataclasses import replace
from fractions import Fraction as F
from contextlib import ExitStack
from unittest.mock import patch
import contextlib,io,json,hashlib
from field_refibration import EDGES
from reconstruction_aware_tower import horizontal,vertical
from sharp_reference_packets import compact,change_sharp_reference
import direct_compact_transitions as direct
ROOT=Path(__file__).resolve().parents[3];log=io.StringIO()
with contextlib.redirect_stdout(log):import check_reference_quadratic_fibers as baseline
previous=baseline.previous;A,Z,O=baseline.A,baseline.Z,baseline.O
context,owner=baseline.context,baseline.owner
threshold=A(F(1,1000));a,b,c=(0,2),(0,1),(2,3)
# Oracles and preparations are built OUTSIDE the guarded direct operations.
oracles=baseline.packets
policy_sources={policy:compact(source,context,owner,Z,O) for policy,source in previous.sources.items()}
weak_field=dict(previous.field)
weak_field[0,2]=tuple(A(F(1,1000000))*v for v in weak_field[0,2])
weak_sharp=compact(previous.prepare(weak_field,b,'common'),context,owner,Z,O)
scarce={edge:tuple(A(int(j==(i%2))) for j in range(3)) for i,edge in enumerate(EDGES)}
scarce[c]=(Z,Z,O)
scarce_sharp=compact(previous.prepare(scarce,b,'common'),context,owner,Z,O)
fallback_oracle=change_sharp_reference(scarce_sharp,c,context,owner,Z,O)
assert len(fallback_oracle.full_operator_fallback)==144
blocked_calls=0;negative_controls=0

def forbidden(*args,**kwargs):
    global blocked_calls
    blocked_calls+=1
    raise AssertionError('Full-core materialization or legacy bridge attempted')

def reject(call,error_type=ValueError):
    global negative_controls
    try:call()
    except error_type:negative_controls+=1
    else:raise AssertionError('Invalid direct transition accepted')

blocked=[
 'reconstruction_aware_tower.operator_packet','reconstruction_aware_tower.recover_operator_packet',
 'sharp_reference_packets.operator_packet','sharp_reference_packets.operator_core',
 'sharp_reference_packets.expand','sharp_reference_packets.compact','sharp_reference_packets.change_reference',
 'field_reference_transitions.operator_packet','field_reference_transitions.operator_core',
 'field_reference_transitions.recover_operator_packet','field_reference_transitions.change_reference']
with ExitStack() as stack:
    for name in blocked:stack.enter_context(patch(name,forbidden))
    enter=lambda p,strongest=True:direct.from_sharp(p,context,owner,Z,O,threshold,strongest)
    decode=lambda p:direct.decode(p,context,owner,Z,O)
    step=lambda p,r,anchor=None:direct.change_reference(p,r,context,owner,Z,O,anchor)
    reanchor=lambda p,anchor:direct.reanchor(p,anchor,context,owner,Z,O)
    canonical=lambda p:direct.to_sharp(p,context,owner,Z,O)
    start=enter(oracles[a]);targets={}
    for reference in EDGES:
        target=step(start,reference)
        assert canonical(target)==oracles[reference]
        targets[reference]=target
    assert step(start,a)==start
    assert step(step(start,b),a)==start
    assert step(step(start,b),c)==step(start,c)
    # General chart laws hold with the same requested destination anchor.
    base=targets[b];field,rho,_=decode(base)
    old_anchor=(base.completion.anchor_edge,base.completion.anchor_component)
    anchors=[(edge,j) for edge in EDGES if edge!=b for j in range(3) if field[edge][j]!=Z]
    middle=next(key for key in anchors if key!=old_anchor)
    last=next(key for key in anchors if key not in (old_anchor,middle))
    assert reanchor(base,old_anchor)==base
    assert reanchor(reanchor(base,middle),old_anchor)==base
    assert reanchor(reanchor(base,middle),last)==reanchor(base,last)
    custom=reanchor(base,middle)
    assert step(custom,b,middle)==custom
    assert step(step(custom,a),b,middle)==custom
    assert canonical(custom)==oracles[b]
    excluded=step(base,old_anchor[0])
    assert excluded.completion is None or excluded.completion.anchor_edge!=excluded.carrier.reference
    # Weak chosen chart, then a stronger chart, with unchanged scalar carrier.
    weak=enter(weak_sharp,False)
    assert weak.anchor_certificate.status=='weak'
    weak_rep,weak_rho,_=decode(weak)
    best=direct.choose_anchor(weak_rep,b,weak_rho,Z)
    strong=reanchor(weak,best)
    assert strong.anchor_certificate.status=='above-threshold'
    assert strong.carrier==weak.carrier and canonical(strong)==weak_sharp
    assert strong.prior_probe_certificate==weak.prior_probe_certificate
    # Reference changes commute with all existing retained transport roles.
    naturality=0
    def terminal(carrier,owner):return vertical(vertical(horizontal(carrier,owner),owner),owner)
    for policy,source in policy_sources.items():
        packet=enter(source)
        for operation in (horizontal,vertical,terminal):
            transport=lambda p:direct.transport(p,operation,context,owner,Z,O)
            assert transport(step(packet,b))==step(transport(packet),b)
            naturality+=1
    # Stop before losing coverage: use the old fallback route, not a fake scalar packet.
    scarce_direct=enter(scarce_sharp)
    reject(lambda:step(scarce_direct,c),direct.FullFallbackRequired)
    reject(lambda:enter(baseline.unsupported),direct.FullFallbackRequired)
    reject(lambda:reanchor(base,((2,1),0)))
    reject(lambda:reanchor(base,(b,0)))
    reject(lambda:decode(replace(base,anchor_certificate=replace(base.anchor_certificate,strength_squared=Z))))
    reject(lambda:decode(replace(base,completion=replace(base.completion,values=(Z,Z,Z)))))
    reject(lambda:step(start,(0,0)))
    reject(lambda:decode(replace(base,anchor_threshold_squared=Z)))
    reject(lambda:decode(replace(base,prior_probe_certificate=replace(base.prior_probe_certificate,reason='forged'))))
assert blocked_calls==0
report={'schema':'marici.direct-compact-transitions.v1','status':'pass',
 'all_reference_oracle_agreements':len(targets),'blocked_full_core_entrypoints':len(blocked),'full_core_calls_during_direct_checks':blocked_calls,
 'reference_identity_roundtrip_cocycle':True,'anchor_identity_roundtrip_cocycle':True,
 'arbitrary_chart_roundtrip_with_fixed_destination_anchor':True,'retained_transport_naturality_checks':naturality,
 'weak_anchor':{'threshold_squared':threshold.record(),'before':weak.anchor_certificate.strength_squared.record(),'after':strong.anchor_certificate.strength_squared.record(),'scalar_carrier_unchanged':True,'prior_conditioning_warning_unchanged':True},
 'target_span_failure':{'direct_transition':'explicit FullFallbackRequired','old_route_fallback_blocks':len(fallback_oracle.full_operator_fallback)},
 'negative_controls':negative_controls,'temporary_representation':'36 complex coordinates plus positive normalization; no 144-block core',
 'scope':'Exact direct transitions on selected-spanning charts. Anchor strength is a coordinate diagnostic, not a whole-decoder condition number; no physical phase or stability theorem.',
 'prerequisite_replay':log.getvalue()}
atlas_path=ROOT/'research/strominger/rung-symmetry-atlas-v3.json'
atlas=json.loads(atlas_path.read_text(encoding='utf8'))['readout_layers']['direct_compact_charts']
assert atlas['all_reference_oracle_agreements']==len(targets) and atlas['guarded_full_core_calls']==blocked_calls
assert atlas['retained_transport_naturality_checks']==naturality and not atlas['whole_decoder_stability_claimed']
paths=[Path(__file__),Path(__file__).with_name('direct_compact_transitions.py'),Path(__file__).with_name('reconstruction_aware_tower.py'),atlas_path,ROOT/'research/strominger/direct-compact-transitions-v1.md']
report['direct_source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
out=ROOT/'research/strominger/results/direct-compact-transitions';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ('prerequisite_replay','direct_source_hashes')},indent=2))
