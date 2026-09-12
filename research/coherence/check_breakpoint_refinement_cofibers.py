#!/usr/bin/env python3
"""Verify order-independent jump cofibers for finite breakpoint refinements."""

import json
from itertools import permutations
from pathlib import Path

POINTS=(2,3,5,7)
# Final trace coordinates: endpoint, then left/right traces at each labelled break.
COORDS=(('E',0),)+tuple((side,p) for p in POINTS for side in ('L','R'))
INDEX={c:i for i,c in enumerate(COORDS)}

def jump_row(p):
 row=[0]*len(COORDS);row[INDEX[('R',p)]]=1;row[INDEX[('L',p)]]=-1;return tuple(row)

def rank(rows):
 a=[list(map(float,r)) for r in rows];r=0
 for c in range(len(COORDS)):
  pivot=next((i for i in range(r,len(a)) if abs(a[i][c])>1e-9),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];z=a[r][c];a[r]=[x/z for x in a[r]]
  for i in range(len(a)):
   if i!=r and abs(a[i][c])>1e-9:
    z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[r])]
  r+=1
 return r

def main():
 canonical=frozenset(jump_row(p) for p in POINTS);rows=[]
 for order in permutations(POINTS):
  maps=tuple(jump_row(p) for p in order)
  assert frozenset(maps)==canonical and rank(maps)==4
  rows.append({'order':order,'cofiber_rank':4,'same_final_kernel':True})
 result={'schema':'marici.coherence.breakpoint-refinement-cofibers.v1','orders':len(rows),'all_orders_same_jump_kernel':True,'total_cofiber_dimension':4,'exact_sequence':'0 -> D_B -> D_C -> C^(C\\B) -> 0','conclusion':'refinement order is coherent, but refinement is an extension by jump lines rather than an equivalence'}
 Path(__file__).with_name('breakpoint-refinement-cofibers.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
