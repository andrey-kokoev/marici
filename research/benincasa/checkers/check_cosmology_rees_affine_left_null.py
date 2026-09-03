#!/usr/bin/env python3
"""Extract a rational left-null certificate and test higher columns."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();src=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(src))
L,target=h['L'],h['target'];cols=[]
for kp,maxd in [(1,9),(0,7)]:
 for z in (0,1):
  for d in range(maxd+1):
   for i in range(d+1):cols.append(L({(i,d-i):F(1)},z,kp))
mons=sorted(set(target)|{q for c in cols for q in c},key=lambda q:(sum(q),q[0]));n=len(cols);m=len(mons);A=[[c.get(q,F(0)) for c in cols]+[target.get(q,F(0))] for q in mons];U=[[F(i==j) for j in range(m)] for i in range(m)];r=0
for j in range(n):
 q=next((i for i in range(r,m) if A[i][j]),None)
 if q is None:continue
 A[r],A[q]=A[q],A[r];U[r],U[q]=U[q],U[r];v=A[r][j];A[r]=[x/v for x in A[r]];U[r]=[x/v for x in U[r]]
 for i in range(m):
  if i!=r and A[i][j]:v=A[i][j];A[i]=[x-v*y for x,y in zip(A[i],A[r])];U[i]=[x-v*y for x,y in zip(U[i],U[r])]
 r+=1
bad=next(i for i,row in enumerate(A) if not any(row[:n]) and row[n]);lam=U[bad];detect=sum(lam[i]*target.get(mons[i],F(0)) for i in range(m));tests=[]
for kp,ds in [(1,range(10,16)),(0,range(8,14))]:
 for d in ds:
  hit=0
  for z in (0,1):
   for a in range(d+1):
    c=L({(a,d-a):F(1)},z,kp);v=sum(lam[i]*c.get(mons[i],F(0)) for i in range(m));hit+=bool(v)
  tests.append({'level':kp,'degree':d,'nonannihilated_columns':hit})
def fs(x):return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
support_degrees=[sum(mons[i]) for i,x in enumerate(lam) if x];out={'schema':'marici.benincasa.cosmology-rees-affine-left-null.v1','caps':[9,7],'support_size':sum(bool(x) for x in lam),'support_degree_range':[min(support_degrees),max(support_degrees)],'target_pairing':fs(detect),'higher_column_tests':tests,'annihilates_all_tested_higher_columns':all(t['nonannihilated_columns']==0 for t in tests),'functional':[{'monomial':list(mons[i]),'coefficient':fs(x)} for i,x in enumerate(lam) if x]};R=HERE.parents[1]/'results';(R/'cosmology_rees_affine_left_null.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['support_size','target_pairing','annihilates_all_tested_higher_columns','higher_column_tests']},indent=2))
