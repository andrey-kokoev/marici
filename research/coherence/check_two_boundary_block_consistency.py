#!/usr/bin/env python3
"""Rank and compact perturbations for the two-boundary block constraints."""
import json
from fractions import Fraction
from pathlib import Path
import check_two_sided_block_observer_model as block

def rank(A):
 M=[r[:] for r in A];r=0
 for c in range(len(M[0])):
  p=next((i for i in range(r,len(M)) if M[i][c]),None)
  if p is None:continue
  M[r],M[p]=M[p],M[r];q=M[r][c];M[r]=[x/q for x in M[r]]
  for i in range(len(M)):
   if i!=r:
    q=M[i][c];M[i]=[x-q*y for x,y in zip(M[i],M[r])]
  r+=1
 return r
def main():
 rho=Fraction(3,5);rows=[]
 for n in range(2,16):
  A=[[rho**(n-1-i) for i in range(n)],[rho**i for i in range(n)]];assert rank(A)==2
  rows.append({'events':n,'two_boundary_rank':2,'interior_freedom':n-2})
 n=11;sites=(3,5,8);a=[[rho**(n-1-i) for i in sites],[rho**i for i in sites]]
 # Cross product of the two endpoint rows.
 v=[a[0][1]*a[1][2]-a[0][2]*a[1][1],a[0][2]*a[1][0]-a[0][0]*a[1][2],a[0][0]*a[1][1]-a[0][1]*a[1][0]]
 u=[Fraction(0)]*n
 for i,x in zip(sites,v):u[i]=x
 past,future=block.tails(u,rho);assert past[-1]==0 and future[0]==0
 assert all(past[i]==future[i]==0 for i in range(0,sites[0]))
 assert all(past[i]==future[i]==0 for i in range(sites[-1]+1,n))
 result={'schema':'marici.coherence.two-boundary-block-consistency.v1','rank_rows':rows,'boundary_map':'u -> (P_last,F_first)','boundary_rank':2,'fixed_boundary_fiber_dimension':'n-2','compact_hostile':{'sites':sites,'coefficients':[str(x) for x in v],'zero_left_and_right_exterior_tails':True},'conclusion':'two terminal boundary values remove exactly two global degrees; their kernel contains compact compensated event packets invisible outside their support interval'}
 Path(__file__).with_name('two-boundary-block-consistency.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
