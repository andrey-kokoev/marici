"""Classify every matching invariant under one C5, not just known outputs. Use the asymmetric-arrow step set as an intrinsic finite classification."""
from collections import Counter
from ramsey_strip_intrinsic_fivefold_transport import symmetry,long,action,moved,P,T,I
from ramsey_strip_minimal_shared_constraints import allms
G,hub=symmetry(long);g=min(p for p in G if p!=I);ring=[min(set(I)-{hub})]
for _ in range(4):ring.append(g[ring[-1]])
c={x:i for i,x in enumerate(ring)};matches=[m for m in allms if all(moved(m,action(p))==m for p in G)];signatures={}
for m in matches:
 steps=Counter()
 for d,j in m:
  x,y=P[d]
  if hub in (x,y):continue
  block,=[p for p in T[j-15] if hub in p];z,=set(block)-{hub}
  if (c[x]+c[y]-2*c[z])%5==0:continue
  if (2*c[y]-c[x]-c[z])%5:x,y=y,x
  steps[(c[y]-c[x])%5]+=1
 key=tuple(sorted(steps));assert key not in signatures;signatures[key]=m
 if len(key)==2:
  root,=[a for a in key if 3*a%5 in key];assert {root,3*root%5}==set(key)
print('C5-invariant matchings',len(matches),'distinct arrow step sets',sorted(signatures));assert len(matches)==8
# Multiplication by two preserves both families, each a four-cycle.
p=list(I)
for x,i in c.items():p[x]=ring[2*i%5]
H=action(p)
for key,m in sorted(signatures.items()):
 dest=tuple(sorted(2*x%5 for x in key));assert moved(m,H)==signatures[dest]
print('doubling: two four-cycles, one per family; square reverses all cyclic arrows')
