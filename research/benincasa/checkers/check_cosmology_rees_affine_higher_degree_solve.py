#!/usr/bin/env python3
"""Exact affine scalar solves with incremented degree bounds."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();src=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(src))
L,target=h['L'],h['target'];rowsout=[]
for cap1,cap0 in [(5,1),(6,2),(7,3),(8,4),(9,5),(9,6),(9,7),(10,7),(11,7)]:
 extra=cap1-5;cols=[]
 for kp,maxd in [(1,cap1),(0,cap0)]:
  for z in (0,1):
   for d in range(maxd+1):
    for i in range(d+1):cols.append(L({(i,d-i):F(1)},z,kp))
 mons=sorted(set(target)|{q for c in cols for q in c},key=lambda q:(sum(q),q[0]));n=len(cols);A=[[c.get(m,F(0)) for c in cols]+[target.get(m,F(0))] for m in mons];r=0;piv=[]
 for j in range(n):
  q=next((i for i in range(r,len(A)) if A[i][j]),None)
  if q is None:continue
  A[r],A[q]=A[q],A[r];v=A[r][j];A[r]=[x/v for x in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][j]:v=A[i][j];A[i]=[x-v*y for x,y in zip(A[i],A[r])]
  piv.append(j);r+=1
 consistent=not any(not any(row[:n]) and row[n] for row in A);rowsout.append({'extra_degree':extra,'level1_max_degree':cap1,'level0_max_degree':cap0,'unknowns':n,'equations':len(mons),'rank':len(piv),'consistent':consistent})
out={'schema':'marici.benincasa.cosmology-rees-affine-higher-degree-solve.v1','rows':rowsout};R=HERE.parents[1]/'results';(R/'cosmology_rees_affine_higher_degree_solve.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
