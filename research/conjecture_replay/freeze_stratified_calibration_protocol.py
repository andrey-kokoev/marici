#!/usr/bin/env python3
"""NET2: freeze action-kind strata and a leakage-free future holdout protocol."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[2];src=json.loads((R/'research/conjecture_replay/results/branch_probability_calibration.json').read_text());O=('++','+-','-+','--')
kind={'VA1':'typing','VA2':'census','mixed_log_Betti':'physical_descent','VC1b':'algebraic_membership','VC2b':'typing','VC2b0':'interface_construction','VC2b1':'interface_construction','VC2b1a':'interface_construction','VC2b2':'algebraic_membership','VC2e':'algebraic_membership'}
rows=[]
for r in src['records']:rows.append({**r,'kind':kind[r['action']]})
strata={}
for r in rows:
 x=strata.setdefault(r['kind'],{'count':0,'outcomes':{o:0 for o in O}});x['count']+=1;x['outcomes'][r['outcome']]+=1
protocol={'assignment_rule':'action kind is declared in the immutable action contract before execution','training_rule':'first 8 admitted resolutions per stratum','holdout_rule':'next 4 admitted resolutions per stratum; predictions committed before evidence is opened','scoring':['multiclass Brier','log loss'],'promotion':'hierarchical model replaces uniform only if both aggregate holdout scores improve and no stratum Brier worsens by more than 0.05','minimum_complete_strata':2,'no_relabeling':'kind labels cannot change after outcome resolution; corrections require a topology event and restart that stratum holdout'}
protocol_digest=hashlib.sha256(json.dumps(protocol,sort_keys=True).encode()).hexdigest()
checks={'all_records_typed':len(rows)==len(src['records']),'five_strata':len(strata)==5,'no_stratum_training_ready':all(x['count']<8 for x in strata.values()),'protocol_digest_frozen':len(protocol_digest)==64,'outcomes_complete':all(set(x['outcomes'])==set(O) for x in strata.values())};assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.stratified-calibration-protocol.v1','prospective_action':'NET2_freeze_stratified_holdout','historical_inventory':rows,'strata':strata,'protocol':protocol,'protocol_digest':protocol_digest,'resolution':'++','interface_added':'prospective_stratified_calibration_registry','current_disposition':'Protocol is frozen, but no stratum has eight training observations; reliability calibration must accumulate prospectively rather than refit these ten records.','next_operational_rule':'For every future action, record kind and four-way prediction before execution, then append outcome without changing the prediction.','checks':checks,'passed':True};(R/'research/conjecture_replay/results/stratified_calibration_protocol.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'++','strata':{k:v['count'] for k,v in strata.items()},'digest':protocol_digest}))
