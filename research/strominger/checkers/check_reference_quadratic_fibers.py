"""Sharper reference fibers and a compact, backward-compatible retention adapter."""
from pathlib import Path
from dataclasses import replace
import contextlib,io,json,hashlib
from field_refibration import EDGES
from reference_quadratic_fibers import fiber
from sharp_reference_packets import compact,expand,change_sharp_reference
from reconstruction_aware_tower import horizontal
ROOT=Path(__file__).resolve().parents[3];log=io.StringIO()
with contextlib.redirect_stdout(log):import check_field_reference_transitions as previous
A,Z,O=previous.A,previous.Z,previous.O
context,owner=previous.context,previous.owner
census=[];packets={}
for reference,transition in previous.transitions.items():
    old=transition.target;new=compact(old,context,owner,Z,O)
    assert expand(new,context,owner,Z,O)==old
    packets[reference]=new
    census.append({'reference':reference,'old_gate':old.certificate.status,'new_kind':new.certificate.kind,
                   'all_channel_linear_rank':new.certificate.linear_rank,'reason':new.certificate.reason,
                   'old_fallback_blocks':len(old.operator_fallback),'new_full_fallback_blocks':len(new.full_operator_fallback),
                   'new_completion_complex_values':len(new.completion.values) if new.completion else 0})
assert packets[0,1].certificate.kind=='continuous' and packets[0,1].completion is not None
assert all(packets[e].certificate.kind=='unique' and packets[e].completion is None for e in EDGES if e!=(0,1))
assert all(not p.full_operator_fallback for p in packets.values())
# Real source fixture with no reference probes at all, but zero norm fixes x=0.
zero_reference=dict(previous.field);zero_reference[0,1]=(Z,Z,Z)
old_zero=previous.prepare(zero_reference,(0,1),'common')
new_zero=compact(old_zero,context,owner,Z,O)
assert new_zero.certificate.kind=='unique' and new_zero.certificate.linear_rank==0
assert new_zero.certificate.reason=='minimum-norm quadratic tangency'
assert new_zero.completion is None and expand(new_zero,context,owner,Z,O)==old_zero
# Missing selected span remains outside the new theorem, with full fallback.
zero_packet=previous.baseline.packets['zero','common']
unsupported=compact(zero_packet,context,owner,Z,O)
assert unsupported.certificate.kind=='selected-span-fallback' and len(unsupported.full_operator_fallback)==144
assert expand(unsupported,context,owner,Z,O)==zero_packet
# Weak reference conditioning is not erased by the new exact-retention policy.
old_weak=previous.baseline.packets['weak-probes','common'];new_weak=compact(old_weak,context,owner,Z,O)
assert new_weak.certificate.kind=='unique' and new_weak.completion is None
assert new_weak.prior_probe_certificate==old_weak.certificate
assert expand(new_weak,context,owner,Z,O)==old_weak
# Reference transitions operate through the unchanged verified old interface.
a,b,c=(0,2),(0,1),(2,3)
step=lambda packet,reference:change_sharp_reference(packet,reference,context,owner,Z,O)
assert step(packets[a],a)==packets[a]
assert step(step(packets[a],b),a)==packets[a]
assert step(step(packets[a],b),c)==step(packets[a],c)==packets[c]
for policy,source in previous.sources.items():
    left=compact(horizontal(previous.change(source,b).target,owner),context,owner,Z,O)
    right=step(compact(horizontal(source,owner),context,owner,Z,O),b)
    assert left==right
