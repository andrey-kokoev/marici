#!/usr/bin/env python3
"""Replay the holdout and infer the minimal structural-readout coupling."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
h=json.loads((R/'research/conjecture_replay/results/del_pezzo_holdout_sequence.json').read_text())
c=json.loads((R/'research/conjecture_replay/results/del_pezzo_cost_model.json').read_text())
a=json.loads((R/'research/conjecture_replay/results/del_pezzo_adaptive_policies.json').read_text())
# First appearance of each programme in the holdout, preserving actual order.
first={};
for e in h['events']: first.setdefault(e['primary_conjecture'],e['sequence'])
programme=['DP1','DP2','DP4','DP5','DP6']
assert [first[x] for x in programme]==sorted(first[x] for x in programme)
relations=h['final_retrospective_dispositions']
word=[f"{x}:{relations[x]['relation']}" for x in programme]
prior=c['prior_cost_model']['conjectures'];historical_prior_cost={s:sum(prior[x]['scenario_costs'][s] for x in programme) for s in c['prior_cost_model']['scenario_weights']}
# First upstream physical-incidence success is packet 10; packet 33 gives the
# final explicit corner functional. Both are reported rather than conflated.
actual_events=c['retrospective_cost_model']['events']
def cumulative(n):return round(sum(x['static_cost_proxy'] for x in actual_events if x['sequence']<=n),6)
root=a['solutions']['balanced']['expected']['root_candidates'];predicted_rank=next(i+1 for i,x in enumerate(root) if x['first_action']=='DP1')
# Minimal state variables needed to make structural work affect readout value.
coupling={'state_bits':{
'M':'global invariant marking available: DP1++ or DP7++',
'E':'source e6 placed in that marking: DP2++',
'L':'integral saturation/normalization known: DP4 conclusive',
'P':'mod-two geometric labels known: DP5 conclusive'},
'raw_DP6_executable':'always',
'interpretable_DP6_readout_guard':'M and E and L and P',
'outcome_transport':'If the guard is false, a raw DP6 ++ observation terminates at T_partial rather than T_readout.',
'probability_dependency':'P(T_readout | DP6++, state)=1 when M&E&L&P, else 0',
'justification':'The holdout reaches raw degeneration at packet 5, but obtains marked physical incidence only after the structural vocabulary has been constructed.'}
checks={'historical_programme_order':word==['DP1:++','DP2:++','DP4:++','DP5:++','DP6:++'],'old_policy_predicted_direct':a['solutions']['balanced']['expected']['best_first_action']=='DP6','historical_first_action_DP1':min(first,key=first.get)=='DP1','DP1_old_expected_rank':predicted_rank>1,'coupling_has_four_bits':len(coupling['state_bits'])==4,'packet10_before_explicit_packet33':10<33}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.del-pezzo-replay-and-coupling.v1','correction':'Final relations are scored against each conjecture statement, not against the stronger eventual two-channel objective. DP4, DP5, and DP6 are therefore ++.','historical_programme':{'actions':programme,'typed_word':word,'prior_cost_by_scenario':historical_prior_cost,'first_upstream_physical_incidence_packet':10,'first_upstream_cumulative_static_proxy':cumulative(10),'explicit_corner_readout_packet':33,'explicit_corner_cumulative_static_proxy':cumulative(33)},'old_policy':{'balanced_expected_first':'DP6','historical_first':'DP1','historical_first_rank_under_old_policy':predicted_rank,'diagnosis':'The old policy calls raw executability terminal success and therefore undervalues the marking needed to interpret the output.'},'minimum_hypothesis_coupling':coupling,'regret_disposition':'Scalar cost regret is undefined for the old direct policy because its DP6 output lacks the interpretation guard. It is a type failure, not merely a more expensive success.','checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/del_pezzo_replay_and_coupling.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'word':word,'historical_prior_cost':historical_prior_cost,'old_DP1_rank':predicted_rank,'cumulative_proxy_packet10':cumulative(10),'cumulative_proxy_packet33':cumulative(33),'guard':coupling['interpretable_DP6_readout_guard']}))
