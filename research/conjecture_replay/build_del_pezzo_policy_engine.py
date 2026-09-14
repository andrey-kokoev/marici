#!/usr/bin/env python3
"""Compile and audit the policy-safe guarded path engine."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(Path(__file__).parent))
from policy_engine import enumerate_paths,evaluate,pareto
q=json.loads((R/'research/conjecture_replay/results/del_pezzo_typed_quiver.json').read_text())
c=json.loads((R/'research/conjecture_replay/results/del_pezzo_cost_model.json').read_text())
p=json.loads((R/'research/conjecture_replay/results/del_pezzo_probability_model.json').read_text())
paths=enumerate_paths(q['adjacency']);probs=p['policy_safe']['uninformative']
scenarios={name:{a:v['scenario_costs'][name] for a,v in c['prior_cost_model']['conjectures'].items()} for name in c['prior_cost_model']['scenario_weights']}
summary={};samples={}
for name,costs in scenarios.items():
 rows=[evaluate(x,costs,probs) for x in paths]
 read=[x for x in rows if x['terminal']=='T_readout']
 cheapest=min(x['cost'] for x in read)
 cheapest_rows=[x for x in read if x['cost']==cheapest]
 # Surprisal is retained as an uncertainty/exploration coordinate, not called information gain yet.
 front=pareto(read,{'cost':'min','surprisal_bits':'max'})
 summary[name]={'path_count':len(rows),'readout_count':len(read),'minimum_readout_cost':cheapest,'minimum_readout_path_count':len(cheapest_rows),'pareto_cost_surprisal_count':len(front),'maximum_readout_surprisal_bits':max(x['surprisal_bits'] for x in read)}
 samples[name]={'minimum_readout_paths':cheapest_rows[:10],'pareto_paths':sorted(front,key=lambda x:(x['cost'],-x['surprisal_bits'],x['provenance_id']))[:25]}
ids=[x.provenance_id for x in paths]
checks={'path_count_matches_quiver':len(paths)==q['enumeration']['simple_policy_paths'],'terminal_counts_match':all(sum(x.terminal==t for x in paths)==n for t,n in q['enumeration']['terminal_counts'].items()),'provenance_ids_unique':len(ids)==len(set(ids)),'all_four_scenarios':set(summary)==set(c['prior_cost_model']['scenario_weights']),'policy_probability_is_uniform':all(set(v.values())=={0.25} for v in probs.values()),'direct_DP6_readout_present':any(r['word']==['DP6:++'] for r in samples['balanced']['minimum_readout_paths'])}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.del-pezzo-policy-engine.v1','inputs':{'quiver':'del_pezzo_typed_quiver.json','costs':'prior_cost_model only','probabilities':'policy_safe.uninformative only'},'path_identity':'SHA256 of the full ordered (action,outcome,target) sequence; no endpoint quotient','summary':summary,'samples':samples,'credal_support':{'epsilon':.05,'extreme_expectation_rule':'for four continuation values, put 0.05 on each and the remaining 0.80 on an argmin/argmax outcome'},'checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/del_pezzo_policy_engine.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'summary':summary}))
