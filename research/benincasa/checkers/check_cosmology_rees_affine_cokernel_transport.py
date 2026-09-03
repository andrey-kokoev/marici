#!/usr/bin/env python3
"""Exact dual correction transporting the pole-two reduced cokernel to pole three."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_affine_localized_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=h['H'],h['Q'],h['K'],h['target'],h['B'];one={(0,0):F(1)};R=mul(H,Q)
def pw(a,n):
 r=one
 for _ in range(n):r=mul(r,a)
 return r
def pf(s):
 a,b=s.split('/') if '/' in s else (s,'1');return F(int(a),int(b))
def cert(n):
 x=json.loads((HERE.parents[1]/'results'/f'cosmology_rees_affine_H{n}Q{n}_exact_certificate.json').read_text());return {tuple(q['monomial']):pf(q['coefficient']) for q in x['certificate']}
def pull(lam,P):
 out={};mx=max(a for a,b in lam);my=max(b for a,b in lam)
 for i in range(mx+1):
  for j in range(my+1):
   v=sum(c*lam.get((i+a,j+b),F(0)) for (a,b),c in P.items())
   if v:out[(i,j)]=v
 return out
def ev(lam,f):return sum(lam.get(m,F(0))*v for m,v in f.items())
def M(f,z,kp,n):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c))
 return add(mul(R,L),sc(mul(mul(Kp,Q),mul(f,der(R,z))),-n))
mu2=pull(cert(2),R);mu3=pull(cert(3),pw(R,2));t3=mul(target,pw(R,4));cross=ev(mu2,t3)
if not cross:
 out={'schema':'marici.benincasa.cosmology-rees-affine-cokernel-transport.v1','from_order':2,'to_order':3,'mu2_support':len(mu2),'mu3_support':len(mu3),'cross_target_pairing':'0','disposition':'direct carry-over fails before the operator transport equation because the order-two reduced functional does not detect the order-three target','scope':'does not exclude a noncanonical correction or an alternative choice of order-two cokernel functional'}
 (HERE.parents[1]/'results'/'cosmology_rees_affine_cokernel_transport.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0)
scale=1/cross;delta=dict(mu3)
for m,v in mu2.items():delta[m]=delta.get(m,F(0))-scale*v
rows=[];bad=0
for kp,maxd in ((1,26),(0,22)):
 for z in (0,1):
  for d in range(maxd+1):
   for i in range(d+1):
    q=M({(i,d-i):F(1)},z,kp,3);r=ev(delta,q)+scale*ev(mu2,q);bad+=r!=0
out={'schema':'marici.benincasa.cosmology-rees-affine-cokernel-transport.v1','from_order':2,'to_order':3,'mu2_support':len(mu2),'mu3_support':len(mu3),'cross_target_pairing':str(cross),'base_scale':str(scale),'delta_support':sum(v!=0 for v in delta.values()),'transport_equation_residuals':bad,'transported_target_pairing':str(ev(mu3,t3)),'scope':'exact correction exists for the computed order-2 and order-3 certificates; no canonical or all-n transport follows'};(HERE.parents[1]/'results'/'cosmology_rees_affine_cokernel_transport.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
