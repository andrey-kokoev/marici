#!/usr/bin/env python3
"""Exact degree-support persistence test for the H^2Q^2 cokernel certificate."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_affine_localized_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=h['H'],h['Q'],h['K'],h['target'],h['B']
def Lnum(f,z,kp,D):
 p=2-kp;c=F(-1,2)-kp;one={(0,0):F(1)};Kp=K if p==1 else mul(K,K);Km=one if p==1 else K
 return add(mul(Kp,add(mul(D,B(f,z)),sc(mul(mul(Q,f),der(D,z)),-1))),sc(mul(mul(mul(Km,Q),mul(der(K,z),f)),D),c))
def pf(s):
 a,b=(s.split('/')+['1'])[:2] if '/' in s else (s,'1');return F(int(a),int(b))
cert=json.loads((HERE.parents[1]/'results'/'cosmology_rees_affine_H2Q2_exact_certificate.json').read_text());lam={tuple(x['monomial']):pf(x['coefficient']) for x in cert['certificate']};support_degrees=sorted({sum(m) for m in lam});smax=max(support_degrees);D=mul(mul(H,H),mul(Q,Q));tests=[]
for kp,start in ((1,20),(0,16)):
 d=start
 while True:
  cols=[Lnum({(i,d-i):F(1)},z,kp,D) for z in (0,1) for i in range(d+1)];mind=min(sum(m) for c in cols for m,v in c.items() if v);bad=sum(1 for c in cols if sum(lam.get(m,F(0))*v for m,v in c.items())!=0);tests.append({'level':kp,'input_degree':d,'minimum_output_degree':mind,'nonannihilated_columns':bad})
  if mind>smax:break
  d+=1
out={'schema':'marici.benincasa.cosmology-rees-affine-H2Q2-certificate-persistence.v1','support_size':len(lam),'support_degree_range':[min(support_degrees),smax],'tested_higher_degrees':tests,'persistent':all(x['nonannihilated_columns']==0 for x in tests),'proof':'all lower degrees are covered by the certified caps; every later degree after the final listed degree has minimum output degree above certificate support'};(HERE.parents[1]/'results'/'cosmology_rees_affine_H2Q2_certificate_persistence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
