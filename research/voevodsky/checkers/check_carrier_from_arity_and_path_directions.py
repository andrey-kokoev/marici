#!/usr/bin/env python3
"""Construct the local carrier from arity and the two Segal directions."""
import json
from pathlib import Path

def rank(vectors):
 A=[list(map(float,v)) for v in vectors];r=0
 for c in range(len(A[0])):
  p=next((i for i in range(r,len(A)) if abs(A[i][c])>1e-12),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];q=A[r][c];A[r]=[x/q for x in A[r]]
  for i in range(len(A)):
   if i!=r:
    q=A[i][c];A[i]=[x-q*y for x,y in zip(A[i],A[r])]
  r+=1
 return r

def main():
 directions=('initial','final')
 a=(1,0,0);nu_i=(0,1,0);nu_f=(0,0,1)
 assert rank([a])==1 and rank([nu_i,nu_f])==2 and rank([a,nu_i,nu_f])==3
 assert rank([a,nu_i])==rank([a,nu_f])==2
 # Coefficient comparison proves intersection span(a).
 for x in range(-3,4):
  for s in range(-3,4):
   for t in range(-3,4):
    if (x,s,0)==(x,0,t):assert s==t==0
 swap=((1,0,0),(0,0,1),(0,1,0))
 def mv(M,v):return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))
 assert mv(swap,a)==a and mv(swap,nu_i)==nu_f and mv(swap,nu_f)==nu_i
 assert all(mv(swap,mv(swap,v))==v for v in (a,nu_i,nu_f))
 result={'schema':'marici.voevodsky.carrier-from-arity-and-path-directions.v1','arity_monoid':'N','arity_group_completion':'Z','arity_realification_rank':1,'path_direction_set':list(directions),'free_direction_space_rank':2,'carrier_construction':'(R tensor_Z N^gp) direct-sum R[{initial,final}]','carrier_rank':3,'initial_plane_rank':2,'final_plane_rank':2,'shared_intersection_rank':1,'reversal_fixes_arity':True,'reversal_exchanges_directions':True,'reversal_involutive':True,'conclusion':'Conditional on a noncollapsed two-element endpoint orbit, free Euclidean linearization produces the rank-three carrier and two planes.','claim_boundary':'Initial/final labels depend on simplex orientation. The 2-Segal axioms alone neither retain a two-element endpoint orbit nor select free Euclidean linearization.'}
 out=Path(__file__).parents[1]/'results'/'carrier_from_arity_and_path_directions.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
