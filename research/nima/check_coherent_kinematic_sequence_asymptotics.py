#!/usr/bin/env python3
"""Compare chain asymptotics across coherent infinite moment-curve sequences."""
import json,math,sys,time
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_chain_toy import connected_chain
families={'linear':lambda i:i,'quadratic':lambda i:i*i+3*i+1,'cubic':lambda i:i**3+i};ks=(20,30,40,50,60);outrows={};start=time.perf_counter()
for name,fn in families.items():
 rows=[]
 for k in ks:
  n=3*k+2;h,_,c=connected_chain(k,[fn(i) for i in range(1,n+1)]);v=h.component(c);g=float(s.N(-s.log(abs(v)),18));rows.append({'k':k,'action':g,'action_over_k':g/k,'action_over_k_log_k':g/(k*math.log(k))})
 # Fit action/k = c_log log(k)+d on the tail.
 X=s.Matrix([[math.log(r['k']),1.0] for r in rows]);Y=s.Matrix([r['action_over_k'] for r in rows]);c_log,d=[float(v) for v in (X.T*X).inv()*X.T*Y]
 outrows[name]={'sections':rows,'fitted_k_log_k_coefficient':c_log,'fitted_extensive_constant':d}
coeff={name:r['fitted_k_log_k_coefficient'] for name,r in outrows.items()}
checks={'all_sequences_exact_nonzero':all(all(r['action']>0 for r in f['sections']) for f in outrows.values()),'raw_leading_coefficient_not_universal':max(coeff.values())-min(coeff.values())>5,'coefficient_tracks_spacing_degree':coeff['linear']<coeff['quadratic']<coeff['cubic'],'quadratic_near_previous_six':abs(coeff['quadratic']-6)<1}
out={'schema':'marici.nima.coherent-kinematic-sequence-asymptotics.v1','sequences':{'linear':'x_i=i','quadratic':'x_i=i^2+3i+1','cubic':'x_i=i^3+i'},'finite_sections':list(ks),'families':outrows,'conclusion':'The raw k log k coefficient is not kinematic-universal; it tracks asymptotic point spacing and must be removed by a projectively/local normalized reference operator.','elapsed_seconds':time.perf_counter()-start,'checks':checks,'passed':all(checks.values()),'scope':'Exact chain components on three positive coherent moment-curve sequences; finite-section fits, not asymptotic proofs.'}
p=ROOT/'research/nima/results/coherent-kinematic-sequence-asymptotics.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
