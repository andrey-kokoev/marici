"""Column positions 1,2,3,4 are corners. Test the transposition (23) as a relabeling, not a new link-color axiom."""
from itertools import combinations,permutations,product
from collections import Counter
V=(1,2,3,4);g={1:1,2:3,3:2,4:4};X=[(i,) for i in V]+list(permutations(V,2))+[('e',*t) for t in combinations(V,2)]
def image(x):return ('e',*sorted(g[i] for i in x[1:])) if x[0]=='e' else tuple(g[i] for i in x)
def seed(f):
    red=set()
    def link(x,y):red.add(frozenset((x,y)))
    for i in V:
        for j in V:
            if j!=i and j!=f[i]:link((i,),(i,j));link((i,f[i]),(i,j))
    for i,j in combinations(V,2):link((i,j),('e',i,j));link((j,i),('e',i,j))
    n={x:{z for y in red if x in y for z in y if z!=x} for x in X};return {frozenset((x,y)):('R' if y in n[x] else 'B' if n[x]&n[y] else '?') for x,y in combinations(X,2)}
fixed=[]
for dest in product(*[set(V)-{i} for i in V]):
    f=dict(zip(V,dest));h={g[i]:g[j] for i,j in f.items()};s=seed(f);t=seed(h);assert all(t[frozenset(map(image,e))]==v for e,v in s.items())
    if s==t:fixed.append(dest)
    if dest==(2,1,4,3):print('selected seed:',Counter((v,t[e]) for e,v in s.items()));assert s[frozenset(((1,),(1,2)))]=='B' and s[frozenset(((1,),(1,3)))]=='R'
print('fixed choices',sorted(fixed));assert len(fixed)==3
