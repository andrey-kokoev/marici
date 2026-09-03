#!/usr/bin/env python3
"""Exact dual pullback recurrence between pole-five and pole-four detectors."""
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
def M(f,z,kp,n):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c));T=mul(mul(Kp,Q),mul(f,der(R,z)));return add(mul(R,L),sc(T,-n))
a=json.loads((HERE.parents[1]/'results'/'cosmology_rees_affine_pole4_target_detector.json').read_text());l4={tuple(x['monomial']):pf(x['coefficient']) for x in a['certificate_R5']};b=json.loads((HERE.parents[1]/'results'/'cosmology_rees_affine_pole5_target_detector.json').read_text());l5={tuple(x['monomial']):pf(x['coefficient']) for x in b['certificate_R6']};p5=pull(l5,R);delta=dict(p5)
for m,v in l4.items():delta[m]=delta.get(m,F(0))-v
badp=badd=0;count=0
for kp,cap in ((1,40),(0,36)):
 for z in (0,1):
  for d in range(cap+1):
   for i in range(d+1):
    q=M({(i,d-i):F(1)},z,kp,4);badp+=ev(p5,q)!=0;badd+=ev(delta,q)!=0;count+=1
t4=mul(target,pw(R,5));out={'schema':'marici.benincasa.cosmology-rees-affine-detector-recurrence-order4-5.v1','pullback_support':len(p5),'chosen_order4_support':len(l4),'difference_support':sum(v!=0 for v in delta.values()),'functionals_equal':p5==l4,'columns_tested':count,'pullback_annihilation_residuals':badp,'difference_annihilation_residuals':badd,'pullback_target_pairing':str(ev(p5,t4)),'chosen_target_pairing':str(ev(l4,t4)),'difference_target_pairing':str(ev(delta,t4)),'recurrence':'R-star(lambda_5) is a normalized lambda_4 detector; chosen lambda_4 differs by a target-annihilating cokernel functional','scope':'exact at orders four and five; no unique detector representative'};(HERE.parents[1]/'results'/'cosmology_rees_affine_detector_recurrence_order4_5.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
