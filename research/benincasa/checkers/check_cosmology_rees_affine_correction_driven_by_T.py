#!/usr/bin/env python3
"""Verify that the exact dual correction is driven by the pole-shift term T."""
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
def ev(l,f):return sum(l.get(m,F(0))*v for m,v in f.items())
def pull(l,P):
 out={};mx=max(a for a,b in l);my=max(b for a,b in l)
 for i in range(mx+1):
  for j in range(my+1):
   v=sum(c*l.get((i+a,j+b),F(0)) for (a,b),c in P.items())
   if v:out[(i,j)]=v
 return out
def pieces(f,z,kp,n):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c));T=mul(mul(Kp,Q),mul(f,der(R,z)));return add(mul(R,L),sc(T,-n)),T
a=json.loads((HERE.parents[1]/'results'/'cosmology_rees_affine_transportable_representative_third.json').read_text());nu={tuple(x['monomial']):pf(x['coefficient']) for x in a['certificate_R4']};b=json.loads((HERE.parents[1]/'results'/'cosmology_rees_affine_H3Q3_exact_certificate.json').read_text());lam3={tuple(x['monomial']):pf(x['coefficient']) for x in b['certificate']};mu3=pull(lam3,pw(R,2));delta=dict(mu3)
for m,v in nu.items():delta[m]=delta.get(m,F(0))-v
m2bad=tb=0;count=0;by_degree=[]
for kp,cap in ((1,26),(0,22)):
 for d in range(cap+1):
  rb=rt=0
  for z in (0,1):
   for i in range(d+1):
    f={(i,d-i):F(1)};m2,_=pieces(f,z,kp,2);m3,T=pieces(f,z,kp,3);rb+=ev(nu,m2)!=0;rt+=ev(delta,m3)-ev(nu,T)!=0;count+=1
  if rb or rt:by_degree.append({'level':kp,'degree':d,'nu_M2_residuals':rb,'transport_residuals':rt})
  m2bad+=rb;tb+=rt
deg=sorted({sum(m) for m,v in nu.items() if v});first=by_degree[0] if by_degree else None
out={'schema':'marici.benincasa.cosmology-rees-affine-correction-driven-by-T-third.v1','nu_support_degree_range':[min(deg),max(deg)],'columns_tested':count,'nu_M2_residuals':m2bad,'delta_M3_minus_nu_T_residuals':tb,'residuals_by_degree':by_degree,'first_residual':first,'persistent':m2bad==0,'disposition':'T-driven transport holds only where nu annihilates M2; the first listed degree is the exact extension obstruction','identity':'M3=M2-T implies delta M3=nu T only when nu M2=0'};(HERE.parents[1]/'results'/'cosmology_rees_affine_correction_driven_by_T_third.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
