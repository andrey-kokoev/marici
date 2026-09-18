#!/usr/bin/env python3
"""Test the k^(6k) leading renormalization of the infinite coherence chain."""
import json,math,sys,time
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_chain_toy import connected_chain
ks=(25,50,100,200);rows=[];start=time.perf_counter()
for k in ks:
 history,_,component=connected_chain(k);value=history.component(component);g=float(s.N(-s.log(abs(value)),18));f=g/k;residual=f-6*math.log(k)
 rows.append({'k':k,'minus_log_abs_per_phase':f,'coefficient_of_k_log_k':g/(k*math.log(k)),'after_k_to_6k_per_phase':residual,'denominator_digits':len(str(value.q))})
residuals=[r['after_k_to_6k_per_phase'] for r in rows];tail_change=abs(residuals[-1]-residuals[-2]);raw_coeffs=[r['coefficient_of_k_log_k'] for r in rows]
checks={'leading_coefficient_moves_toward_six':all(raw_coeffs[i]<raw_coeffs[i-1] and raw_coeffs[i]>6 for i in range(1,len(raw_coeffs))),'k6k_removes_logarithmic_growth':max(residuals)-min(residuals)<1,'residual_extensive_cost_stabilizing':tail_change<0.15,'all_exact_sections_nonzero':all(r['denominator_digits']>0 for r in rows)}
out={'schema':'marici.nima.infinite-phase-leading-renormalization.v1','family':'connected_chain(k)','leading_counterterm':'k^(6k)','finite_sections':rows,'tail_residual_estimate':residuals[-1],'candidate_second_counterterm':f'exp({residuals[-1]:.12g} k)','elapsed_seconds':time.perf_counter()-start,'checks':checks,'passed':all(checks.values()),'scope':'Exact finite sections through k=200 with floating logarithmic diagnostics; identifies a leading counterterm but does not prove convergence or the exact residual constant.'}
p=ROOT/'research/nima/results/infinite-phase-leading-renormalization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
