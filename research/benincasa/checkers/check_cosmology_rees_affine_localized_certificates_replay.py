#!/usr/bin/env python3
"""Dependency-free replay of exact H^2Q^2 and H^3Q^3 certificate verification."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=h['g']['H'],h['Q'],h['K'],h['target'],h['B']
def Lnum(f,z,kp,D):
 p=2-kp;c=F(-1,2)-kp;one={(0,0):F(1)};Kp=K if p==1 else mul(K,K);Km=one if p==1 else K
 return add(mul(Kp,add(mul(D,B(f,z)),sc(mul(mul(Q,f),der(D,z)),-1))),sc(mul(mul(mul(Km,Q),mul(der(K,z),f)),D),c))
def pf(s):
 a,b=s.split('/') if '/' in s else (s,'1');return F(int(a),int(b))
def power(a,n):
 r={(0,0):F(1)}
 for _ in range(n):r=mul(r,a)
 return r
rows=[]
for n,caps in ((2,(19,15)),(3,(26,22))):
 path=HERE.parents[1]/'results'/f'cosmology_rees_affine_H{n}Q{n}_exact_certificate.json';cert=json.loads(path.read_text());lam={tuple(x['monomial']):pf(x['coefficient']) for x in cert['certificate']};D=mul(power(H,n),power(Q,n));bad=0;count=0
 for kp,maxd in zip((1,0),caps):
  for z in (0,1):
   for d in range(maxd+1):
    for i in range(d+1):
     c=Lnum({(i,d-i):F(1)},z,kp,D);count+=1;bad+=sum(lam.get(m,F(0))*v for m,v in c.items())!=0
 tgt=mul(target,mul(D,D));pair=sum(lam.get(m,F(0))*v for m,v in tgt.items());rows.append({'pole_order':n,'columns':count,'nonannihilated_columns':bad,'target_pairing':str(pair),'verified':bad==0 and pair==1})
out={'schema':'marici.benincasa.cosmology-rees-affine-localized-certificates-replay.v1','dependency_free':True,'rows':rows,'verified':all(x['verified'] for x in rows)};(HERE.parents[1]/'results'/'cosmology_rees_affine_localized_certificates_replay.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
