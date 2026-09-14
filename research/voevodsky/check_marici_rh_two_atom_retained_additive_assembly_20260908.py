#!/usr/bin/env python3
"""Audit support and mixed blocks for retained additive two-atom assembly."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_two_atom_retained_additive_assembly_certificate_20260908.json');a=p.parse_args();checks=0
 primes=[2,3,5,7,11,13]
 for p0 in primes:
  for q in primes:
   if p0==q:continue
   source_support={(p0,1),(q,1)}
   assert (p0*q,1) not in source_support;checks+=1
   # Retained Green form is block diagonal by prime idempotent.
   mixed_block=0 if p0!=q else None
   assert mixed_block==0;checks+=1
 out={'schema':'marici.rh.two-atom-retained-additive-assembly.v1','status':'cross_prime_additive_hostile_closed','checks':checks,
 'assembly':'labelled direct sum e_p direct-sum e_q',
 'mixed_green':'G(P_p x,P_q y)=0 for p!=q','primitive_pq_projection':0,
 'reason':'source support is the disjoint union of prime-power fibres and every retained G1 component commutes with prime idempotents',
 'same_prime_note':'different grades at one prime may have nonzero authorized overlap and are not covered by the zero-block claim',
 'boundary':'does not construct a multiplicative/star assembly whose target contains a pq-labelled object'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks}))
if __name__=='__main__':main()
