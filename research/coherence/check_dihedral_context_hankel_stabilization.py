#!/usr/bin/env python3
"""Compute finite-depth Hankel ranks for the residual translation/reversal alphabet."""

import json, random
from fractions import Fraction
from itertools import product
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def mv(A,v):return [sum(A[i][k]*v[k] for k in range(2)) for i in range(2)]
def rank(M):
 A=[r[:] for r in M];rows=len(A);cols=len(A[0]);r=0
 for c in range(cols):
  p=next((i for i in range(r,rows) if A[i][c]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];z=A[r][c];A[r]=[x/z for x in A[r]]
  for i in range(rows):
   if i!=r and A[i][c]:
    z=A[i][c];A[i]=[x-z*y for x,y in zip(A[i],A[r])]
  r+=1
 return r
def words(h):return [w for n in range(h+1) for w in product((0,1),repeat=n)] # 0=T,1=R
def rep(w,T,R):
 A=[[Fraction(1),0],[0,Fraction(1)]]
 for x in w:A=mm(A,T if x==0 else R)
 return A
def main():
 rng=random.Random(20260912);rows=[]
 for trial in range(40):
  z=Fraction(rng.randrange(2,12),rng.randrange(2,12))
  if z==1:continue
  T=[[z,0],[0,1/z]];R=[[0,Fraction(1)],[Fraction(1),0]]
  alpha=[Fraction(rng.randrange(1,9)),Fraction(rng.randrange(1,9))];beta=[Fraction(rng.randrange(1,9)),Fraction(rng.randrange(1,9))]
  ranks=[]
  for h in range(5):
   W=words(h);H=[]
   for u in W:
    row=[]
    for v in W:
     x=mv(rep(u+v,T,R),beta);row.append(sum(alpha[i]*x[i] for i in range(2)))
    H.append(row)
   ranks.append(rank(H))
  assert all(x<=2 for x in ranks) and ranks[-1]==2 and ranks==sorted(ranks)
  rows.append({'trial':trial,'z':str(z),'ranks_depth_0_to_4':ranks,'stabilized_rank':2})
 result={'schema':'marici.coherence.dihedral-context-hankel-stabilization.v1','constructor_alphabet':['T_z','R'],'relations':['R^2=I','R T_z R=T_z^-1'],'cases':len(rows),'all_ranks_nondecreasing_and_at_most_two':True,'all_stabilize_at_two':True,'conclusion':'the stationary hyperbolic double is the minimal context-closed realization for generic probes of the T/R protocol'}
 Path(__file__).with_name('dihedral-context-hankel-stabilization.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('constructor_alphabet','cases','all_stabilize_at_two','conclusion')},indent=2))
if __name__=='__main__':main()
