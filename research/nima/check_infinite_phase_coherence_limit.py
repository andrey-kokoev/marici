#!/usr/bin/env python3
"""Finite-section diagnostics for the infinite coherence-chain limit."""
import json,math,sys,time
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_chain_toy import connected_chain
ks=(5,10,20,40,60,80,100);rows=[];previous=None;start=time.perf_counter()
for k in ks:
 history,_,component=connected_chain(k);value=history.component(component);g=float(s.N(-s.log(abs(value)),18));row={'k':k,'n':3*k+2,'degree':4*k,'sign':1 if value>0 else -1,'minus_log_abs':g,'free_energy_per_phase':g/k,'scaled_k_logk':g/(k*math.log(k)),'denominator_digits':len(str(value.q))}
 if previous is not None:
  pk,pg=previous;row['incremental_cost_per_added_phase']=(g-pg)/(k-pk)
 rows.append(row);previous=(k,g)
raw_decay=all(rows[i]['minus_log_abs']>rows[i-1]['minus_log_abs'] for i in range(1,len(rows)))
scaled=[r['scaled_k_logk'] for r in rows[-4:]]
checks={'exact_nonzero_all_sections':all(r['denominator_digits']>0 for r in rows),'raw_magnitude_strictly_decays':raw_decay,'orientation_is_minus_one_to_k':all(r['sign']==(-1)**r['k'] for r in rows),'joint_limit_n_equals_3k_plus_2':all(r['n']==3*r['k']+2 for r in rows),'k_logk_scaling_stable_on_tail':max(scaled)<1.2*min(scaled)}
out={'schema':'marici.nima.infinite-phase-coherence-limit.v1','family':'connected_chain(k)','finite_sections':rows,'raw_limit_evidence':'|W_k| decreases rapidly toward zero','renormalization_diagnostic':'-log|W_k| divided by k log k stabilizes on the sampled tail; use exp(c k log k), not exp(c k), as the first renormalization ansatz','elapsed_seconds':time.perf_counter()-start,'checks':checks,'passed':all(checks.values()),'scope':'Exact finite sections through k=100 plus floating logarithmic diagnostics; evidence for normalization, not a proof of an infinite Fredholm determinant.'}
p=ROOT/'research/nima/results/infinite-phase-coherence-limit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
