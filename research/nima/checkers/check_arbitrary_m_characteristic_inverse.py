#!/usr/bin/env python3
"""Construct the explicit integral inverse of the characteristic transform."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
rows=[]
for m in range(2,13):
 ev=[(i,j) for i in range(1,m+1) for j in range(i,m+1)];p={e:k for k,e in enumerate(ev)}
 top=[(1,j) for j in range(1,m+1)];right=[(i,m) for i in range(2,m+1)];bulk=[(i,j) for i in range(2,m+1) for j in range(i,m)];obs=top+right+bulk;o={e:k for k,e in enumerate(obs)};T=s.zeros(len(ev));
 for e in top+right:T[o[e],p[e]]=1
 for i,j in bulk:
  for e,c in (((i,j),1),((i-1,j),-1),((i,j+1),-1),((i-1,j+1),1)):T[o[(i,j)],p[e]]=c
 # Rows of Q express reconstructed f(i,j) in descriptor coordinates.
 Q=s.zeros(len(ev));
 for e in top+right:Q[p[e],o[e]]=1
 for i in range(2,m+1):
  for j in range(m-1,i-1,-1):Q[p[(i,j)],:]=Q[p[(i-1,j)],:]+Q[p[(i,j+1)],:]-Q[p[(i-1,j+1)],:];Q[p[(i,j)],o[(i,j)]]+=1
 rows.append({'m':m,'dimension':len(ev),'left_inverse':Q*T==s.eye(len(ev)),'right_inverse':T*Q==s.eye(len(ev)),'inverse_integral':all(z.q==1 for z in Q),'inverse_max_abs_entry':max(abs(int(z)) for z in Q)})
checks={'m2_to_m12':len(rows)==11,'two_sided_inverse':all(x['left_inverse'] and x['right_inverse'] for x in rows),'integral_inverse':all(x['inverse_integral'] for x in rows)}
out={'schema':'marici.nima.arbitrary-m-characteristic-inverse.v1','recurrence':'f(i,j)=g(i,j)+f(i-1,j)+f(i,j+1)-f(i-1,j+1), evaluated for i=2..m and j=m-1 down to i','inductive_theorem':'For every finite m>=2, boundary values on i=1 and j=m (overlap omitted) plus every interior mixed difference determine a unique field. The displayed recurrence constructs an integral inverse; induction over lexicographic (i,-j) verifies each coordinate, so the transform is unimodular over Z.','computational_rows':rows,'checks':checks,'passed':all(checks.values()),'control_disposition':'This is a static coordinate isomorphism. It supplies no physical time, transition law, actuator, Rosenbrock pencil, or robustness margin.','claim_boundary':'The arbitrary-finite-m statement concerns the integral characteristic transform only; there is no colimit or bounded-inverse theorem.'}
p=R/'research/nima/results/arbitrary-m-characteristic-inverse.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
