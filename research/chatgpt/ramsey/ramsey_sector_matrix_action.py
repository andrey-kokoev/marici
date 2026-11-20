"""Check a 12-element action on binary tables, not on graph vertices."""
from itertools import permutations, product

P = tuple(permutations(range(3)))
G = tuple(product(P, (0, 1)))

def compose(p, q):
    return tuple(p[q[i]] for i in range(3))

def perm_mask(m, p):
    return sum(((m >> i) & 1) << p[i] for i in range(3))

def act(B, g):
    p, e = g
    out = [[0]*7 for _ in range(3)]
    for i in range(3):
        for m in range(1,8):
            out[p[i]][perm_mask(m,p)-1] = B[i][m-1] ^ e
    return tuple(map(tuple,out))

if __name__ == '__main__':
    B = tuple(tuple((m>>i)&1 for m in range(1,8)) for i in range(3))
    probe = ((1,1,0,0,0,0,0),(0,0,0,1,0,0,0),(0,0,0,0,0,0,0))
    for g,h in product(G,repeat=2):
        assert act(act(probe,h),g)==act(probe,(compose(g[0],h[0]),g[1]^h[1]))
    assert len({act(probe,g) for g in G})==12
    print('actions:',len(G),'fixed membership table:',sum(act(B,g)==B for g in G),'distinct tables:',len({act(B,g) for g in G}))
    print('membership marks:',sum(map(sum,B)),'nonmembership marks:',21-sum(map(sum,B)))
