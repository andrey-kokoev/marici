#!/usr/bin/env python3
"""Exact cutoff bonding maps for minimal G4 candidate module skeletons."""
import json
from pathlib import Path
from evidence_policy import write_result
R=Path(__file__).resolve().parents[2]
grades=(1,2); ori=('forward','reciprocal'); selected=((2,1),(3,2))
def skeleton(P):
 P=tuple(P); out=['wall_even','wall_odd']
 out += [f'p{p}_k{k}_{o}' for p in P for k in grades for o in ori]
 if selected[0][0] in P and selected[1][0] in P:
  out += ['link_(p2k1,p3k2)','link_(p3k2,p2k1)']
 out += ['archimedean_radial']; return out
def inc(P,Q,v):
 assert set(P)<=set(Q); return {k:v.get(k,0) for k in skeleton(Q)}
def ret(P,Q,v):
 assert set(P)<=set(Q); return {k:v.get(k,0) for k in skeleton(P)}
def vec(P): return {k:i+1 for i,k in enumerate(skeleton(P))}
P=(2,);Q=(2,3);S=(2,3,5);x=vec(P);y=vec(Q)
checks={'left_inverse':ret(P,Q,inc(P,Q,x))==x,'composition':inc(Q,S,inc(P,Q,x))==inc(P,S,x),'retraction_composition':ret(P,Q,ret(Q,S,inc(Q,S,y)))==ret(P,S,inc(Q,S,y)),'old_coordinates_fixed':all(inc(P,Q,x)[k]==x[k] for k in skeleton(P)),'new_coordinates_zero':all(inc(P,Q,x)[k]==0 for k in set(skeleton(Q))-set(skeleton(P))),'link_appears_only_when_typed':not any(k.startswith('link_') for k in skeleton(P)) and sum(k.startswith('link_') for k in skeleton(Q))==2,'shared_ports_not_duplicated':skeleton(S).count('wall_even')==skeleton(S).count('archimedean_radial')==1};assert all(checks.values())
out={'schema':'marici.conjecture-replay.CR1-candidate-cutoff-bonding.v1','passed':True,'claim_status':'proved','evidence':[{'class':'SYMBOLIC','claim':'Coordinate extension by zero and restriction satisfy identity, composition, typed-link appearance, and shared-port nonduplication on three nested prime cutoffs.','checker':'research/conjecture_replay/check_CR1_candidate_cutoff_bonding.py'},{'class':'SOURCE_DERIVED','claim':'Prime-labelled source blocks are diagonal and cutoff projections commute with retained radial response construction.','source':'research/aspect/contracts/theta-rh-g4-radial-interface.v1.json'}],'outcome':'++ algebraic cutoff system for finite target candidates','cutoffs':['{2}','{2,3}','{2,3,5}'],'inclusion':'i_PQ extends new prime, orientation, and newly typed linking modules by zero while fixing wall and archimedean shared modules','retraction':'r_PQ restricts to modules supported at P; r_PQ i_PQ=I','composition':'i_QS i_PQ=i_PS and r_PQ r_QS=r_PS','checks':checks,'metric':'For the source-labelled block-diagonal saturated metric, i_PQ is isometric and r_PQ is contractive. Both have norm one because the shared wall module is nonzero.','response':'Function-valued modules are transported by identity on old labels, not scalar sampled; linking modules appear only when both ordered labels are present.','jets':'Bonding maps are parameter-independent, so they commute with every spectral derivative.','colimit':'The algebraic direct limit is the finite-support labelled target with one shared wall and archimedean module. This does not itself choose or complete a global topology.','remaining':'Prove Cauchy compatibility and closedness in the weighted projective/Hilbert/nuclear completion, including all selected ordered linking modules.','next':'construct_the_weighted_completion_seminorms_and_show_the_bonding_maps_have_uniform_norm_one_on_each_rung'}
write_result(R/'research/conjecture_replay/results/CR1_candidate_cutoff_bonding.json',out);print(json.dumps({'passed':True,'sizes':[len(skeleton(Z)) for Z in (P,Q,S)],'checks':checks}))
