"""Exhaustive induced-core replacement gate; labels 1..47 survive."""
from test_r312_extension import full, maximal
from collections import Counter
from itertools import combinations_with_replacement

core = full ^ 1
sets = list(maximal(0,core,0))
assert max(map(int.bit_count,sets)) == 11
large = [s for s in sets if s.bit_count()==11]
# Start from maximal neighborhoods hitting all 11-sets; enumerate *all*
# their hitting subsets, since shrinking can enable an edge between newcomers.
legal = set()
for m in sets:
    if all(m&s for s in large):
        t=m
        while t:
            if all(t&s for s in large): legal.add(t)
            t=(t-1)&m
print('core 11-sets',len(large),'legal single neighborhoods by size',sorted(Counter(t.bit_count() for t in legal).items()))
results=Counter()
for a,b in combinations_with_replacement(sorted(legal),2):
    if not a&b: results['adjacent feasible']+=1
    # Nonadjacent newcomers cannot both avoid any independent old 10-set.
    alpha=max((s & ~(a|b)).bit_count() for s in sets)
    results['nonadjacent residual alpha',alpha]+=1
print(results)
