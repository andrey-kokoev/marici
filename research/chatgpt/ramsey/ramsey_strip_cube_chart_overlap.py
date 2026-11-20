"""Compare cube coordinate charts by identity on common partitions, not by choosing a global symmetry. Determine whether chart overlap extends uniquely to a cube isometry."""
from itertools import product,permutations,combinations
from collections import Counter
from ramsey_strip_opposite_partition_transport import T,moves
charts=[]
for i,A in enumerate(T):
 colors=sorted(A);F={}
 for j,B in enumerate(T):
  if A&B:continue
  for d in B:
   c,=[k for k,a in enumerate(colors) if set(a).isdisjoint(d)];F[j,c]=moves[i,j,d]
 origin=min(j for j,B in enumerate(T) if not A&B);chart={}
 for bits in product((0,1),repeat=3):
  j=origin
  for c,b in enumerate(bits):
   if b:j=F[j,c]
  chart[j]=bits
 charts.append(chart)
hist=Counter()
for a,b in combinations(range(15),2):
 shared=charts[a].keys()&charts[b].keys();S=[charts[a][j] for j in shared];ed=sum(sum(x!=y for x,y in zip(u,v))==1 for u,v in combinations(S,2));extensions=[]
 for perm in permutations(range(3)):
  for shift in product((0,1),repeat=3):
   if all(tuple(charts[a][j][perm[k]]^shift[k] for k in range(3))==charts[b][j] for j in shared):extensions.append((perm,shift))
 hist[len(T[a]&T[b]),len(shared),ed,len(extensions)]+=1
print('(reference shared blocks, overlap vertices, overlap cube edges, full cube isometry extensions):',dict(hist))
