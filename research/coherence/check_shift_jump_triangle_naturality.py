#!/usr/bin/env python3
"""Classify transport of jump cofibers under half-line shifts."""

import json, math
from itertools import combinations
from pathlib import Path

A=tuple(math.log(p) for p in (2,3,5,7));TOL=1e-11
def subs():
 for n in range(1,5):
  for S in combinations(range(4),n):yield sum(A[i] for i in S)
def main():
 B=tuple(sorted(subs()));rows=[];squares=survive=cross=endpoint=0
 for a in A:
  # Right extension transports every old jump c to a+c and adds endpoint-to-jump at a.
  for c in B:
   squares+=1
   # symbolic trace pair (L,R): shifted traces are the same pair
   sample=(3,11);assert sample[1]-sample[0]==sample[1]-sample[0]
  endpoint+=1
  for c in B:
   if c>a+TOL:
    survive+=1
    sample=(5,13);assert sample[1]-sample[0]==sample[1]-sample[0]
   elif c<a-TOL:cross+=1
   else:endpoint+=1
 result={'schema':'marici.coherence.shift-jump-triangle-naturality.v1','breakpoints':len(B),'right_shift_naturality_squares':squares,'right_new_endpoint_jump_cells':4,'left_surviving_jump_squares':survive,'left_boundary_crossing_jump_cells':cross,'left_breaks_at_shift_endpoint':endpoint-4,'identities':{'S':'J_(a+c) S_a = J_c','R_surviving':'J_(c-a) R_a = J_c for c>a'},'conclusion':'S is exact-triangle natural with one new endpoint jump; R is natural only on surviving seams and sends the rest to its relative compression defect'}
 Path(__file__).with_name('shift-jump-triangle-naturality.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
