#!/usr/bin/env python3
"""Exact finite model of Yoneda-style joint observation forcing coherencer uniqueness."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def rank(a):
 a=[r[:] for r in a];m=len(a);n=len(a[0]);i=0
 for j in range(n):
  p=next((k for k in range(i,m) if a[k][j]),None)
  if p is None:continue
  a[i],a[p]=a[p],a[i];z=a[i][j];a[i]=[x/z for x in a[i]]
  for k in range(m):
   if k!=i and a[k][j]:c=a[k][j];a[k]=[a[k][l]-c*a[i][l] for l in range(n)]
  i+=1
 return i
I=[[F(1),0],[0,F(1)]];J=[[F(1),0],[0,F(-1)]];B1=[[F(1),0]];B2=[[0,F(1)]];stack=B1+B2
checks={'single_observer_not_faithful':rank(B1)<2,'single_observer_cannot_separate':mm(B1,I)==mm(B1,J),'joint_observer_full_rank':rank(stack)==2,'joint_observer_separates':mm(stack,I)!=mm(stack,J)}
out={'schema':'marici.nima.qRB-yoneda-faithful-truncation.v1','finite_theorem':'For finite-dimensional H, a jointly monic stacked observer B forces U=V whenever BU=BV. Hence the type of observed coherencers is a proposition; existence makes it contractible.','fixture':{'single_observer':['x1'],'joint_observers':['x1','x2'],'stacked_rank':rank(stack)},'checks':checks,'passed':all(checks.values()),'infinite_dimensional_target':{'observer_family':'all source-derived translates and endpoint functionals','separation':'intersection of observer kernels equals the declared radical','density':'closed span of represented observers is the dual test carrier','consequence':'completed qRB filler unique up to contractible coherent choice'},'current_status':'finite mechanism exact; source-derived all-translate density remains open','rh_proved':False}
p=ROOT/'research/nima/results/qRB-yoneda-faithful-truncation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
