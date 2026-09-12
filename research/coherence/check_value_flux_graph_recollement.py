#!/usr/bin/env python3
"""Check the local value/flux trace quotient and Green-kernel channel."""

import json
from fractions import Fraction
from pathlib import Path

def mv(A,v):return [sum(a*x for a,x in zip(r,v)) for r in A]
def rank(A):
 M=[list(map(Fraction,r)) for r in A];r=0
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
 # Coordinates: value-, derivative-, value+, derivative+.
 J=[[-1,0,1,0],[0,-1,0,1]]
 continuous_value_and_flux=[[1,0,1,0],[0,1,0,1]]
 green=[1,1,1,-1]
 jump=mv(J,green)
 assert rank(J)==2 and all(mv(J,v)==[0,0] for v in continuous_value_and_flux)
 assert jump==[0,-2]
 result={'schema':'marici.coherence.value-flux-graph-recollement.v1','jump_map_rank':rank(J),'old_matching_trace_dimension':2,'new_trace_dimension':4,'quotient_dimension':2,'green_kernel_jump':{'value':jump[0],'flux':jump[1]},'massive_distribution_coefficients':{'delta':-jump[1],'delta_prime':-jump[0]},'conclusion':'the Green kernel occupies the flux summand and has zero value-jump component'}
 Path(__file__).with_name('value-flux-graph-recollement.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
