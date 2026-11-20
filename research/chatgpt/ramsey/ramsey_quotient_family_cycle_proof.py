"""Read active components from parallel edges of the quotient. Reflection is coordinate negation, the square of doubling; each pair of parallel bundles lifts to a ten-cycle."""
from collections import Counter
from ramsey_cyclic_binary_coordinates import codes,H
from ramsey_cyclic_quotient_constructor import L,R,B,act
r=[H[H[i]] for i in range(30)];project=lambda e:(next(k for k,s in enumerate(L) if e[0] in s),next(k for k,s in enumerate(R) if e[1] in s))
for (family,x,y),m in sorted(codes.items()):
 n=frozenset(tuple(sorted((r[i],r[j]))) for i,j in m);difference=m^n;bundles=[b for b in B if b<=difference];counts=Counter(project(next(iter(b))) for b in bundles)
 assert len(bundles)==2*(family+1) and set(counts.values())=={2}
 for endpoints in counts:
  a,b=[b for b in bundles if project(next(iter(b)))==endpoints];fa=dict(a);fb=dict(b);inv={v:u for u,v in fb.items()};step={u:inv[v] for u,v in fa.items()};start=min(step);orbit=[start];z=step[start]
  while z!=start:orbit.append(z);z=step[z]
  assert len(orbit)==5
 print('code',(family,x,y),'differing quotient parallel-edge pairs',dict(counts),'lifted ten-cycles',family+1)
