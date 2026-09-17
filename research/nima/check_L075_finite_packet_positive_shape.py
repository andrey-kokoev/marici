#!/usr/bin/env python3
"""Promote the completed directed rank-1000 L=.75 residual to a finite-packet Schur certificate."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research/voevodsky/results';N=ROOT/'research/nima/results'
def load(n):return json.loads((V/n).read_text())
crit=load('L075_critical_degree149_arb.json');gap=load('L075_uniform_complement_gap.json');agg=load('L075_directed_residual_chunk_aggregate.json');tol=load('L075_residual_norm_tolerance.json');tail=load('L075_directed_tail_component_ledger.json')
# Published interval lower endpoint from the directed critical-form artifact.
a=tol['directed_candidate_lower'];alpha=tol['complement_floor'];r=agg['partial_norm_upper'];schur=a-r*r/alpha
checks={'critical_form_directed':crit['passed'],'complement_floor_positive':alpha>0,'all_rank1000_residual_modes_directed':agg['full_residual_certified'] and agg['remaining_even_modes']==0,'rank1000_residual_below_positive_threshold':r<tol['maximum_residual_norm_for_positivity'],'rank1000_schur_lower_positive':schur>0,'infinite_tail_fully_certified':tail['full_tail_passed']}
out={'schema':'marici.nima.L075-finite-packet-positive-shape.v1','packet':{'support_radius':.75,'critical_degree':149,'directed_residual_stop':1000},'schur_data':{'critical_lower':a,'complement_floor':alpha,'directed_residual_upper':r,'schur_lower':schur,'residual_threshold':tol['maximum_residual_norm_for_positivity']},'checks':checks,'finite_rank1000_packet_positive':all(v for k,v in checks.items() if k!='infinite_tail_fully_certified'),'completed_infinite_packet_positive':all(checks.values()),'remaining_tail_reserve':tail['reserve_for_thrice_continuous_remainder'],'remaining_obligation':tail['remaining_obligation'],'rh_proved':False,'passed':all(v for k,v in checks.items() if k!='infinite_tail_fully_certified')}
p=N/'L075-finite-packet-positive-shape.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
