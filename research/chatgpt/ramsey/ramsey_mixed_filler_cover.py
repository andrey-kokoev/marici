"""Exact mixed-simplex filler-cover test, for R(3,5), R(3,6),
R(3,7), and R(4,4). Standard Python 3 only.

Lemma: in a coloring with no A K_n or B K_m, take n-1
pairwise disjoint pure B cliques U_i (sizes p_i). Let W be outside.
X_i = {w in W: all edges w--U_i are B}.
F   = outside common A-neighbors across B edges joining different U_i.
Then W = union_i X_i union F and
N <= sum_i (p_i + R(n,m-p_i)-1) + |F|.

The exact inputs are published critical graph6 examples, a 13-vertex
circulant, and the Paley(17) graph. The 22-vertex graph6 string is the
first entry in B. McKay's r37_22.g6 catalogue.
"""
from itertools import combinations

G6_17 = 'P??GaOo`XMGsIcT?pSLaGuA?'
G6_22 = 'U???GOOGIGPB`SQgg[cEoKaagg@iI@w@`ROCrGA?'
R = {(3,2):3,(3,3):6,(3,4):9,(3,5):14,(4,2):4}

def graph6(s):
    n=ord(s[0])-63
    g=[[False]*n for _ in range(n)]
    bits=[(ord(ch)-63>>k)&1 for ch in s[1:] for k in (5,4,3,2,1,0)]
    for (i,j),b in zip(((i,j) for j in range(1,n) for i in range(j)),bits):
        g[i][j]=g[j][i]=bool(b)
    return g

def circulant(n,steps):
    return [[i!=j and min(abs(i-j),n-abs(i-j)) in steps for j in range(n)]for i in range(n)]

def paley17():
    n=17;qr={pow(k,2,n)for k in range(1,n)}
    return [[i!=j and (i-j)%n in qr for j in range(n)] for i in range(n)]

def check(name,A,n,m,blocks):
    N=len(A); t=n-1
    assert len(blocks)==t
    U=set().union(*map(set,blocks))
    assert len(U)==sum(map(len,blocks))
    assert all(not A[i][j] for b in blocks for i,j in combinations(b,2))
    assert not any(all(A[i][j] for i,j in combinations(group,2))
                   for group in combinations(range(N),n))
    assert not any(all(not A[i][j] for i,j in combinations(group,2))
                   for group in combinations(range(N),m))

    W=set(range(N))-U
    regions=[{w for w in W if all(not A[w][u] for u in b)} for b in blocks]
    defects=[(u,v) for i,j in combinations(range(t),2)
             for u in blocks[i] for v in blocks[j] if not A[u][v]]
    F={w for u,v in defects for w in W if A[w][u] and A[w][v]}
    uncovered=W-set().union(*regions)
    assert uncovered <= F
    budget=sum(len(b)+R[(n,m-len(b))]-1 for b in blocks)
    assert N<=budget+len(F)
    # The chosen instances all saturate this bound, with disjoint regions.
    assert N==budget+len(F)
    assert uncovered==F
    assert sum(map(len,regions))==len(set().union(*regions))
    print(f'{name}: N={N}, base={budget}, filler={len(F)}, '
          f'regions={list(map(len,regions))}, witnesses={sorted(F)}')
    return F

if __name__=='__main__':
    check('R(3,5)',circulant(13,{2,3}),3,5,((0,1),(3,4,11)))
    check('R(3,6) 3+3',graph6(G6_17),3,6,((1,4,10),(2,7,16)))
    check('R(3,6) 2+4',graph6(G6_17),3,6,((1,10),(2,6,7,16)))
    check('R(3,7)',graph6(G6_22),3,7,((0,4,8),(3,13,17,21)))
    check('R(4,4)',paley17(),4,4,((0,3),(1,4),(2,5)))
    print('All five exact filler covers passed.')
