#!/usr/bin/env python3
"""Asymptotics across coherent positive curves with different embeddings in P3."""
import itertools,json,math,sys,time
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_chain_toy import connected_chain
profiles={'ordinary_0123':(0,1,2,3),'generalized_0124':(0,1,2,4),'generalized_0135':(0,1,3,5),'generalized_0236':(0,2,3,6)};ks=(20,30,40,50,60);rows={};start=time.perf_counter()
for name,powers in profiles.items():
 ys=[];positive=True
 for k in ks:
  n=3*k+2;xs=[s.Integer(i) for i in range(1,n+1)];cols=[[x**p for p in powers] for x in xs];h,_,c=connected_chain(k,xs,cols);v=h.component(c);g=float(s.N(-s.log(abs(v)),18));ys.append(g/k)
  # Ordered maximal minors are positive for these generalized Vandermonde probes.
  for q in itertools.combinations(range(min(n,8)),4):positive &= s.det(s.Matrix.hstack(*(s.Matrix(cols[i]) for i in q)))>0
 X=s.Matrix([[math.log(k),1.0,math.log(k)/k,1.0/k] for k in ks]);Y=s.Matrix(ys);clog,d,elog,e=[float(v) for v in (X.T*X).inv()*X.T*Y];rows[name]={'powers':list(powers),'sum_excess':sum(powers)-6,'ordered_probe_minors_positive':bool(positive),'k_log_k_coefficient':clog,'extensive_constant':d,'log_k_over_k':elog,'one_over_k':e}
coeff=[r['k_log_k_coefficient'] for r in rows.values()]
checks={'all_generalized_curves_positive_on_probe':all(r['ordered_probe_minors_positive'] for r in rows.values()),'ordinary_linear_embedding_has_zero_log_coefficient':abs(rows['ordinary_0123']['k_log_k_coefficient'])<1e-6,'embedding_changes_raw_leading_coefficient':max(coeff)-min(coeff)>5,'all_exact_components_finite':all(math.isfinite(r['extensive_constant']) for r in rows.values())}
out={'schema':'marici.nima.projective-embedding-asymptotics.v1','kinematics':'Z_i=(x_i^m0,x_i^m1,x_i^m2,x_i^m3), x_i=i','finite_sections':list(ks),'profiles':rows,'conclusion':'The raw leading coefficient depends on projective-curve embedding as well as point spacing. A universal infinite object requires normalization by local Plucker data, not only x-spacing.','elapsed_seconds':time.perf_counter()-start,'checks':checks,'passed':all(checks.values()),'scope':'Exact finite chain sections on four generalized positive Vandermonde curves; positivity checked on initial ordered minors, not a proof for every infinite minor.'}
p=ROOT/'research/nima/results/projective-embedding-asymptotics.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
