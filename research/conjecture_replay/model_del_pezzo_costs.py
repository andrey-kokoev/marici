#!/usr/bin/env python3
"""Construct leakage-free prior costs and retrospective static realization proxies."""
import ast,hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]
hold=json.loads((R/'research/conjecture_replay/results/del_pezzo_holdout_sequence.json').read_text())
inv=json.loads((R/'research/conjecture_replay/results/del_pezzo_entrance_conjectures.json').read_text())
# Entrance-time ordinal feature estimates. Dimensions are independently useful
# resource burdens, scored 0..3 from the stated resolving experiment alone.
dims=['symbolic_algebra','integral_lattice','geometric_resolution','physical_chain','source_interface']
F={
'DP1':[3,1,1,0,0], 'DP2':[1,1,1,0,3], 'DP3':[2,3,2,0,3], 'DP4':[1,3,0,0,1],
'DP5':[1,3,1,0,2], 'DP6':[3,2,3,3,2], 'DP7':[3,3,3,0,1], 'DP8':[1,2,1,0,2]}
weights={'balanced':[1,1,1,1,1],'compute_limited':[3,2,1,1,1],'physical_risk':[1,2,2,4,3],'integrality_first':[1,4,1,1,2]}
prior={}
for c in inv['conjectures']:
 v=F[c['id']]
 prior[c['id']]={'features':dict(zip(dims,v)),'scenario_costs':{k:sum(a*b for a,b in zip(v,w)) for k,w in weights.items()},'uncertainty_interval':'[0.7*score,1.5*score]','basis':'entrance resolving-experiment text only'}
# Match each immutable result to the nearest preceding checker. This is a
# retrospective complexity proxy, not a measured runtime and not policy input.
checkers=list((R/'research/voevodsky/checkers').glob('*.py'))
def metrics(p):
 raw=p.read_bytes();text=raw.decode('utf-8');tree=ast.parse(text)
 return {'bytes':len(raw),'lines':len(text.splitlines()),'ast_nodes':sum(1 for _ in ast.walk(tree)),'sha256':hashlib.sha256(raw).hexdigest()}
actual=[]
for e in hold['events']:
 rp=R/e['artifact'];rt=rp.stat().st_mtime_ns
 candidates=[p for p in checkers if p.stat().st_mtime_ns<=rt]
 cp=max(candidates,key=lambda p:p.stat().st_mtime_ns)
 m=metrics(cp);result_bytes=rp.stat().st_size
 # Dimensionless, monotone static work proxy; no fitted holdout weights.
 proxy=round(math.log2(1+m['bytes'])+math.log2(1+m['ast_nodes'])+math.log2(1+result_bytes),6)
 actual.append({'sequence':e['sequence'],'artifact':e['artifact'],'primary_conjecture':e['primary_conjecture'],'checker':cp.relative_to(R).as_posix(),'checker_to_result_gap_seconds':round((rt-cp.stat().st_mtime_ns)/1e9,6),'checker_metrics':m,'result_bytes':result_bytes,'static_cost_proxy':proxy})
agg={}
for x in actual:
 a=agg.setdefault(x['primary_conjecture'],{'event_count':0,'static_cost_sum':0.0,'static_cost_mean':0.0})
 a['event_count']+=1;a['static_cost_sum']+=x['static_cost_proxy']
for a in agg.values():
 a['static_cost_sum']=round(a['static_cost_sum'],6);a['static_cost_mean']=round(a['static_cost_sum']/a['event_count'],6)
checks={'prior_all_nodes':set(prior)=={c['id'] for c in inv['conjectures']},'feature_bounds':all(all(0<=x<=3 for x in F[k]) for k in F),'positive_prior_costs':all(all(x>0 for x in v['scenario_costs'].values()) for v in prior.values()),'all_holdouts_costed':len(actual)==45,'checker_precedes_result':all(x['checker_to_result_gap_seconds']>=0 for x in actual),'close_checker_match':all(x['checker_to_result_gap_seconds']<120 for x in actual),'DP8_censored_from_actual': 'DP8' not in agg}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.del-pezzo-cost-model.v1','prior_cost_model':{'role':'policy input','dimensions':dims,'scenario_weights':dict(zip(weights.keys(),(dict(zip(dims,w)) for w in weights.values()))),'conjectures':prior},'retrospective_cost_model':{'role':'holdout scoring only','warning':'static source-complexity proxy, not wall-clock runtime','formula':'log2(1+checker_bytes)+log2(1+AST_nodes)+log2(1+result_bytes)','events':actual,'aggregate_by_conjecture':agg},'checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/del_pezzo_cost_model.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'prior_balanced':{k:v['scenario_costs']['balanced'] for k,v in prior.items()},'actual_aggregate':agg}))
