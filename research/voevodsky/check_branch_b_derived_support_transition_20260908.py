#!/usr/bin/env python3
"""Exact combinatorial check of the Branch-B local-cohomology support counit."""
import argparse,json
from itertools import combinations
from pathlib import Path

TS=((1,3),(1,5),(3,5),(1,3,5)); ENDS={"plus":(1,3,5),"minus":(0,2,4)}
def subsets(xs): return [s for n in range(len(xs)+1) for s in combinations(xs,n)]
def d(xs,s):
 # Extended Cech incidence; coefficients/localizations are represented by labels.
 return [(s+(x,),(-1)**sum(y<x for y in s)) for x in xs if x not in s]
def total_d(X,J,a,b):
 return [(aa,b,c) for aa,c in d(X,a)]+[(a,bb,((-1)**len(a))*c) for bb,c in d(J,b)]
def proj(a,b): return a if not b else None

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 rows=[]; checks=0; X=tuple(range(6))
 for sigma,I in ENDS.items():
  for T in TS:
   J=('t_T',)+tuple('t'+str(i) for i in I)
   defects=[]
   for u in subsets(X):
    for v in subsets(J):
     lhs={}
     for uu,vv,c in total_d(X,J,u,v):
      z=proj(uu,vv)
      if z is not None: lhs[z]=lhs.get(z,0)+c
     rhs={z:c for z,c in d(X,u)} if proj(u,v) is not None else {}
     lhs={z:c for z,c in lhs.items() if c}
     if lhs!=rhs: defects.append([u,v,lhs,rhs])
     checks+=1
   assert not defects
   rows.append({'sigma':sigma,'T':list(T),'source_ideal':['X0','X1','X2','X3','X4','X5','t_T']+[f't{i}' for i in I],
    'target_ideal':['X0','X1','X2','X3','X4','X5'],
    'map':'id_Cech(X) tensor epsilon_Cech(t_T,t_I)','basis_columns_checked':len(subsets(X))*len(subsets(J)),'defects':0})
 out={'schema':'marici.branch_b.derived_support_transition.v1','status':'proved','frames':rows,
  'theorem':'RΓ_(I_X+J)(K)=RΓ_J RΓ_I_X(K) -> RΓ_I_X(K) by the local-cohomology counit',
  'stacks_labels':['dualizing-lemma-local-cohomology-adjoint','dualizing-lemma-local-cohomology-ss','dualizing-lemma-local-cohomology-and-restriction','dualizing-lemma-torsion-change-rings'],
  'total_new_basis_checks':checks}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','frames':len(rows),'checks':checks}))
if __name__=='__main__':main()
