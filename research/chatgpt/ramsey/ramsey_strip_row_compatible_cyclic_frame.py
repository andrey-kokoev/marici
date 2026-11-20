"""Which short-cycle fillings have an intrinsic C5 frame preserved by the original row swap? If compatible, center the affine coordinates at its non-hub fixed label and test doubling squared."""
from ramsey_strip_intrinsic_fivefold_transport import symmetry,action,I,comp
from ramsey_strip_unbiased_three_constraints import selected,allms
r6=(1,0,2,3,5,4)
for n,pair in enumerate(selected,1):
 for o,j in enumerate(pair):
  m=allms[j];G,hub=symmetry(m);normal={comp(r6,comp(g,r6)) for g in G}==G
  print('filling',n,'orientation',o,'hub',hub,'row swap preserves cyclic frame',normal)
  if not normal:continue
  anchor,=[x for x in I if r6[x]==x and x!=hub];g=min(g for g in G if g!=I);ring=[anchor]
  for _ in range(4):ring.append(g[ring[-1]])
  q=list(I)
  for i,x in enumerate(ring):q[x]=ring[2*i%5]
  assert comp(q,q)==r6
  print(' anchored at',anchor,'doubling',q,'square is literal row swap',True)
