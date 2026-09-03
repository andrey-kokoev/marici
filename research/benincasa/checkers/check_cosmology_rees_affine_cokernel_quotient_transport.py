#!/usr/bin/env python3
"""Exact descent test for multiplication by R on reduced cokernel quotients."""
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
def pull(l,P):
 out={};mx=max(a for a,b in l);my=max(b for a,b in l)
 for i in range(mx+1):
  for j in range(my+1):
   v=sum(c*l.get((i+a,j+b),F(0)) for (a,b),c in P.items())
   if v:out[(i,j)]=v
 return out
def ev(l,f):return sum(l.get(m,F(0))*v for m,v in f.items())
def M(f,z,kp,n):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c));return add(mul(R,L),sc(mul(mul(Kp,Q),mul(f,der(R,z))),-n))
b=json.loads((HERE.parents[1]/'results'/'cosmology_rees_affine_H3Q3_exact_certificate.json').read_text());full={tuple(x['monomial']):pf(x['coefficient']) for x in b['certificate']};mu3=pull(full,pw(R,2));smax=max(sum(m) for m in mu3);res=[]
for kp in (1,0):
 d=0
 while True:
  vals=[];mind=None
  for z in (0,1):
   for i in range(d+1):
    q=mul(R,M({(i,d-i):F(1)},z,kp,2));vals.append(ev(mu3,q));md=min(sum(m) for m,v in q.items() if v);mind=md if mind is None else min(mind,md)
  nz=sum(v!=0 for v in vals)
  if nz:res.append({'level':kp,'degree':d,'nonzero_pairings':nz,'first_pairing':str(next(v for v in vals if v))})
  if mind>smax:break
  d+=1
t3=mul(target,pw(R,3));out={'schema':'marici.benincasa.cosmology-rees-affine-cokernel-quotient-transport.v1','candidate_map':'multiplication by R from coker(M2) to coker(M3)','descent_condition':'R image(M2) subset image(M3)','mu3_support_size':len(mu3),'mu3_support_max_degree':smax,'target_class_pairing_after_R':str(ev(mu3,mul(R,t3))),'image_descent_residuals':res,'descends':False if res else None,'candidate_survives_mu3_probe':not res,'disposition':'a nonzero mu3 pairing would disprove descent; zero pairing with this one cokernel probe does not prove image inclusion'};(HERE.parents[1]/'results'/'cosmology_rees_affine_cokernel_quotient_transport.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
