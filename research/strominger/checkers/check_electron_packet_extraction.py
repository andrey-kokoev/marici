"""Exact return-image extraction, continuation squares and erasure hostiles."""
from dataclasses import replace
from hashlib import sha256
import json
from pathlib import Path
import sys
from electron_packet_interface import (ROOT, STORE, Interface, Packet, SourceState, Archive,
    ACTIONS,E,I,F,G0,G1,act,adj,sm,gmm,gt,gm,gc,matrix_add)

def digest(p): return sha256(p.read_bytes()).hexdigest()
def inner(x,y): return gt(gm(gc(a),b) for a,b in zip(x,y))
def reject(action,text):
    try: action()
    except ValueError as e: assert text in str(e),(text,str(e))
    else: raise AssertionError('accepted invalid object: '+text)

prior_path=ROOT/'research/voevodsky/results/electron-three-direction-trial-v1.json'
prior=json.loads(prior_path.read_text(encoding='utf-8'))
assert prior['verification_passed'] and all(prior['checks'].values())
pins=dict(prior['source_sha256']); pins[prior_path.relative_to(ROOT).as_posix()]=digest(prior_path)
for name in ('electron_packet_interface.py','check_electron_packet_extraction.py'):
    p=Path(__file__).with_name(name).resolve(); pins[p.relative_to(ROOT).as_posix()]=digest(p)
for module in tuple(sys.modules.values()):
    file=getattr(module,'__file__',None)
    if file:
        p=Path(file).resolve()
        if p.suffix=='.py' and p.parent==ROOT/'research/voevodsky/checkers':
            key=p.relative_to(ROOT).as_posix()
            if key in pins: assert pins[key]==digest(p),'stale imported prerequisite: '+key
            pins[key]=digest(p)
assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale prerequisite pins'
before={p:digest(ROOT/p) for p in pins}
f=Interface(); assert len(ACTIONS)==24 and all(e in ACTIONS for e in E)
assert gmm(f.N,f.N)==f.N
for stage in f.stages: assert gmm(stage,f.K)==f.K
# Universal matrix equations, independent of the sample spinors.
for u in ACTIONS:
    W=f.raw_actions[u]
    assert gmm(W,f.K)==gmm(f.K,u)
    assert gmm(f.D,W)==gmm(u,f.D)
    assert gmm(f.raw_actions[adj(u)],W)==f.N
    for v in ACTIONS:
        assert gmm(u,v) in ACTIONS
        assert gmm(f.raw_actions[v],W)==f.raw_actions[gmm(v,u)]
# I on the raw8 space is NOT the operation identity: the inherited identity is N on im(K).
assert f.raw_actions[I]==f.N and f.N!=tuple(tuple(G1 if i==j else G0 for j in range(8)) for i in range(8))
samples=((G1,G0),(G0,G1),((F(3,5),F(0)),(F(0),F(4,5))),((F(6,7),F(0)),(F(3,7),F(2,7))))
for z in samples:
    s=f.seed(z); p=f.extract(s)
    assert f.recover(p)==s and f.extract(f.recover(p))==p
    assert tuple(tuple(inner(a,b)[0] for b in p.directions) for a in p.directions)==tuple(tuple(F(a==b) for b in range(3)) for a in range(3))
    for u in ACTIONS:
        s1=f.source_step(s,u); p1=f.packet_step(p,u)
        assert f.extract(s1)==p1 and f.recover(p1)==s1
        assert f.recover(f.packet_step(p1,adj(u))).raw==s.raw
    # Same coefficient endpoint, different admitted construction history.
    s2=f.source_step(f.source_step(s,E[0]),adj(E[0]))
    assert s2.raw==s.raw and s2!=s and f.extract(s2)!=p
s=f.seed(samples[2]); p=f.extract(s)
reject(lambda:f.extract(SourceState(s.archive,(G1,)+(G0,)*7)),'raw state/image/history')
reject(lambda:f.extract(replace(s,archive=replace(s.archive,source_sha256='erased'))),'source binding')
reject(lambda:f.recover(replace(p,directions=(p.directions[1],p.directions[0],p.directions[2]))),'frame mismatch')
reject(lambda:f.recover(replace(p,archive=replace(p.archive,word=(E[0],)))),'packet history')
reject(lambda:f.packet_step(p,sm(2,I)),'operation unavailable')
reject(lambda:f.source_step(s,sm(2,I)),'operation unavailable')
# Sign erasure preserves density but loses a full-amplitude/reference continuation.
a=f.packet_step(f.packet_step(p,E[0]),E[1]); b=f.packet_step(f.packet_step(p,E[1]),E[0])
assert a.spinor==tuple((-x[0],-x[1]) for x in b.spinor)
density=lambda z:tuple(tuple(gm(x,gc(y)) for y in z) for x in z)
assert density(a.spinor)==density(b.spinor) and a!=b
assert inner(a.spinor,a.spinor)==G1 and inner(a.spinor,b.spinor)==(-F(1),F(0))
assert all(digest(ROOT/path)==h for path,h in before.items())
checks={
 'prerequisite_pins_and_native_inputs_unchanged':True,
 'encoder_decoder_and_actual_native_return_identity':True,
 'all_three_native_stages_fix_encoded_return_image':True,
 'all24_enabled_logical_actions_have_exact_raw_and_packet_squares':True,
 'all576_action_compositions_and_image_only_inverse_laws':True,
 'four_normalized_samples_recover_state_and_archive':True,
 'same_endpoint_different_history_not_identified':True,
 'off_image_wrong_source_wrong_frame_wrong_history_rejected':True,
 'matching_source_packet_enabled_domains_reject_amplification':True,
 'ray_erasure_loses_minus_identity_reference_continuation':True}
report={'schema':'marici.electron-packet-extraction.v1','status':'pass','checks':checks,
 'scope':'Native electron normalized return image im(K), not arbitrary raw8 states, geometry or entire assembly source reconstruction.',
 'laws':{'DK':'I2','KD':'actual stored N','p_step':'p(W_u x,archive+c)=step_P(p(x,archive),u)','W_u':'K u D','inverse':'W_(u*) W_u=N on raw8, identity only on im(K)'},
 'native_logical_actions':24,'composition_pairs':576,'sample_states':4,
 'archive':'Native store digest, initial normalized spinor and complete command word; no quotient of equal endpoints.',
 'dimension_policy':'Local real variation directions of the full normalized retained carrier, including phase. Electron n=3; no proton/neutron n assigned.',
 'hostile_reference_pairing':['1','-1'],'source_sha256':pins,
 'formal_proof_recompiled':False,'native_producers_executed':False,'physical_particle_or_cost_claim':False}
out=ROOT/'research/strominger/results/electron-packet-extraction-v1.json'
out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='source_sha256'},indent=2))
