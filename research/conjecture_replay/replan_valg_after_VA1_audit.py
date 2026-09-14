#!/usr/bin/env python3
"""Replan the v_alg frontier after exposing the absent IBP interface."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from interpretation_planner import Action,Branch,Decoder,Effect,Planner,State,OUTCOMES
def action(name,cost,requires=(),adds=(),raw=None):
 return Action(name,cost,frozenset(requires),{s:Branch(.25,Effect(add=frozenset(adds) if s=='++' else frozenset(),raw=raw if s=='++' else None)) for s in OUTCOMES})
initial=State(frozenset({'current_v_alg_frontier'}),frozenset({'marked_extension','primitive_e6','physical_e6','wall_horizontal_GM_class'}))
actions=[
 action('VA0_construct_filtered_IBP_lowering',12,['wall_horizontal_GM_class'],['filtered_IBP_lowering']),
 action('VA1_apply_lowering_and_project',8,['marked_extension','filtered_IBP_lowering'],['physical_valg_channel']),
 action('VA2_alternative_discriminant_census',13,['marked_extension','physical_e6'],['physical_valg_channel']),
 action('VA3_integral_valg_normalization',7,['physical_valg_channel'],['integral_valg']),
 action('VA4_two_channel_Smith_validation',3,['physical_e6','physical_valg_channel','integral_valg'],raw='rank_two_integral_tomography')]
d=Decoder('VA4_two_channel_Smith_validation','rank_two_integral_tomography',frozenset({'physical_e6','physical_valg_channel','integral_valg'}),'two_channel_physical_readout')
v=Planner(actions,[d],d.target).solve_expected(initial)
checks={'repaired_action_requires_lowering':next(a for a in actions if a.name.startswith('VA1_')).requires==frozenset({'marked_extension','filtered_IBP_lowering'}),'VA0_constructs_missing_interface':next(a for a in actions if a.name.startswith('VA0_')).branches['++'].effect.add==frozenset({'filtered_IBP_lowering'}),'replanned_away_from_ill_typed_VA1':v.first_action!='VA1_apply_lowering_and_project','alternative_ranked_first':v.first_action=='VA2_alternative_discriminant_census'}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.replanned-v-alg-frontier.v1','supersedes_policy_only':'prospective_valg_frontier.json; its hash freeze and failed prediction remain immutable evidence','first_action':v.first_action,'success_probability_under_uniform_model':v.success,'expected_cost_with_abandonment':v.expected_cost,'actions':[{'name':a.name,'cost':a.cost,'requires':sorted(a.requires),'++_adds':sorted(a.branches['++'].effect.add)} for a in actions],'interpretation':'Once construction of the absent lowering interface is priced as its own uncertain action, the alternative physical discriminant census has greater expected option value.','commitment':'Execute VA2 by enumerating source-admissible physical operations outside the frozen total-energy/Cut corner family and test their projections onto the v_alg tail.','checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/replanned_valg_frontier.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'first':v.first_action,'success':v.success,'expected_cost':v.expected_cost,'commitment':out['commitment']}))
