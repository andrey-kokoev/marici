#!/usr/bin/env python3
"""Instantiate the generic interpretation planner at the Del Pezzo entrance."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from interpretation_planner import Action,Branch,Decoder,Effect,Planner,State,OUTCOMES
cost=json.loads((R/'research/conjecture_replay/results/del_pezzo_cost_model.json').read_text())['prior_cost_model']['conjectures']
def action(name,requires=(),adds=(),raw=None):
 branches={s:Branch(.25,Effect(add=frozenset(adds) if s=='++' else frozenset(),raw=raw if s=='++' else None)) for s in OUTCOMES}
 return Action(name,cost[name]['scenario_costs']['balanced'],frozenset(requires),branches)
actions=[
 action('DP1',adds=['M']),                         # inexpensive pencil marking
 action('DP7',adds=['M']),                         # direct Picard-marking alternative
 action('DP2',requires=['M'],adds=['E']),           # place source class in marking
 action('DP4',requires=['M','E'],adds=['L']),       # integral saturation
 action('DP5',requires=['M','L'],adds=['P']),       # geometric parity labels
 action('DP6',raw='physical_integral_class'),       # executable before interpretable
]
decoder=Decoder('DP6','physical_integral_class',frozenset({'M','E','L','P'}),'physical_readout')
planner=Planner(actions,[decoder],'physical_readout');initial=State(frozenset({'del_pezzo_models'}))
value=planner.solve_expected(initial)
# Ablation: the old model's total decoder requires no interpretation interfaces.
naive=Planner(actions,[Decoder('DP6','physical_integral_class',frozenset(),'physical_readout')],'physical_readout').solve_expected(initial)
# Type check directly: the same raw observation has different semantic status.
raw_before=decoder.decode('DP6','physical_integral_class',initial)
ready=State(initial.hypotheses,frozenset({'M','E','L','P'}));raw_after=decoder.decode('DP6','physical_integral_class',ready)
checks={'four_way_actions':all(set(a.branches)==set(OUTCOMES) for a in actions),'raw_before_undefined':raw_before is None,'raw_after_decodes':raw_after=='physical_readout','naive_selects_DP6':naive.first_action=='DP6','typed_selects_historical_DP1':value.first_action=='DP1','typed_positive_success':value.success>0,'typed_cost_finite':value.expected_cost>0}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-net.del-pezzo-generic-interpretation-planner.v1','generic_state':{'hypotheses':sorted(initial.hypotheses),'interfaces':sorted(initial.interfaces)},'actions':[{'name':a.name,'cost':a.cost,'requires':sorted(a.requires),'++_adds':sorted(a.branches['++'].effect.add),'++_raw':a.branches['++'].effect.raw} for a in actions],'decoder':{'experiment':decoder.experiment,'raw':decoder.raw,'requires':sorted(decoder.requires),'target':decoder.target},'typed_policy':{'first_action':value.first_action,'success_probability':value.success,'expected_cost':value.expected_cost},'naive_ablation':{'first_action':naive.first_action,'success_probability':naive.success,'expected_cost':naive.expected_cost},'checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/del_pezzo_generic_interpretation_planner.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'typed':out['typed_policy'],'naive':out['naive_ablation']}))
