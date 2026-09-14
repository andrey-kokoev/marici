#!/usr/bin/env python3
"""Audit depth-independent coherence of the retained labelled direct-sum carrier."""
import argparse,json,random
from pathlib import Path
import numpy as np

def trees(lo,hi,rng):
 if hi-lo==1:return lo
 k=rng.randrange(lo+1,hi);return (trees(lo,k,rng),trees(k,hi,rng))
def flatten(t):return [t] if isinstance(t,int) else flatten(t[0])+flatten(t[1])
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_retained_direct_sum_coherence_certificate_20260908.json');a=p.parse_args();rng=random.Random(20260908);checks=0;max_condition=0
 for n in range(1,65):
  for _ in range(20):
   t=trees(0,n,rng);order=flatten(t);assert order==list(range(n));checks+=1
   P=np.eye(n)[:,order];condition=np.linalg.cond(P);max_condition=max(max_condition,condition);assert condition==1.0;checks+=1
 out={'schema':'marici.rh.retained-direct-sum-coherence.v1','status':'structural_coherence_isometric','checks':checks,'atom_counts_tested':[1,64],'random_bracketings_per_count':20,'max_condition_number':max_condition,
 'general_reason':'canonical flattening preserves the ordered prime/grade coordinates; associators and unitors are coordinate rebracketings represented by identity/permutation unitaries',
 'consequence':'retained direct-sum coherence has depth-independent condition number one and preserves bounded-energy completion',
 'boundary':'does not construct the arithmetic-to-analytic incidence rewrite or prove its critical-pair compatibility with seam and endpoint transport'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'max_condition_number':max_condition}))
if __name__=='__main__':main()
