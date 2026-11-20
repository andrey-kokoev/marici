"""Translation certificate for the 13-point obstruction; test a deletion prediction."""
from itertools import combinations, product
V=range(13)
blue=[frozenset(s) for k in range(14) for s in combinations(V,k)
      if all((j-i)%13 not in {1,5,8,12} for i,j in combinations(s,2))]
Q=[s for s in blue if len(s)==4]
shift=lambda s,d:frozenset((x+d)%13 for x in s)
reps=[frozenset(s) for s in [(0,2,4,6),(0,2,6,9),(0,3,6,9)]]
assert len(Q)==39 and {shift(s,d) for s in reps for d in V}==set(Q)
assert all(any(s<=q for q in Q) for s in blue)
D={(i,j):{d for d in V if all(q&a or q&shift(b,d) for q in Q)}
   for i,a in enumerate(reps) for j,b in enumerate(reps)}
for i,j,k in product(range(3),repeat=3):
    assert not ({(x+y)%13 for x in D[i,j] for y in D[j,k]} & D[i,k])
print('Compatible pair offsets:',{p:sorted(s) for p,s in D.items()});print('No compatible triangle.')
rows=[{1,3,5,7},{1,5,8,12},{2,4,6,8}];assert all(a in Q for a in rows)
bad=[b for b in blue if len(b)+sum(not b&a for a in rows)>=6];assert bad and all(0 in b for b in bad)
print('Obstructions for proposed triple:',len(bad),'all contain 0; deleting 0 suffices.')
