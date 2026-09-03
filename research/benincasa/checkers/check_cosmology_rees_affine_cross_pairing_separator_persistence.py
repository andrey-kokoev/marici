#!/usr/bin/env python3
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve();b=P.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(b))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,B=g['H'],h['Q'],h['K'],h['B'];O={(0,0):F(1)};R=mul(H,Q)
def pf(s):a,b=s.split('/') if '/' in s else (s,'1');return F(int(a),int(b))
def ev(l,f):return sum(l.get(m,F(0))*v for m,v in f.items())
def M(f,z,k):
 p=2-k;C=F(-1,2)-k;Kp=K if p==1 else mul(K,K);Km=O if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),C));return add(mul(R,L),sc(mul(mul(Kp,Q),mul(f,der(R,z))),-4))
a=json.loads((P.parents[1]/'results'/'cosmology_rees_affine_cross_pairing_separator.json').read_text());l={tuple(x['monomial']):pf(x['coefficient']) for x in a['certificate']};ds=[sum(m) for m in l];tests=[]
for k,d in ((1,34),(0,30)):
 while True:
  C=[M({(i,d-i):F(1)},z,k) for z in (0,1) for i in range(d+1)];mn=min(sum(m) for x in C for m,v in x.items() if v);tests.append({'level':k,'degree':d,'minimum_output_degree':mn,'bad':sum(ev(l,x)!=0 for x in C)})
  if mn>max(ds):break
  d+=1
out={'schema':'marici.benincasa.cosmology-rees-affine-cross-pairing-separator-persistence.v1','support_degree_range':[min(ds),max(ds)],'boundary_tests':tests,'persistent':all(x['bad']==0 for x in tests)};(P.parents[1]/'results'/'cosmology_rees_affine_cross_pairing_separator_persistence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
