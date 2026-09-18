#!/usr/bin/env python3
"""Fit and validate the power-law counterterm of the infinite chain."""
import json,math,sys,time
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_chain_toy import connected_chain
fit_ks=(100,150,200,250,300);validation_ks=(350,400);cache={};start=time.perf_counter()
def action(k):
 if k not in cache:
  h,_,c=connected_chain(k);v=h.component(c);cache[k]=float(s.N(-s.log(abs(v)),18))
 return cache[k]
# Fit y=d*k+a*log(k)+c+b/k by linear least squares.
X=s.Matrix([[float(k),math.log(k),1.0,1.0/k] for k in fit_ks]);Y=s.Matrix([action(k)-6*k*math.log(k) for k in fit_ks]);d,a,c,b=[float(v) for v in (X.T*X).inv()*X.T*Y]
def row(k,role):
 g=action(k);log_weight=-g+6*k*math.log(k)+d*k+a*math.log(k);return {'k':k,'role':role,'minus_log_abs':g,'renormalized_log_weight':log_weight,'renormalized_weight_magnitude':math.exp(log_weight),'distance_from_predicted_limit':abs(log_weight+c)}
rows=[row(k,'fit') for k in fit_ks]+[row(k,'validation') for k in validation_ks];valid=[r for r in rows if r['role']=='validation']
checks={'positive_power_exponent':a>0,'validation_sections_not_in_fit':all(r['k'] not in fit_ks for r in valid),'validation_near_predicted_limit':max(r['distance_from_predicted_limit'] for r in valid)<0.002,'validation_improves_with_k':valid[-1]['distance_from_predicted_limit']<valid[0]['distance_from_predicted_limit'],'finite_nonzero_limit_estimate':0<math.exp(-c)<math.inf}
out={'schema':'marici.nima.infinite-phase-power-renormalization.v1','asymptotic_model':'-log|W_k|=6 k log k+d k+a log k+c+b/k','fit_sections':list(fit_ks),'validation_sections':list(validation_ks),'parameters':{'d':d,'a':a,'c':c,'b':b},'renormalized_weight':'(-1)^k k^(6k+a) exp(d k) W_k','predicted_limit':math.exp(-c),'sections':rows,'elapsed_seconds':time.perf_counter()-start,'checks':checks,'passed':all(checks.values()),'scope':'Finite-section asymptotic fit with exact W_k and out-of-fit validation through k=400; numerical evidence, not an analytic proof.'}
p=ROOT/'research/nima/results/infinite-phase-power-renormalization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