# Same scalar leaves, different needed three-value completion column.
other=compact(previous.other_bad.target,context,owner,Z,O)
assert other.carrier==packets[b].carrier and other.completion!=packets[b].completion
# Algebra-only tests cover the full complex-nullity-one classification.
# These synthetic operators are NOT substituted for the source corner cycle.
I={(i,j):A(int(i==j)) for i in range(3) for j in range(3)}
P={(i,j):A(1)/2 if i<2 and j<2 else Z for i in range(3) for j in range(3)}
Q={k:I[k]-P[k] for k in I};ops={'P':P,'Q':Q,'C':I}
rows=((O,Z,Z),(Z,Z,O));values=(O,Z)
two=fiber(rows,values,{'P':O,'Q':O,'C':A(2)},I,ops,Z,O)
assert two['kind']=='finite-two' and two['linear_rank']==2
assert two['alternatives']['radicand']==O
# No square root needs to be chosen by the production classifier.
tangent=fiber(rows,values,{'P':A(2),'Q':Z,'C':A(2)},I,ops,Z,O)
assert tangent['kind']=='unique' and tangent['solution']==(O,O,Z)
P0={(i,j):A(int(i==j==0)) for i in range(3) for j in range(3)}
circle_ops={'P':P0,'Q':{k:I[k]-P0[k] for k in I},'C':I}
circle=fiber(rows,values,{'P':O,'Q':O,'C':A(2)},I,circle_ops,Z,O)
assert circle['kind']=='continuous' and circle['reason']=='entire residual circle'
negative_controls=0

def reject(call):
    global negative_controls
    try:call()
    except (ValueError,AssertionError):negative_controls+=1
    else:raise AssertionError('Invalid compact reconstruction accepted')

reject(lambda:expand(replace(packets[b],completion=None),context,owner,Z,O))
column=packets[b].completion
reject(lambda:expand(replace(packets[b],completion=replace(column,values=(Z,Z,Z))),context,owner,Z,O))
reject(lambda:expand(replace(packets[b],completion=replace(column,anchor_component=3)),context,owner,Z,O))
reject(lambda:expand(replace(packets[b],certificate=replace(packets[b].certificate,kind='unique')),context,owner,Z,O))
reject(lambda:expand(replace(unsupported,full_operator_fallback=()),context,owner,Z,O))
reject(lambda:expand(replace(new_weak,prior_probe_certificate=packets[a].prior_probe_certificate),context,owner,Z,O))
reject(lambda:fiber(rows,values,{'P':A(3),'Q':A(-1),'C':A(2)},I,ops,Z,O))
report={'schema':'marici.reference-quadratic-fibers.v1','status':'pass','reference_census':census,
 'source_zero_norm_case':{'linear_rank':0,'unique':True,'extra_records':0},
 'nullity_one_algebra_tests':['finite-two','unique-tangent','continuous-circle'],
 'synthetic_cycle_is_not_source_cycle':True,'higher_nullity_nonhomogeneous':'unresolved; retained completion required',
 'sharp_reference_identity_roundtrip_cocycle':True,'retained_promotion_compatibility_policies':2,
 'existing_packet_expansion_roundtrips':True,'conditioning_warnings_retained':True,
 'completion_record':'one canonically anchored outer-product column: three complex values, no phase anchor',
 'negative_controls':negative_controls,'minimality_claimed':False,
 'scope':'Exact classification on stated strata; no universal higher-nullity classification or improved noise stability. Original packet verifier remains authoritative after expansion.',
 'prerequisite_replay':log.getvalue()}
atlas_path=ROOT/'research/strominger/rung-symmetry-atlas-v3.json'
atlas=json.loads(atlas_path.read_text(encoding='utf8'))['readout_layers']['sharp_reference_fibers']
assert atlas['reference_census_unique']==sum(row['new_kind']=='unique' for row in census)
assert atlas['reference_census_continuous']==sum(row['new_kind']=='continuous' for row in census)
assert atlas['conditioning_warnings_preserved'] and not atlas['minimality_claimed']
paths=[Path(__file__),Path(__file__).with_name('reference_quadratic_fibers.py'),Path(__file__).with_name('sharp_reference_packets.py'),Path(__file__).with_name('field_reconstruction.py'),atlas_path,ROOT/'research/strominger/reference-quadratic-fibers-v1.md']
report['direct_source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
out=ROOT/'research/strominger/results/reference-quadratic-fibers';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ('prerequisite_replay','direct_source_hashes')},indent=2))
