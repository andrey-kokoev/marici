#!/usr/bin/env python3
"""Exact verification of the denominator-power recurrence for affine localization."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_affine_localized_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=h['H'],h['Q'],h['K'],h['target'],h['B'];one={(0,0):F(1)}
def pw(a,n):
 r=one
 for _ in range(n):r=mul(r,a)
 return r
def Lpoly(f,z,kp):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K
 return add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c))
def N(f,z,kp,D):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K
 return add(mul(Kp,add(mul(D,B(f,z)),sc(mul(mul(Q,f),der(D,z)),-1))),sc(mul(mul(mul(Km,Q),mul(der(K,z),f)),D),c))
R=mul(H,Q);rows=[]
for n in range(1,5):
 D=pw(R,n);bad=0;tested=0
 for kp in (1,0):
  p=2-kp;Kp=K if p==1 else mul(K,K)
  for z in (0,1):
   for d in range(4):
    for i in range(d+1):
     f={(i,d-i):F(1)};M=add(mul(R,Lpoly(f,z,kp)),sc(mul(mul(Kp,Q),mul(f,der(R,z))),-n));bad+=N(f,z,kp,D)!=mul(pw(R,n-1),M);tested+=1
 target_ok=mul(target,mul(D,D))==mul(pw(R,n-1),mul(target,pw(R,n+1)));rows.append({'pole_order':n,'basis_columns_tested':tested,'operator_residuals':bad,'target_factorization':target_ok})
out={'schema':'marici.benincasa.cosmology-rees-affine-pole-order-recurrence.v1','identity':'N_n(f)=R^(n-1)[R L_poly(f)-n K^p Q f partial(R)]','R':'H Q','rows':rows,'verified':all(x['operator_residuals']==0 and x['target_factorization'] for x in rows),'induction_residual':'the order shift n to n+1 changes the reduced operator by -K^p Q f partial(R); cokernel transport is not supplied by factorization alone'};(HERE.parents[1]/'results'/'cosmology_rees_affine_pole_order_recurrence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
