#!/usr/bin/env python3
"""Split VC2 into executable stages after materializing its first quotient."""
import hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from interpretation_planner import Action,Branch,Decoder,Effect,Implication,Planner,Proposition,State,OUTCOMES
stage=R/'research/benincasa/results/G12_multistage_primitive_complex_stage1.json';stage_data=json.loads(stage.read_text())
def action(name,cost,req,success):
 bs={}
 for o in OUTCOMES:
  add=frozenset(success if o=='++' else {f'{name}:{o}'})
  x=next(iter(add));imp=Implication(Proposition('branch',(name,o),scope='action-resolution'),'entails',Proposition(x,scope='planner-interface'),'prospectively frozen stage checker')
  bs[o]=Branch(.25,Effect(add=add),(imp,))
 return Action(name,cost,frozenset(req),bs)
actions=[
 action('VC2b_construct_stage2_overlap_differential',5,['VC2_stage1_quotient'],{'VC2_stage2_differential'}),
 action('VC2c_verify_exchange_and_path_coherence',3,['VC2_stage2_differential'],{'VC2_coherent_complex'}),
 action('VC2d_physical_boundary_descent',3,['VC2_coherent_complex'],{'filtered_IBP_lowering'}),
 action('VC1b_sparse_finite_field_membership',3,['VC1a_symbolic_implementation_infeasible'],{'VC1_bounded_membership'}),
 action('VC1c_exact_rational_reconstruction',8,['VC1_bounded_membership'],{'VC1_exact_lowering'}),
 action('VC1d_support_boundary_audit',5,['VC1_exact_lowering'],{'filtered_IBP_lowering'}),
 action('VC3_apply_lowering_and_project',4,['filtered_IBP_lowering','physical_odd_shape_response'],{'physical_valg_channel'}),
 action('VC4_integral_normalization',7,['physical_valg_channel'],{'integral_valg'}),
 action('VC5_Smith_validation',3,['integral_valg','physical_e6'],{'two_channel_physical_readout'}),]
initial=State(frozenset(),frozenset({'VC2_stage1_quotient','VC1a_symbolic_implementation_infeasible','local_IBP_core','physical_odd_shape_response','physical_e6','marked_extension'}))
dec=Decoder('VC5_Smith_validation',None,frozenset({'two_channel_physical_readout'}),'two_channel_physical_readout');v=Planner(actions,[dec],dec.target,require_implications=True).solve_expected(initial)
contracts={'VC2b_construct_stage2_overlap_differential':{'++':'a differential into H1 lowers the target residual filtration','+-':'a differential exists but fails support typing','-+':'target survives the enlarged stage-2 image','--':'overlap primitive domain cannot be typed'},'VC2c_verify_exchange_and_path_coherence':{'++':'all parallel lowering paths are coherently equivalent and exchange-equivariant','+-':'local coherence holds but exchange descent fails','-+':'an incompatible lowering diamond is found','--':'coherence witnesses cannot be compared'},'VC2d_physical_boundary_descent':{'++':'the coherent complex preserves the source relative cycle and exports filtered_IBP_lowering','+-':'algebraic complex exists but physical descent fails','-+':'a boundary term obstructs descent','--':'physical pairing is untyped'}}
checks={'stage1_passed':stage_data['passed'],'stage1_interface_present':'VC2_stage1_quotient' in initial.interfaces,'original_VC2_removed':all(a.name!='VC2_multistage_relative_primitive_complex' for a in actions),'three_remaining_VC2_stages':sum(a.name.startswith('VC2') for a in actions)==3,'contracts_for_each_stage':len(contracts)==3,'model_recommendation_is_available':v.first_action in {a.name for a in actions if a.available(initial)}};assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.VC2-granular-replan.v1','frozen_at_utc':datetime.now(timezone.utc).isoformat(),'stage1_evidence':{'path':str(stage.relative_to(R)).replace('\\','/'),'sha256':hashlib.sha256(stage.read_bytes()).hexdigest(),'status':'completed','accounting_cost_units':3,'cost_kind':'retrospective engineering allocation, not measured runtime'},'current_interfaces':sorted(initial.interfaces),'remaining_actions':[{'name':a.name,'cost':a.cost,'requires':sorted(a.requires)} for a in actions],'outcome_contracts':contracts,'policy':{'first_action':v.first_action,'success_probability_under_uniform_prior':v.success,'expected_future_cost':v.expected_cost},'recommendation':'Execute VC1b_sparse_finite_field_membership first. After splitting VC2 into three uncertain stages, the model prefers the cheaper three-stage VC1 continuation; VC2b remains the fallback. Do not infer coherence or physical descent from stage-1 quotient existence.','checks':checks,'passed':True}
d=R/'research/conjecture_replay/results/VC2_granular_replan.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'first':v.first_action,'success':v.success,'future_cost':v.expected_cost,'stages':['VC2b','VC2c','VC2d']}))
