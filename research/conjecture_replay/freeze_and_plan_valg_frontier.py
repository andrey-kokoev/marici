#!/usr/bin/env python3
"""Prospectively freeze and rank the unresolved v_alg tomography frontier."""
import hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from interpretation_planner import Action,Branch,Decoder,Effect,Planner,State,OUTCOMES
sources=[
'research/voevodsky/results/C1_integral_e6_replay.json',
'research/voevodsky/results/C10_all_sourced_corner_projection_rank.json',
'research/voevodsky/results/C15_canonical_physical_mixed_detector.json',
'research/voevodsky/results/exchange_odd_response_GM_lift_audit.json',
'research/benincasa/physical-normal-lift-cech-coherence.json',
'research/benincasa/results/relative-shape-pole-depth.json']
def rec(s):
 p=R/s;b=p.read_bytes();return {'path':s,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
freeze=[rec(x) for x in sources]
def action(name,cost,requires=(),adds=(),raw=None):
 return Action(name,cost,frozenset(requires),{s:Branch(.25,Effect(add=frozenset(adds) if s=='++' else frozenset(),raw=raw if s=='++' else None)) for s in OUTCOMES})
initial=State(frozenset({'current_v_alg_frontier'}),frozenset({'marked_extension','primitive_e6','physical_e6','wall_horizontal_GM_class'}))
actions=[
 action('VA1_GM_IBP_simple_residue',8,['marked_extension','wall_horizontal_GM_class'],['physical_valg_channel']),
 action('VA2_alternative_discriminant_census',13,['marked_extension','physical_e6'],['physical_valg_channel']),
 action('VA3_integral_valg_normalization',7,['physical_valg_channel'],['integral_valg']),
 action('VA4_two_channel_Smith_validation',3,['physical_e6','physical_valg_channel','integral_valg'],raw='rank_two_integral_tomography')]
decoder=Decoder('VA4_two_channel_Smith_validation','rank_two_integral_tomography',frozenset({'physical_e6','physical_valg_channel','integral_valg'}),'two_channel_physical_readout')
planner=Planner(actions,[decoder],decoder.target);v=planner.solve_expected(initial)
# Ablations establish that the recommendation comes from interface structure.
without_gm=planner.solve_expected(State(initial.hypotheses,initial.interfaces-{'wall_horizontal_GM_class'}))
without_marked=planner.solve_expected(State(initial.hypotheses,initial.interfaces-{'marked_extension'}))
checks={'all_sources_frozen':len(freeze)==6,'current_packets_pass':all(json.loads((R/x).read_text()).get('passed',json.loads((R/x).read_text()).get('all_checks_pass',True)) for x in sources),'VA1_ranked_first':v.first_action=='VA1_GM_IBP_simple_residue','without_GM_uses_alternative':without_gm.first_action=='VA2_alternative_discriminant_census','without_marking_no_success':without_marked.success==0,'nonzero_prospective_success':v.success>0}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.prospective-v-alg-frontier.v1','frozen_at_utc':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),'objective':'construct a primitive physical v_alg channel and validate rank-two Smith tomography with the established e6 channel','source_freeze':freeze,'initial_interfaces':sorted(initial.interfaces),'actions':[{'name':a.name,'cost':a.cost,'requires':sorted(a.requires),'++_adds':sorted(a.branches['++'].effect.add),'++_raw':a.branches['++'].effect.raw} for a in actions],'decoder':{'experiment':decoder.experiment,'raw':decoder.raw,'requires':sorted(decoder.requires),'target':decoder.target},'prospective_policy':{'first_action':v.first_action,'success_probability_under_uninformative_model':v.success,'expected_cost_with_abandonment':v.expected_cost},'ablations':{'without_GM_interface':{'first_action':without_gm.first_action,'success':without_gm.success},'without_marked_extension':{'first_action':without_marked.first_action,'success':without_marked.success}},'commitment':'Before observing any new outcome, execute VA1: apply the global contact-weighted Gauss-Manin adapter to the six-term relative-shape jet, perform IBP/simple-residue lowering, and project onto g101-g110.','outcome_contract':{'++':'nonzero intrinsic antisymmetric simple-residue component; construct integral normalization next','+-':'simple residue survives but has zero v_alg projection; move to alternative discriminant census','-+':'covariant response reduces to zero in the mixed quotient; reject this shape channel','--':'reduction cannot yet be completed or typed; repair the reduction interface before inference'},'checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/prospective_valg_frontier.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'first':v.first_action,'success':v.success,'expected_cost':v.expected_cost,'without_GM_first':without_gm.first_action,'commitment':out['commitment']}))
