#!/usr/bin/env python3
"""Admit the VC1 symbolic timeout as telemetry and replan implementation strategy."""
import json,sys
from datetime import datetime,timezone
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from interpretation_planner import Action,Branch,Decoder,Effect,Implication,Planner,Proposition,State,OUTCOMES
telemetry={'schema':'marici.conjecture-replay.execution-telemetry.v1','recorded_at_utc':datetime.now(timezone.utc).isoformat(),'action':'VC1a_symbolic_expanded_image_test','parent_action':'VC1_controlled_rational_primitive_enlargement','status':'timeout','timeout_seconds':300,'second_attempt':'operator-aborted; elapsed time not admitted','normalized_cost_units':5.0,'normalization':'one cost unit = 60 seconds of wall time for this replan','effects':{'add':['VC1a_symbolic_implementation_infeasible'],'does_not_add':['VC1_pole_budget_obstructed','filtered_IBP_lowering']},'interpretation':'implementation failure only; VC1 mathematical outcome remains unresolved'}
(R/'research/conjecture_replay/results/VC1a_execution_telemetry.json').write_text(json.dumps(telemetry,indent=2)+'\n')
def action(name,cost,requires,success_add):
 branches={}
 for o in OUTCOMES:
  add=frozenset(success_add if o=='++' else {f'{name}:{o}'})
  conclusion=next(iter(add));imp=Implication(Proposition('branch',(name,o),scope='action-resolution'),'entails',Proposition(conclusion,scope='planner-interface'),'admitted checker result')
  branches[o]=Branch(.25,Effect(add=add),(imp,))
 return Action(name,cost,frozenset(requires),branches)
actions=[
 action('VC1b_sparse_finite_field_membership',3,['VC1a_symbolic_implementation_infeasible'],{'VC1_bounded_membership'}),
 action('VC1c_exact_rational_reconstruction',8,['VC1_bounded_membership'],{'VC1_exact_lowering'}),
 action('VC1d_support_boundary_audit',5,['VC1_exact_lowering'],{'filtered_IBP_lowering'}),
 action('VC2_multistage_relative_primitive_complex',14,['local_IBP_core'],{'filtered_IBP_lowering'}),
 action('VC3_apply_lowering_and_project',4,['filtered_IBP_lowering','physical_odd_shape_response'],{'physical_valg_channel'}),
 action('VC4_integral_normalization',7,['physical_valg_channel'],{'integral_valg'}),
 action('VC5_Smith_validation',3,['integral_valg','physical_e6'],{'two_channel_physical_readout'}),]
initial=State(frozenset(),frozenset({'VC1a_symbolic_implementation_infeasible','local_IBP_core','physical_odd_shape_response','physical_e6','marked_extension'}))
dec=Decoder('VC5_Smith_validation',None,frozenset({'two_channel_physical_readout'}),'two_channel_physical_readout')
v=Planner(actions,[dec],dec.target,require_implications=True).solve_expected(initial)
checks={'timeout_cost_admitted':telemetry['normalized_cost_units']==5,'mathematical_VC1_unresolved':'VC1_pole_budget_obstructed' not in initial.interfaces,'symbolic_route_invalidated':'VC1a_symbolic_implementation_infeasible' in initial.interfaces,'sparse_route_available':actions[0].available(initial),'recommendation_is_defined':v.first_action in {'VC1b_sparse_finite_field_membership','VC2_multistage_relative_primitive_complex'}};assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.post-timeout-v-alg-replan.v1','sunk_cost':{'action':telemetry['action'],'units':5,'status':'timeout'},'current_interfaces':sorted(initial.interfaces),'candidate_actions':[{'name':a.name,'cost':a.cost,'requires':sorted(a.requires)} for a in actions],'policy':{'first_action':v.first_action,'success_probability_under_uniform_branch_prior':v.success,'expected_future_cost_with_abandonment':v.expected_cost},'recommendation':'Execute VC2_multistage_relative_primitive_complex first. The model prefers its shorter success chain over VC1b -> VC1c -> VC1d; retain VC1b sparse finite-field membership as the fallback and never rerun VC1a.','warning':'Costs for unexecuted actions remain engineering estimates; branch probabilities remain uncalibrated bookkeeping priors.','checks':checks,'passed':True}
(R/'research/conjecture_replay/results/post_timeout_valg_replan.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'sunk_cost':5,'first':v.first_action,'success':v.success,'future_cost':v.expected_cost,'recommendation':out['recommendation']}))
