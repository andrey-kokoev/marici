#!/usr/bin/env python3
"""Exact pole-one localized affine scalar tests with cleared denominators."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();src=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(src))
g=h['g'];add,sc,mul,der=h['add'],h['sc'],h['mul'],h['der'];Q,K,B,target=h['Q'],h['K'],h['B'],h['target'];H=g['H']
def Lnum(f,z,kp,D):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=K if p-1==1 else {(0,0):F(1)}
 return add(mul(Kp,add(mul(D,B(f,z)),sc(mul(mul(Q,f),der(D,z)),-1))),sc(mul(mul(mul(Km,Q),mul(der(K,z),f)),D),c))
def solve(D,name,degD):
 cols=[]
 for kp,maxd in [(1,5+degD),(0,1+degD)]:
  for z in (0,1):
   for d in range(maxd+1):
    for i in range(d+1):cols.append(Lnum({(i,d-i):F(1)},z,kp,D))
 tgt=mul(target,mul(D,D));mons=sorted(set(tgt)|{q for c in cols for q in c},key=lambda q:(sum(q),q[0]));n=len(cols);A=[[c.get(q,F(0)) for c in cols]+[tgt.get(q,F(0))] for q in mons];r=0
 for j in range(n):
  q=next((i for i in range(r,len(A)) if A[i][j]),None)
  if q is None:continue
  A[r],A[q]=A[q],A[r];v=A[r][j];A[r]=[x/v for x in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][j]:v=A[i][j];A[i]=[x-v*y for x,y in zip(A[i],A[r])]
  r+=1
 return {'denominator':name,'pole_order':1,'numerator_caps':[5+degD,1+degD],'unknowns':n,'equations':len(mons),'rank':r,'consistent':not any(not any(row[:n]) and row[n] for row in A)}
rows=[dict(solve(mul(Q,Q),'Q^2',10),pole_order=2)];out={'schema':'marici.benincasa.cosmology-rees-affine-localized-solve.v1','domain':'common denominator D at both levels and components','rows':rows};R=HERE.parents[1]/'results';(R/'cosmology_rees_affine_localized_solve.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
