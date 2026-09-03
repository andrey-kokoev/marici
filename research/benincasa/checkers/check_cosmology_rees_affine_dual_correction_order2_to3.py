#!/usr/bin/env python3
"""Exact dual correction from a simultaneous order-two detector to the order-three detector."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=g['H'],h['Q'],h['K'],h['target'],h['B'];one={(0,0):F(1)};R=mul(H,Q)
def pw(a,n):
 r=one
 for _ in range(n):r=mul(r,a)
 return r
def pf(s):
 a,b=s.split('/') if '/' in s else (s,'1');return F(int(a),int(b))
def ev(lam,f):return sum(lam.get(m,F(0))*v for m,v in f.items())
def pull(lam,P):
 mx=max(a for a,b in lam);my=max(b for a,b in lam);out={}
 for i in range(mx+1):
  for j in range(my+1):
   v=sum(c*lam.get((i+a,j+b),F(0)) for (a,b),c in P.items())
   if v:out[(i,j)]=v
 return out
def M(f,z,kp,n):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c));return add(mul(R,L),sc(mul(mul(Kp,Q),mul(f,der(R,z))),-n))
a=json.loads((HERE.parents[1]/'results'/'cosmology_rees_affine_transportable_representative.json').read_text());nu={tuple(x['monomial']):pf(x['coefficient']) for x in a['certificate_R4']};b=json.loads((HERE.parents[1]/'results'/'cosmology_rees_affine_H3Q3_exact_certificate.json').read_text());lam3={tuple(x['monomial']):pf(x['coefficient']) for x in b['certificate']};mu3=pull(lam3,pw(R,2));delta=dict(mu3)
for m,v in nu.items():delta[m]=delta.get(m,F(0))-v
bad=0;cols=0
for kp,cap in ((1,26),(0,22)):
 for z in (0,1):
  for d in range(cap+1):
   for i in range(d+1):
    q=M({(i,d-i):F(1)},z,kp,3);bad+=ev(delta,q)+ev(nu,q)!=0;cols+=1
t4=mul(target,pw(R,4));out={'schema':'marici.benincasa.cosmology-rees-affine-dual-correction-order2-to3.v1','base_support':len(nu),'order3_support':len(mu3),'correction_support':sum(v!=0 for v in delta.values()),'columns_tested':cols,'correction_equation_residuals':bad,'base_target_R4_pairing':str(ev(nu,t4)),'order3_target_R4_pairing':str(ev(mu3,t4)),'correction_target_R4_pairing':str(ev(delta,t4)),'identity':'delta=mu3-nu; delta M3=-nu M3','scope':'exact for the chosen representatives; does not establish canonical or all-order transport'};(HERE.parents[1]/'results'/'cosmology_rees_affine_dual_correction_order2_to3.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
