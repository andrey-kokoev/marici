"""Enumerate dictionaries without affine coordinates: conjugate on the output of one known duality by every permutation of the ground labels (the full type-preserving group: maximal intersecting duad families of size five are the six stars). Test the native fan before choosing an exit."""
from itertools import permutations
from collections import Counter
from ramsey_strip_affine_star_dictionary import X,P,T,D,cycle,fixed,pair
fan=P.index(pair(cycle[0],cycle[2]));h=list(range(6))
for a,b in zip(cycle,cycle[1:]+cycle[:1]):h[a]=b
def act(p):
 tr=lambda d:pair(*(p[i] for i in d));return [P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T]
H=act(h);out=Counter();total=0
for p in permutations(range(6)):
 A=act(p);F=[A[D[i]] for i in range(30)]
 if any(F[F[i]]!=i for i in range(30)):continue
 total+=1
 if any(F[H[i]]!=H[F[i]] for i in range(30)):continue
 absolute=[set(d) for i,d in enumerate(P) if d in T[F[i]-15]];pole,=set.intersection(*absolute);out[F[fan],X[pole]]+=1
print('reciprocal',total,'half-step compatible (fan image, absolute star center):',out);assert total==36 and sorted(out.values())==[1]*4
