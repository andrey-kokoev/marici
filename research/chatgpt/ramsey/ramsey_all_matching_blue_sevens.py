"""Check whether absence of blue sevens is specific to affine choices or holds for all 288 incident perfect matchings."""
from collections import Counter
from ramsey_strip_minimal_shared_constraints import allms
from ramsey_strip_short_output_isomorphism import graph
hist=Counter()
for m in allms:
 N=graph(m);bits=[sum(1<<x for x in s) for s in N]
 def count(mask,k):
  if not k:return 1
  if mask.bit_count()<k:return 0
  total=0
  while mask:
   b=mask&-mask;mask^=b;total+=count(mask&~bits[b.bit_length()-1],k-1)
  return total
 hist[count((1<<22)-1,7)]+=1
print('independent seven-sets -> matching count',dict(hist))
