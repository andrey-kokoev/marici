#!/usr/bin/env python3
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from interpretation_planner import *
r=json.loads((R/'research/benincasa/results/G12_VC1b_sparse_membership.json').read_text());assert r['VC1b_resolution']=='-+'
def A(n,c,req,add):
 bs={}
 for o in OUTCOMES:
  x=next(iter(add if o=='++' else {f'{n}:{o}'}));bs[o]=Branch(.25,Effect(add=frozenset({x})),(Implication(Proposition('branch',(n,o)),'entails',Proposition(x),'checker'),))
 return Action(n,c,frozenset(req),bs)
actions=[A('VC2b_construct_stage2_overlap_differential',5,['VC2_stage1_quotient'],{'VC2_stage2_differential'}),A('VC2c_verify_exchange_and_path_coherence',3,['VC2_stage2_differential'],{'VC2_coherent_complex'}),A('VC2d_physical_boundary_descent',3,['VC2_coherent_complex'],{'filtered_IBP_lowering'}),A('VC3_apply_lowering_and_project',4,['filtered_IBP_lowering','physical_odd_shape_response'],{'physical_valg_channel'}),A('VC4_integral_normalization',7,['physical_valg_channel'],{'integral_valg'}),A('VC5_Smith_validation',3,['integral_valg','physical_e6'],{'two_channel_physical_readout'})]
s=State(frozenset(),frozenset({'VC2_stage1_quotient','VC1b_sparse_budget_obstructed','physical_odd_shape_response','physical_e6'}));d=Decoder('VC5_Smith_validation',None,frozenset({'two_channel_physical_readout'}),'target');v=Planner(actions,[d],'target',require_implications=True).solve_expected(s);assert v.first_action=='VC2b_construct_stage2_overlap_differential'
out={'schema':'marici.conjecture-replay.post-VC1b-replan.v1','resolved':{'action':'VC1b_sparse_finite_field_membership','outcome':'-+','conclusion':'VC1b_sparse_budget_obstructed'},'invalidated_continuation':['VC1c_exact_rational_reconstruction','VC1d_support_boundary_audit'],'VC1_parent':'unresolved beyond the tested minimal pole budget','policy':{'first_action':v.first_action,'success':v.success,'expected_future_cost':v.expected_cost},'passed':True};(R/'research/conjecture_replay/results/post_VC1b_replan.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
