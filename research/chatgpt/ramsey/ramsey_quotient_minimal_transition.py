"""Compare minimum-support moves inside one cyclic frame to row-comparison minimization globally. Minimality in a fixed frame is a distinct condition."""
from collections import Counter
from itertools import combinations
from ramsey_cyclic_binary_coordinates import codes,H
from ramsey_strip_minimal_shared_constraints import allms
from ramsey_strip_matching_restart import turn
adj={key:set() for key in codes}
for a,b in combinations(codes,2):
 if len(codes[a]^codes[b])==10:adj[a].add(b);adj[b].add(a)
print('minimum-support quotient move adjacency',{k:sorted(v) for k,v in sorted(adj.items())})
r=[H[H[i]] for i in range(30)]
for (family,x,y),m in codes.items():
 mate=frozenset((r[i],r[j]) for i,j in m);assert mate==codes[family,1-x,1-y]
 assert ((family,1-x,1-y) in adj[family,x,y])==(family==0)
print('full matching census row-difference sizes',dict(sorted(Counter(len(m^turn(m)) for m in allms).items())))
