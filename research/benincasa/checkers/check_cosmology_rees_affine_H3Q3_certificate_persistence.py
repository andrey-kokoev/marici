#!/usr/bin/env python3
"""Exact support persistence for the H^3Q^3 certificate."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_affine_localized_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,B=h['H'],h['Q'],h['K'],h['B']
def Lnum(f,z,kp,D):
 p=2-kp;c=F(-1,2)-kp;one={(0,0):F(1)};Kp=K if p==1 else mul(K,K);Km=one if p==1 else K
 return add(mul(Kp,add(mul(D,B(f,z)),sc(mul(mul(Q,f),der(D,z)),-1))),sc(mul(mul(mul(Km,Q),mul(der(K,z),f)),D),c))
def pf(s):
 a,b=s.split('/') if '/' in s else (s,'1');return F(int(a),int(b))
cert=json.loads((HERE.parents[1]/'results'/'cosmology_rees_affine_H3Q3_exact_certificate.json').read_text());lam={tuple(x['monomial']):pf(x['coefficient']) for x in cert['certificate']};ds=sorted({sum(m) for m in lam});D=mul(mul(mul(H,H),H),mul(mul(Q,Q),Q));tests=[]
for kp,d in ((1,27),(0,23)):
 cols=[Lnum({(i,d-i):F(1)},z,kp,D) for z in (0,1) for i in range(d+1)];tests.append({'level':kp,'first_omitted_degree':d,'minimum_output_degree':min(sum(m) for c in cols for m,v in c.items() if v),'nonannihilated_columns':sum(sum(lam.get(m,F(0))*v for m,v in c.items())!=0 for c in cols)})
out={'schema':'marici.benincasa.cosmology-rees-affine-H3Q3-certificate-persistence.v1','support_size':len(lam),'support_degree_range':[min(ds),max(ds)],'boundary_tests':tests,'persistent':all(x['minimum_output_degree']>max(ds) and x['nonannihilated_columns']==0 for x in tests),'proof':'minimum output degree increases with numerator degree'};(HERE.parents[1]/'results'/'cosmology_rees_affine_H3Q3_certificate_persistence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
