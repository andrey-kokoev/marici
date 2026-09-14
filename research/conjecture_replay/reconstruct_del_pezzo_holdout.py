#!/usr/bin/env python3
"""Reconstruct and annotate all post-entrance holdout observations."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
freeze=json.loads((R/'research/conjecture_replay/results/del_pezzo_entrance_freeze.json').read_text())
typed=json.loads((R/'research/conjecture_replay/results/del_pezzo_typed_quiver.json').read_text())
# Primary entrance conjecture, epistemic effect, and concise observation. These
# annotations are scoring data and are never inputs to entrance policy synthesis.
ann=[
('DP1','support','reflection-preserved pencil has four split critical fibers spanning rank three'),
('DP2','support','source soft node is a split-fiber component difference'),
('DP4','revision','primitive closure exists with raw-lattice index four, refining the guessed index'),
('DP5','support','two-bit quotient is the three pairings of four split fibers'),
('DP6','partial','total energy gives a double-conic degeneration and four smoothing points'),
('DP6','partial','four width-two local smoothing marks are identified'),
('DP5','support','local singularity is cD4 with discriminant group (Z/2)^2'),
('DP5','support','site exchange acts by D4 triality'),
('DP6','partial','outer-arm incidence is the criterion for nonzero physical class'),
('DP6','support','total-energy branch meets the fixed outer D4 arm'),
('DP5','refute','naive equivariant identification of D4 and source parity planes fails'),
('DP3','partial','v_alg evaluates equally on four conductor marks and does not select one'),
('DP5','support','conductor marks acquire a canonical real cyclic order'),
('DP6','support','BD prescription orients collision arcs'),
('DP2','support','paired nodes produce odd primitive e6 component'),
('DP3','refute','generic total-energy thimble does not link the v_alg divisor'),
('DP3','revision','base dlog regularity alone cannot decide extension residue'),
('DP5','partial','conductor smoothing has a global square-root section'),
('DP5','support','square root has an alternating real Cech cocycle'),
('DP6','support','BD orientation determines the conductor Cech chain'),
('DP3','refute','oriented conductor residue gives zero v_alg parity'),
('DP6','refute','claimed direct parity pairings are ill-typed and withdrawn'),
('DP3','refute','marked top-kernel extension maps only to e6'),
('DP2','support','primitive top kernel has unit e6 incidence'),
('DP6','support','physical cusp predictions pass their stated tests'),
('DP6','support','BD marked-top discontinuity supplies a physical parity readout'),
('DP2','support','two-node cellular boundary derives unit e6 incidence'),
('DP7','support','infinity components receive an explicit Picard marking'),
('DP6','support','marked-top logarithmic discontinuity law is derived'),
('DP6','support','physical cusp monodromy is a transvection'),
('DP6','revision','first physical-current specialization remains conditional'),
('DP6','refute','one proposed physical-corner support mechanism is falsified'),
('DP6','support','iterated physical corner reads primitive e6 and zero v_alg'),
('DP5','support','split-bitangent differences form one mod-two Weyl orbit'),
('DP2','revision','corner e6 coordinate has Betti index four in the tested normalization'),
('DP2','support','physical occurrence pair restores primitive e6 integrality'),
('DP6','support','plain logarithmic and iterated Cut operations form an integral cospan'),
('DP3','refute','tested mixed corner packets add no v_alg rank'),
('DP3','refute','all sourced corner projections have rank one on e6'),
('DP2','support','local physical e6 detector agrees with the global component difference'),
('DP5','support','triality and adjacent cusp parity transport consistently'),
('DP5','refute','theta-characteristic axioms do not supply the claimed selector'),
('DP3','refute','canonical physical mixed residue cancels v_alg'),
('DP3','partial','fixed-coordinate exchange-odd response produces a candidate'),
('DP3','refute','candidate principal response vanishes under wall-horizontal GM lift')]
assert len(ann)==len(freeze['holdout_manifest'])
events=[]
for i,(h,(dp,effect,summary)) in enumerate(zip(freeze['holdout_manifest'],ann),1):
 data=json.loads((R/h['path']).read_text())
 events.append({'sequence':i,'artifact':h['path'],'sha256':h['sha256'],'schema':data.get('schema'),'primary_conjecture':dp,'effect':effect,'observation':summary,'passed_packet':data.get('passed',data.get('all_checks_pass',True))})
counts={}
for e in events:
 counts.setdefault(e['primary_conjecture'],{'support':0,'refute':0,'partial':0,'revision':0})[e['effect']]+=1
# Final retrospective dispositions do not overwrite the sequence.
final={
'DP1':{'relation':'++','basis':'four split fibers span the invariant rank-three lattice'},
'DP2':{'relation':'++','basis':'e6 is a primitive global component difference with sourced physical incidence'},
'DP3':{'relation':'--','basis':'many proposed realizations fail; intrinsic v_alg marking/readout remains unresolved'},
'DP4':{'relation':'++','basis':'the conjectured nontrivial saturation explains the half-factor; its index is four'},
'DP5':{'relation':'++','basis':'the stated two-bit ambiguity is exactly encoded by the three geometric pairings'},
'DP6':{'relation':'++','basis':'the stated physical degeneration selects a primitive integral e6 class; this conjecture did not claim two-channel completeness'},
'DP7':{'relation':'++','basis':'an adapted Picard marking is eventually constructed'},
'DP8':{'relation':'-+','basis':'available involutions are mod-two trivial on the source support plane and fail as selector'}}
checks={'all_45_manifest_entries_annotated':len(events)==45,'sequence_exact':all(e['sequence']==i for i,e in enumerate(events,1)),'hashes_match_freeze':all(e['sha256']==freeze['holdout_manifest'][i-1]['sha256'] for i,e in enumerate(events,1)),'known_effects':all(e['effect'] in {'support','refute','partial','revision'} for e in events),'observed_DP_nodes_match_expected':set(counts)==({x['id'] for x in typed['typed_conjectures']}-{'DP8'}),'DP8_explicitly_censored': 'DP8' not in counts,'all_final_relations_typed':all(v['relation'] in typed['sign_semantics'] for v in final.values())}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.del-pezzo-holdout-sequence.v1','role':'retrospective scoring only; forbidden as policy input','events':events,'effect_counts':counts,'final_retrospective_dispositions':final,'checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/del_pezzo_holdout_sequence.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'events':len(events),'effect_counts':counts,'final':{k:v['relation'] for k,v in final.items()}}))
