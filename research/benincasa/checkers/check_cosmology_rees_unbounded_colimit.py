#!/usr/bin/env python3
"""Exact finite falsification audit for the all-order transition identity and formal colimit."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve();b=P.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(b))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,B=g['H'],h['Q'],h['K'],h['B'];O={(0,0):F(1)};R=mul(H,Q)
def M(f,z,k,n):
 p=2-k;c=F(-1,2)-k;Kp=K if p==1 else mul(K,K);Km=O if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c));return add(mul(R,L),sc(mul(mul(Kp,Q),mul(f,der(R,z))),-n))
tests=[]
for n in range(2,8):
 bad=0;count=0
 for k in (0,1):
  for z in (0,1):
   for d in range(7):
    for i in range(d+1):
     f={(i,d-i):F(1)};bad+=M(mul(R,f),z,k,n+1)!=mul(R,M(f,z,k,n));count+=1
 tests.append({'order':n,'basis_tests':count,'residuals':bad})
out={'schema':'marici.benincasa.cosmology-rees-unbounded-colimit.v1','identity':'M_(n+1)(R f)=R M_n(f)','finite_falsification_tests':tests,'formal_direct_system':{'objects':'Q_n=P/im(M_n) for integers n>=2','arrows':'i_n([f])=[R f]','composition':'i_(m-1)...i_n([f])=[R^(m-n) f]'},'formal_colimit':'disjoint union of Q_n modulo (n,x)~(n+1,i_n(x))','formal_colimit_constructed':all(x['residuals']==0 for x in tests),'target_class_nonzero_in_colimit':None,'target_nonzero_gate':'a class nonzero at finitely many stages may still map to zero later; requires all-order nonvanishing or one compatible colimit detector','faithful_coordinate_on_colimit':None,'scope':'algebraic direct limit of presentation quotients; no stabilization, nonzero distinguished class, physical descent, or canonical rank-26 comparison'};(P.parents[1]/'results'/'cosmology_rees_unbounded_colimit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
