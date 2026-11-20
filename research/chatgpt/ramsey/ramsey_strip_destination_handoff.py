"""Separate acting by a destination row on a tetrahedral edge from reading the other edge of its Hall block. Test both literal row handoffs in 1-based column notation."""
from itertools import combinations
rows=('BRNN','BNRN');V=set(range(1,5));edges={frozenset(e) for e in combinations(sorted(V),2)}
def roles(row):
    br=frozenset(i for i,c in enumerate(row,1) if c in 'BR');return br,frozenset(V-br)
def perm(row):
    return {x:y for e in roles(row) for x in e for y in e if y!=x}
def image(f,e):return frozenset(f[x] for x in e)
for src,dst in ((0,1),(1,0)):
    b,n=roles(rows[dst]);incoming=roles(rows[src])[0];assert len(incoming&n)==1
    f=perm(rows[dst]);assert image(f,n)==n and image(f,b)==b
    # The exit duad is unordered. If it is an input/output relation with distinct outputs, the mate is unique.
    mate,=set(roles(rows[dst]))-{n};assert mate==b and mate!=incoming
    print('arrive on',sorted(n),'row permutation gives',sorted(image(f,n)),'other member gives',sorted(mate),'reverse shared-corner step gives',sorted(incoming))
