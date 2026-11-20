"""Sharp direct forbidden-pattern width on original edge variables, no auxiliary variables."""
from itertools import combinations
E=list(combinations(range(7),2));idx={e:i for i,e in enumerate(E)}
tri=[sum(1<<idx[e] for e in combinations(t,2)) for t in combinations(range(7),3)]
# Subset DP: bad iff removing the lowest red edge leaves a triangle or that edge closes one.
closing=[[(m^(1<<i)) for m in tri if m>>i&1] for i in range(21)]
bad=bytearray(1<<21)
for r in range(1,len(bad)):
    b=r&-r;rest=r^b;bad[r]=bad[rest] or any(rest&m==m for m in closing[b.bit_length()-1])
def legal(r):return bool(r) and not bad[r]
assert not legal(0) and all(legal(1<<i) for i in range(21))
print('blank K7:',sum(map(legal,range(len(bad)))),'legal of',len(bad))
free=[idx[e] for e in [(0,1),(2,3),(4,5)]]
assert sum(legal(sum(1<<i for j,i in enumerate(free) if m>>j&1)) for m in range(8))==7
print('three blank matching edges, other 18 blue: 7 legal of 8')
