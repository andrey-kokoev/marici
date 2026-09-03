#!/usr/bin/env python3
"""Exact degree-support persistence for the reduced pole-five target detector."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,B=g['H'],h['Q'],h['K'],h['B'];one={(0,0):F(1)};R=mul(H,Q)
def pf(s):
 a,b=s.split('/') if '/' in s else (s,'1');return F(int(a),int(b))
def ev(l,f):return sum(l.get(m,F(0))*v for m,v in f.items())
def M(f,z,kp):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c));T=mul(mul(Kp,Q),mul(f,der(R,z)));return add(mul(R,L),sc(T,-5))
a=json.loads((HERE.parents[1]/'results'/'cosmology_rees_affine_pole5_target_detector.json').read_text());lam={tuple(x['monomial']):pf(x['coefficient']) for x in a['certificate_R6']};ds=[sum(m) for m in lam];smax=max(ds);tests=[]
for kp,start in ((1,41),(0,37)):
 d=start
 while True:
  cols=[M({(i,d-i):F(1)},z,kp) for z in (0,1) for i in range(d+1)];mind=min(sum(m) for c in cols for m,v in c.items() if v);bad=sum(ev(lam,c)!=0 for c in cols);tests.append({'level':kp,'degree':d,'minimum_output_degree':mind,'nonannihilated':bad})
  if mind>smax:break
  d+=1
out={'schema':'marici.benincasa.cosmology-rees-affine-pole5-persistence.v1','support_size':len(lam),'support_degree_range':[min(ds),smax],'boundary_tests':tests,'persistent':all(x['nonannihilated']==0 for x in tests),'proof':'all degrees through caps (40,36) were exactly verified; after the listed boundary, minimum output degree increases beyond support'};(HERE.parents[1]/'results'/'cosmology_rees_affine_pole5_persistence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
