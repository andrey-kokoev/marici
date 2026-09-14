#!/usr/bin/env python3
"""Retrospective success-first policy synthesis with an interpretation state."""
import functools,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]
q=json.loads((R/'research/conjecture_replay/results/del_pezzo_typed_quiver.json').read_text())
c=json.loads((R/'research/conjecture_replay/results/del_pezzo_cost_model.json').read_text())
A=q['adjacency'];states=['++','+-','-+','--'];eps=.05
bits={'M':1,'E':2,'L':4,'P':8};READY=15

def updated(action,outcome,state):
 if outcome!='++':return state
 return state|({'DP1':bits['M'],'DP7':bits['M'],'DP2':bits['E'],'DP4':bits['L'],'DP5':bits['P']}.get(action,0))
def aggregate(xs,mode):
 if mode=='optimistic':return max(xs)
 if mode=='expected':return sum(xs)/4
 if mode=='minimax':return min(xs)
 if mode=='credal_worst':return eps*sum(xs)+(1-4*eps)*min(xs)
 raise ValueError(mode)

def solve(costs,mode):
 @functools.lru_cache(None)
 def V(node,used_tuple,state):
  if node.startswith('T_'):return (1.0 if node=='T_readout' else 0.0),0.0
  used=set(used_tuple);successes=[];downcosts=[]
  for outcome in states:
   ns=updated(node,outcome,state);opts=[]
   for target in A[node][outcome]:
    # A favorable raw physical result without the interpretation interface is partial.
    effective='T_partial' if node=='DP6' and outcome=='++' and ns!=READY else target
    if effective not in used:
     s,k=V(effective,tuple(sorted(used|{effective})),ns);opts.append((s,-k,effective,k))
   if not opts:opts=[(0.0,0.0,'dead',0.0)]
   best=max(opts,key=lambda x:(x[0],x[1],x[2]));successes.append(best[0]);downcosts.append(best[3])
  return aggregate(successes,mode),costs[node]+sum(downcosts)/4
 roots=[]
 for first in A['O']['*']:
  s,k=V(first,tuple(sorted({'O',first})),0);roots.append({'first_action':first,'readout_success':s,'expected_action_cost':k})
 best=max(roots,key=lambda x:(x['readout_success'],-x['expected_action_cost'],x['first_action']))
 return {'best_first_action':best['first_action'],'readout_success':best['readout_success'],'expected_action_cost':best['expected_action_cost'],'root_candidates':sorted(roots,key=lambda x:(-x['readout_success'],x['expected_action_cost'],x['first_action']))}
scenarios={name:{a:v['scenario_costs'][name] for a,v in c['prior_cost_model']['conjectures'].items()} for name in c['prior_cost_model']['scenario_weights']}
solutions={s:{m:solve(costs,m) for m in ['optimistic','expected','minimax','credal_worst']} for s,costs in scenarios.items()}
checks={'historical_first_recovered_expected':solutions['balanced']['expected']['best_first_action']=='DP1','optimistic_has_successful_branch':solutions['balanced']['optimistic']['readout_success']==1,'direct_DP6_zero_success':all(next(x for x in z['root_candidates'] if x['first_action']=='DP6')['readout_success']==0 for y in solutions.values() for z in y.values()),'no_guaranteed_policy':all(y['minimax']['readout_success']==0 for y in solutions.values()),'positive_expected_policy':all(y['expected']['readout_success']>0 for y in solutions.values())}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.del-pezzo-stateful-policies.v1','status':'retrospective reconstructed model','readiness_bits':bits,'readout_guard':'M&E&L&P','objective':'lexicographically maximize readout success under the risk functional, then minimize expected action cost','solutions':solutions,'interpretation':{'optimistic':'existence of a successful outcome branch','expected':'uniform expected readout probability','minimax':'guaranteed readout probability','credal_worst':'lower readout probability over epsilon-credal distributions'},'checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/del_pezzo_stateful_policies.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'balanced':{m:{k:v[k] for k in ['best_first_action','readout_success','expected_action_cost']} for m,v in solutions['balanced'].items()}}))
