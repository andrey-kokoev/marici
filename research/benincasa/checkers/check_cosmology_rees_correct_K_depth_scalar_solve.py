#!/usr/bin/env python3
"""Exact scalar solve with the actual three K-coordinate levels."""
import json,runpy
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve();R=P.parents[1]/'results'
# Reuse polynomial constructors without trusting the old operators/target.
g=runpy.run_path(str(P.with_name('check_cosmology_rees_scalar_joint_tail_solve.py')));add,sc,mul,der=g['add'],g['sc'],g['mul'],g['der'];Q,K=g['Q'],g['K']
def B(f,z):return add(mul(Q,der(f,z)),sc(mul(der(Q,z),f),-1))
def L(f,z,kp):
 p=2-kp;c=F(-1,2)-kp
 return add(mul(K if p==1 else mul(K,K),B(f,z)),sc(mul(mul(K if p-1==1 else {(0,0):F(1)},Q),mul(der(K,z),f)),c))
cols=[];labels=[]
for kp,maxd in [(1,5),(0,1)]:
 for z in (0,1):
  for d in range(maxd+1):
   for i in range(d+1):cols.append(L({(i,d-i):F(1)},z,kp));labels.append((kp,z,i,d-i))
target=sc(mul(mul(K,K),Q),3);mons=sorted(set(target)|{q for c in cols for q in c},key=lambda q:(sum(q),q[0]));n=len(cols);rows=[[c.get(m,F(0)) for c in cols]+[target.get(m,F(0))] for m in mons];pr=0;piv=[]
for j in range(n):
 q=next((i for i in range(pr,len(rows)) if rows[i][j]),None)
 if q is None:continue
 rows[pr],rows[q]=rows[q],rows[pr];v=rows[pr][j];rows[pr]=[x/v for x in rows[pr]]
 for i in range(len(rows)):
  if i!=pr and rows[i][j]:
   v=rows[i][j];rows[i]=[a-v*b for a,b in zip(rows[i],rows[pr])]
 piv.append(j);pr+=1
bad=any(all(not x for x in r[:-1]) and r[-1] for r in rows);sol=[F(0)]*n
if not bad:
 for i,j in enumerate(piv):sol[j]=rows[i][-1]
 assert not add(target,*[sc(c,-x) for c,x in zip(cols,sol) if x])
out={'schema':'marici.benincasa.cosmology-rees-correct-K-depth-scalar-solve.v1','weights':'w(kp,levels)=K^(2-kp) product q_i^(2-level_i)','operators':['L0=K^2 B-(1/2)KQ gradK dot f','L1=K B-(3/2)Q gradK dot f'],'target':'3K^2Q','unknown_count':n,'equation_count':len(mons),'matrix_rank':len(piv),'consistent':not bad,'nonzero_solution_count':sum(bool(x) for x in sol),'solution':[{'label':repr(labels[i]),'coefficient':str(x)} for i,x in enumerate(sol) if x],'exact_residual_zero':not bad};(R/'cosmology_rees_correct_K_depth_scalar_solve.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
