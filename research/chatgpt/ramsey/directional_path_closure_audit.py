#!/usr/bin/env python3
"""Typed endpoint and closed-circle audit for the Ramsey directional research note.

Checks endpoint closure only; no higher coherence witnesses or Ramsey graph
extension theorem is inferred from these results.
"""
import itertools
import json
from collections import Counter
from pathlib import Path

N=13
D=frozenset((0,1,3,9))
shift=lambda B,i:frozenset((x+i)%N for x in B)
minus=lambda B:frozenset((-x)%N for x in B)
blocks=sorted({tuple(sorted(shift(D,i))) for i in range(N)} |
              {tuple(sorted(shift(minus(D),i))) for i in range(N)})
assert len(blocks)==26

def is_closed_four_block(B,allow_reverse_r=False):
    for p in itertools.permutations(B):
        if all((p[(i+1)%4] == (p[i]+1)%N or
                p[(i+1)%4] == (-p[i])%N or
                (allow_reverse_r and p[(i+1)%4] == (p[i]-1)%N))
               for i in range(4)):
            return True
    return False

for n in (8,16,32):
    m=n//2
    # Any permutation of exactly m r steps and one s step is closed.
    examples={tuple('r'*j+'s'+'r'*(m-j)) for j in range(m+1)}
    assert len(examples)==m+1
    for word in examples:
        assert (word.count('r') + m*word.count('s'))%n==0

# Same-letter multiset produces opposite closure outcomes in D13.
def action_D13(word,start=0):
    x=start
    for z in word:
        x=(x+1)%N if z=='r' else (-x)%N
    return x
assert action_D13('rsrs',0)==0
assert action_D13('rrss',0)==2

result={
  'seed_block':[0,1,3,9],
  'unique_reflection_closed_blocks':len(blocks),
  'steiner_blocks_with_simple_closed_four_point_r_s_cycle':sum(is_closed_four_block(B) for B in blocks),
  'steiner_blocks_with_simple_closed_four_point_r_reverse_r_s_cycle':sum(is_closed_four_block(B,True) for B in blocks),
  'cyclic_central_inversion_closure':{str(n): {'n':n,'multiset_r':n//2,'multiset_s':1,
                                'distinct_gluing_orders':n//2+1,'all_closed':True}
                                for n in (8,16,32)},
  'mirror_reflection_order_dependency':{
      'words':['rsrs','rrss'],
      'start':0,
      'final_positions':[action_D13('rsrs'),action_D13('rrss')],
      'both_orders_typed':True,
      'both_orders_closed':False
  },
  'scope':'A closed 4-cycle is required to visit each block point exactly once using only primitive steps. Paths may not leave the chosen four-point carrier. Does not test higher paths through other vertices or existence of higher coherence witnesses.'
}
path=Path('/mnt/data/directional_path_closure_audit.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
