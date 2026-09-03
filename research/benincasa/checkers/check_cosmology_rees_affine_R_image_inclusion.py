#!/usr/bin/env python3
"""Exact chain identity proving multiplication by R descends between pole-order cokernels."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=g['H'],h['Q'],h['K'],h['target'],h['B'];R=mul(H,Q);one={(0,0):F(1)}
def pw(a,n):
 r=one
 for _ in range(n):r=mul(r,a)
 return r
def L(f,z,kp):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K;return add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c))
def M(f,z,kp,n):
 p=2-kp;Kp=K if p==1 else mul(K,K);T=mul(mul(Kp,Q),mul(f,der(R,z)));return add(mul(R,L(f,z,kp)),sc(T,-n))
rows=[]
for n in range(1,5):
 bad=0;tested=0
 for kp in (1,0):
  for z in (0,1):
   for d in range(7):
    for i in range(d+1):
     f={(i,d-i):F(1)};bad+=M(mul(R,f),z,kp,n+1)!=mul(R,M(f,z,kp,n));tested+=1
 t=mul(target,pw(R,n+1));target_ok=mul(R,t)==mul(target,pw(R,n+2));rows.append({'from_order':n,'to_order':n+1,'columns_tested':tested,'chain_residuals':bad,'target_transport':target_ok})
out={'schema':'marici.benincasa.cosmology-rees-affine-R-image-inclusion.v1','identity':'M_(n+1)(R f)=R M_n(f)','derivation':'L_poly(R f)=R L_poly(f)+K^p Q f partial(R), whose correction cancels the change from n to n+1','rows':rows,'image_inclusion':'R image(M_n) subset image(M_(n+1)) for every positive integer n','quotient_map':'[g] maps to [R g]','verified':all(x['chain_residuals']==0 and x['target_transport'] for x in rows),'scope':'algebraic reduced polynomial cokernels; no source-derived physical interpretation'};(HERE.parents[1]/'results'/'cosmology_rees_affine_R_image_inclusion.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
