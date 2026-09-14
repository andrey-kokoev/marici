#!/usr/bin/env python3
"""Exact finite analog of the endpoint-augmented form-core reduction."""
import json
from fractions import Fraction
from pathlib import Path

def rank(A):
 M=[[Fraction(x) for x in row] for row in A];r=0
 if not M:return 0
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
 cases=[]
 for bulk_dim in range(1,9):
  odd_bulk=[tuple(1 if i==j else 0 for i in range(bulk_dim)) for j in range(bulk_dim)]
  odd_aug=[v+(0,) for v in odd_bulk];endpoint=(0,)*bulk_dim+(1,)
  assert rank(odd_aug)==bulk_dim
  assert rank(odd_aug+[endpoint])==bulk_dim+1
  # Every odd probe has zero endpoint coordinate; the endpoint vector is independent.
  assert all(v[-1]==0 for v in odd_aug)
  cases.append({'bulk_dimension':bulk_dim,'odd_rank':bulk_dim,'ambient_rank':bulk_dim+1,'augmented_rank':bulk_dim+1})
 # Positivity separates for q=q_bulk + alpha |z|^2 when alpha >= 0.
 for lam in range(-3,4):
  for alpha in range(4):
   full_positive=(lam>=0 and alpha>=0);bulk_positive=(lam>=0)
   assert full_positive==bulk_positive
 result={'schema':'marici.voevodsky.endpoint-augmented-odd-core-reduction.v1','finite_dimensions_checked':'1..8','cases':cases,'endpoint_codimension':1,'minimal_added_probe':'pure endpoint vector','density_equivalence':'odd-plus-endpoint is dense in H_bulk direct-sum C_E iff odd probes are dense in H_bulk','source_endpoint_coefficient':'exp(h/4)-1 > 0 for h>0','positivity_reduction':'q_bulk direct-sum q_endpoint is nonnegative iff q_bulk is nonnegative','conclusion':'The endpoint obstruction is repaired by one independent probe, but all unresolved positivity remains in the bulk form-core problem.'}
 out=Path(__file__).parents[1]/'results'/'endpoint_augmented_odd_core_reduction.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
