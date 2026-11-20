"""Use six tetrahedral edges as ground labels. Enumerate Hall choices and test only the induced corner action, not the full automorphism group of the unrooted output."""
from itertools import combinations, permutations
from collections import Counter
X=list(combinations(range(4),2)); D=list(combinations(range(6),2)); M=[m for m in combinations(D,3) if len(set(sum(m,())))==6]
G=list(permutations(range(4)))
def action(p):
    e=[X.index(tuple(sorted(p[i] for i in x))) for x in X]; d=lambda v:tuple(sorted(e[i] for i in v))
    return [D.index(d(v)) for v in D],[M.index(tuple(sorted(d(v) for v in m))) for m in M]
acts=list(map(action,G));hist=Counter()
def count(sel,used):
    if len(sel)==15:
        hist[sum(all(sel[a[i]]==b[j] for i,j in enumerate(sel)) for a,b in acts)]+=1;return
    for j,m in enumerate(M):
        if not used>>j&1 and D[len(sel)] in m:count(sel+[j],used|1<<j)
count([],0);assert hist=={1:288};print('Hall choices by tetrahedral stabilizer order:',dict(hist))
