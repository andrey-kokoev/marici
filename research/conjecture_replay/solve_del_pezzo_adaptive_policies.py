#!/usr/bin/env python3
"""Solve finite adaptive policies under four risk functionals."""
import functools,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]
q=json.loads((R/'research/conjecture_replay/results/del_pezzo_typed_quiver.json').read_text())
c=json.loads((R/'research/conjecture_replay/results/del_pezzo_cost_model.json').read_text())
p=json.loads((R/'research/conjecture_replay/results/del_pezzo_probability_model.json').read_text())
A=q['adjacency'];states=p['states'];probs=p['policy_safe']['uninformative'];eps=.05
terminal_loss={'T_readout':0.0,'T_partial':40.0,'T_rejected':60.0,'T_unresolved':80.0}

def solve(costs,mode,loss_scale=1.0):
 @functools.lru_cache(None)
 def V(node,used_tuple):
  if node.startswith('T_'): return loss_scale*terminal_loss[node],{'terminal':node}
  used=set(used_tuple);vals=[];branches={}
  for outcome in states:
   opts=[]
   for target in A[node][outcome]:
    if target not in used:
     val,sub=V(target,tuple(sorted(used|{target})));opts.append((val,target,sub))
   if not opts:return math.inf,{'dead_at':node,'outcome':outcome}
   best=min(opts,key=lambda x:(x[0],x[1]));vals.append(best[0]);branches[outcome]={'next':best[1],'continuation_value':best[0],'policy':best[2]}
  if mode=='optimistic':future=min(vals)
  elif mode=='expected':future=sum(probs[node][s]*v for s,v in zip(states,vals))
  elif mode=='minimax':future=max(vals)
  elif mode=='credal_worst':future=eps*sum(vals)+(1-4*eps)*max(vals)
  else:raise ValueError(mode)
  return costs[node]+future,{'action':node,'action_cost':costs[node],'outcome_continuations':branches,'aggregate_future':future}
 roots=[]
 for first in A['O']['*']:
  val,tree=V(first,tuple(sorted({'O',first})));roots.append({'first_action':first,'value':val,'policy':tree})
 best=min(roots,key=lambda x:(x['value'],x['first_action']))
 return {'best_first_action':best['first_action'],'value':best['value'],'root_candidates':[{k:v for k,v in x.items() if k!='policy'} for x in sorted(roots,key=lambda x:(x['value'],x['first_action']))],'policy_tree':best['policy']}

scenarios={name:{a:v['scenario_costs'][name] for a,v in c['prior_cost_model']['conjectures'].items()} for name in c['prior_cost_model']['scenario_weights']}
solutions={}
for scenario,costs in scenarios.items():
 solutions[scenario]={mode:solve(costs,mode) for mode in ['optimistic','expected','minimax','credal_worst']}
sensitivity={str(scale):{scenario:{mode:solve(costs,mode,scale)['best_first_action'] for mode in ['expected','minimax','credal_worst']} for scenario,costs in scenarios.items()} for scale in [.25,1,5,20]}
all_best=[v['best_first_action'] for x in solutions.values() for v in x.values()]
checks={'all_scenarios':set(solutions)==set(scenarios),'all_modes':all(set(x)=={'optimistic','expected','minimax','credal_worst'} for x in solutions.values()),'finite_values':all(math.isfinite(v['value']) for x in solutions.values() for v in x.values()),'direct_DP6_dominates':set(all_best)=={'DP6'},'loss_sensitivity_stable':all(a=='DP6' for x in sensitivity.values() for y in x.values() for a in y.values()),'uniform_probabilities':all(set(x.values())=={.25} for x in probs.values())}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.del-pezzo-adaptive-policies.v1','objective':'minimize action costs plus terminal loss','terminal_loss':terminal_loss,'risk_functionals':{'optimistic':'min over outcome continuations','expected':'uniform expectation','minimax':'maximum outcome continuation','credal_worst':'epsilon sum plus remaining mass on maximum continuation'},'solutions':solutions,'terminal_loss_scale_sensitivity':sensitivity,'diagnosis':'All policies choose DP6 directly because the model assigns outcome-independent probabilities and no continuation-value update from resolving structural conjectures. Preliminary experiments add cost without changing DP6 outcomes.','model_gap':'A hypothesis space linking structural outcomes to physical-readout probabilities is required for information to have option value.','checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/del_pezzo_adaptive_policies.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'best':{s:{m:x['best_first_action'] for m,x in z.items()} for s,z in solutions.items()},'values':{s:{m:round(x['value'],3) for m,x in z.items()} for s,z in solutions.items()},'diagnosis':out['diagnosis']}))
