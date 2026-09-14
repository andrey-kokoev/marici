#!/usr/bin/env python3
"""Probability and credal models for four-way conjecture resolutions."""
import json,math
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parents[2]
typed=json.loads((R/'research/conjecture_replay/results/del_pezzo_typed_quiver.json').read_text())
hold=json.loads((R/'research/conjecture_replay/results/del_pezzo_holdout_sequence.json').read_text())
cost=json.loads((R/'research/conjecture_replay/results/del_pezzo_cost_model.json').read_text())
states=['++','+-','-+','--'];ids=[x['id'] for x in typed['typed_conjectures']]
# Policy-safe models available at the entrance.
uniform={q:{s:.25 for s in states} for q in ids}
# Imprecise prior: every outcome has at least epsilon mass. Its vertices put all
# remaining mass on one outcome. This supports exact best/worst expectations.
eps=.05
credal={q:{'lower':{s:eps for s in states},'upper':{s:1-3*eps for s in states},'constraint':'sum(p_sigma)=1'} for q in ids}
# Holdout-only empirical model. DP8 is censored because no dedicated post-entry
# observation was recorded. Leave-one-out prevents scoring a label on itself.
observed={q:v['relation'] for q,v in hold['final_retrospective_dispositions'].items() if q!='DP8'}
loo={};alpha=1
for q,y in observed.items():
 counts=Counter(v for k,v in observed.items() if k!=q);den=(len(observed)-1)+alpha*len(states)
 loo[q]={s:(counts[s]+alpha)/den for s in states}
# Full retrospective posterior predictive, descriptive only.
counts=Counter(observed.values());den=len(observed)+4*alpha
posterior={s:(counts[s]+alpha)/den for s in states}
def scores(pred,truth):
 return {'log_loss':-math.log(pred[truth]),'brier':sum((pred[s]-(1 if s==truth else 0))**2 for s in states),'truth_probability':pred[truth]}
cal={'uniform':[],'empirical_leave_one_out':[]}
for q,y in observed.items():
 cal['uniform'].append({'id':q,**scores(uniform[q],y)})
 cal['empirical_leave_one_out'].append({'id':q,**scores(loo[q],y)})
summary={k:{'mean_log_loss':sum(x['log_loss'] for x in xs)/len(xs),'mean_brier':sum(x['brier'] for x in xs)/len(xs)} for k,xs in cal.items()}
# Probability of a conclusive resolution treats -- as inconclusive; probability
# of full advertised success is the ++ mass. Keep these distinct.
derived={'uniform':{q:{'advertised_success':uniform[q]['++'],'conclusive_resolution':1-uniform[q]['--']} for q in ids},'credal_bounds':{q:{'advertised_success':[eps,1-3*eps],'conclusive_resolution':[3*eps,1-eps]} for q in ids}}
checks={'all_nodes_uniform':set(uniform)==set(ids),'uniform_normalized':all(abs(sum(p.values())-1)<1e-12 for p in uniform.values()),'credal_nonempty':4*eps<=1,'loo_normalized':all(abs(sum(p.values())-1)<1e-12 for p in loo.values()),'DP8_censored':'DP8' not in observed and 'DP8' not in loo,'seven_scored':all(len(v)==7 for v in cal.values()),'probability_cost_separation':set(cost['prior_cost_model']['conjectures'])==set(ids)}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.del-pezzo-probability-model.v1','states':states,'policy_safe':{'uninformative':uniform,'robust_credal':credal,'warning':'The credal epsilon is a sensitivity parameter, not an empirical frequency.'},'holdout_only':{'observed_final_relations':observed,'dirichlet_alpha':alpha,'leave_one_out':loo,'posterior_predictive':posterior,'calibration_events':cal,'calibration_summary':summary,'warning':'Retrospective empirical distributions may score policies but may not construct the entrance policy.'},'derived_probabilities':derived,'checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/del_pezzo_probability_model.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'observed_counts':counts,'posterior':posterior,'calibration':summary,'credal_epsilon':eps}))
