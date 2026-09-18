#!/usr/bin/env python3
"""Estimate the extensive counterterm from exact one-phase transfer costs."""
import json,math,sys,time
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_chain_toy import connected_chain
sample=(50,100,150,200,250,300);rows=[];start=time.perf_counter()
def action(k):
 h,_,c=connected_chain(k);v=h.component(c);return float(s.N(-s.log(abs(v)),18))
for k in sample:
 gm=action(k-1);g=action(k);leading=6*(k*math.log(k)-(k-1)*math.log(k-1));d=g-gm-leading;rows.append({'k':k,'transfer_action':g-gm,'leading_k6k_transfer':leading,'residual_d_k':d})
# Least-squares extrapolation d_k = d_infinity + a/k on the last four sections.
tail=rows[-4:];xs=[1/r['k'] for r in tail];ys=[r['residual_d_k'] for r in tail];xm=sum(xs)/len(xs);ym=sum(ys)/len(ys);a=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sum((x-xm)**2 for x in xs);dinf=ym-a*xm
for r in rows:r['renormalized_log_transfer']=dinf-r['residual_d_k'];r['renormalized_transfer_ratio']=math.exp(r['renormalized_log_transfer'])
errors=[abs(r['renormalized_transfer_ratio']-1) for r in tail]
checks={'residual_transfer_cost_decreases':all(rows[i]['residual_d_k']<rows[i-1]['residual_d_k'] for i in range(1,len(rows))),'positive_finite_extrapolated_d':0<dinf<20,'renormalized_transfer_approaches_one':errors[-1]<errors[0] and errors[-1]<0.02,'exact_sections_through_300':rows[-1]['k']==300}
out={'schema':'marici.nima.infinite-phase-second-renormalization.v1','leading_counterterm':'k^(6k)','transfer_sections':rows,'fit_model':'d_k=d_infinity+a/k on k=150,200,250,300','d_infinity_estimate':dinf,'exp_d_estimate':math.exp(dinf),'one_over_k_coefficient':a,'renormalized_weight':'(-1)^k k^(6k) exp(d_infinity k) W_k','elapsed_seconds':time.perf_counter()-start,'checks':checks,'passed':all(checks.values()),'scope':'Exact finite sections with floating transfer diagnostics and a 1/k extrapolation; numerical evidence, not a proof of the infinite limit.'}
p=ROOT/'research/nima/results/infinite-phase-second-renormalization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
