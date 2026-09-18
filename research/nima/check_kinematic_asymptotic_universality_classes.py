#!/usr/bin/env python3
"""Test universality of leading chain asymptotics within spacing classes."""
import json,math,sys,time
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_chain_toy import connected_chain
families={
 'linear_i':(1,lambda i:i),'linear_3i+7':(1,lambda i:3*i+7),
 'quadratic_i2+i':(2,lambda i:i*i+i),'quadratic_2base+5':(2,lambda i:2*(i*i+3*i+1)+5),'quadratic_i2+11i':(2,lambda i:i*i+11*i),
 'cubic_i3+i':(3,lambda i:i**3+i),'cubic_5i3+2i2+i':(3,lambda i:5*i**3+2*i*i+i),'cubic_i3+20i2':(3,lambda i:i**3+20*i*i+i)}
ks=(30,45,60,75,90);rows={};start=time.perf_counter()
for name,(degree,fn) in families.items():
 ys=[]
 for k in ks:
  n=3*k+2;h,_,c=connected_chain(k,[fn(i) for i in range(1,n+1)]);v=h.component(c);g=float(s.N(-s.log(abs(v)),18));ys.append(g/k)
 X=s.Matrix([[math.log(k),1.0,math.log(k)/k,1.0/k] for k in ks]);Y=s.Matrix(ys);clog,d,elog,e=[float(v) for v in (X.T*X).inv()*X.T*Y];rows[name]={'spacing_degree':degree,'k_log_k_coefficient':clog,'extensive_constant':d,'log_k_over_k':elog,'one_over_k':e,'expected_leading':6*(degree-1),'leading_error':clog-6*(degree-1)}
bydegree={p:[r['k_log_k_coefficient'] for r in rows.values() if r['spacing_degree']==p] for p in (1,2,3)}
checks={'leading_coefficient_matches_6p_minus_6':all(abs(r['leading_error'])<0.05 for r in rows.values()),'within_class_spread_small':all(max(v)-min(v)<0.05 for v in bydegree.values()),'extensive_constants_not_universal':len({round(r['extensive_constant'],3) for r in rows.values()})>3,'all_three_spacing_classes':set(bydegree)=={1,2,3}}
out={'schema':'marici.nima.kinematic-asymptotic-universality-classes.v1','model':'-log|W_k|/k = c_log log k+d+(e_log log k+e)/k','finite_sections':list(ks),'families':rows,'class_coefficients':bydegree,'conclusion':'Within tested polynomial-growth classes c_log is universal and equals 6(p-1); the extensive constant is not universal under affine/lower-order changes.','elapsed_seconds':time.perf_counter()-start,'checks':checks,'passed':all(checks.values()),'scope':'Exact finite sections for eight positive coherent moment-curve sequences; numerical asymptotic classification, not proof for arbitrary twistors.'}
p=ROOT/'research/nima/results/kinematic-asymptotic-universality-classes.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
