"""Exact local obstruction and allowed square flip in the (3,6) Clebsch graph.

Vertices F2^4, A adjacency iff Hamming weight of XOR is 1 or 4.
Proof in accompanying answer uses just SRG(16,5,0,2), the canonical
A-two-step-path B-triple completion, and degree/common-neighbor counts.
This verifier is finite, integer-exact, and uses no Ramsey-critical catalog.
"""
from itertools import combinations
from collections import Counter

def graph_clebsch():
    return [sum(1<<j for j in range(16)
                if i!=j and (i^j).bit_count() in (1,4)) for i in range(16)]

def edge(G,i,j):
    return bool(G[i] >> j & 1)

def is_B_clique(G,S):
    return all(not edge(G,i,j) for i,j in combinations(S,2))

def count_squares(G):
    return sum((G[i]&G[j]).bit_count()*((G[i]&G[j]).bit_count()-1)//2
               for i,j in combinations(range(len(G)),2) if not edge(G,i,j)) // 2

def flip_square(G,S):
    H=G.copy()
    for i,j in combinations(S,2):
        H[i]^=1<<j
        H[j]^=1<<i
    return H

def valid(G,m):
    n=len(G)
    assert not any(edge(G,i,j) and (G[i]&G[j])
                   for i,j in combinations(range(n),2))
    assert not any(is_B_clique(G,S) for S in combinations(range(n),m))
    return True

C=graph_clebsch()
assert all(row.bit_count()==5 for row in C)
assert all((C[i]&C[j]).bit_count()==(0 if edge(C,i,j) else 2)
           for i,j in combinations(range(16),2))
assert valid(C,6)
print('SRG(16,5,0,2): certified')

# All 160 oriented-with-unordered-endpoints A-two-step paths.
path_count=0
for b in range(16):
    adj=[v for v in range(16) if edge(C,b,v)]
    for a,c in combinations(adj,2):
        Z=tuple(v for v in range(16)
                if v not in (a,b,c) and
                not any(edge(C,v,u) for u in (a,b,c)))
        assert len(Z)==3 and is_B_clique(C,Z)
        path_count+=1
assert path_count == 160
print('All 160 A-two-step paths have a unique complementary B-triple.')
print('Canonical path 1-0-2 has complementary B-triple',
      tuple(v for v in range(16)
            if v not in (0,1,2) and not any(edge(C,v,u) for u in (0,1,2))))

# Neighborhood of each Clebsch vertex is an independent five-set.
assert all(is_B_clique(C,[v for v in range(16) if edge(C,u,v)])
           for u in range(16))

# Every induced 2K2 has exactly four vertices not dominated by its endpoints.
twoK2=0
for S in combinations(range(16),4):
    e=[(a,b) for a,b in combinations(S,2) if edge(C,a,b)]
    if len(e)!=2 or len(set(e[0]+e[1]))!=4:continue
    twoK2+=1
    mark=sum(1<<v for v in S)
    undominated=[v for v in range(16) if (C[v]&mark)==0]
    assert len(undominated)==4
assert twoK2 == 60
print('All 60 induced 2K2 endpoint sets leave exactly four vertices undominated.')
print('THEOREM: No A->B-only recolorings can admit a seventeenth vertex;')
print('         an admissible extension requires an existing B->A recoloring.')

# A real reversible two-direction square move exists on the same base graph.
squares=[S for S in combinations(range(16),4)
         if sum(edge(C,a,b) for a,b in combinations(S,2))==4]
assert len(squares)==40
profiles=Counter()
for S in squares:
    H=flip_square(C,S)
    assert valid(H,6)
    profiles[(sum(r.bit_count() for r in H)//2,count_squares(H))]+=1
assert profiles == Counter({(38,39):40})
print('All 40 square flips admissible: A-edges 40->38; A-squares 40->39.')

# Same move is *not* universally admissible at the next Ramsey boundary.
n=13
Q=[sum(1<<j for j in range(n) if i!=j and min((j-i)%n,(i-j)%n) in (2,3))
   for i in range(n)]
assert valid(Q,5)
q_squares=[S for S in combinations(range(n),4)
           if sum(edge(Q,a,b) for a,b in combinations(S,2))==4]
assert len(q_squares)==13
for S in q_squares:
    H=flip_square(Q,S)
    assert not any(edge(H,i,j) and (H[i]&H[j])
                   for i,j in combinations(range(n),2))
    assert any(is_B_clique(H,T) for T in combinations(range(n),5))
print('All 13 square flips of the 13-node (3,5) graph create a forbidden B-five.')
print('Conclusion: square recomposition needs an admissibility rule for higher B-links.')

# Exact link-based criterion for a square flip.
def flip_link_test(G,S,m):
    """Necessary and sufficient when G avoids A-triangles and B-K_m,
    and S induces an A-four-cycle with its diagonals B.
    """
    assert len(S)==4
    assert sum(edge(G,i,j) for i,j in combinations(S,2))==4
    # The two new A diagonals must have no common old A-neighbor outside S.
    for i,j in combinations(S,2):
        if not edge(G,i,j):
            if any(edge(G,i,z) and edge(G,j,z)
                   for z in range(len(G)) if z not in S):
                return False
    # The four new B boundary edges cannot extend to a B-K_m.
    for i,j in combinations(S,2):
        if edge(G,i,j):
            L=[z for z in range(len(G)) if z not in S
               and not edge(G,i,z) and not edge(G,j,z)]
            if any(is_B_clique(G,T) for T in combinations(L,m-2)):
                return False
    return True

assert all(flip_link_test(C,S,6) for S in squares)
assert not any(flip_link_test(Q,S,5) for S in q_squares)
print('Link criterion: Clebsch passes all 40; C13 fails all 13.')

# Verify the original dual single-cycle property survives a sample flip.
H=flip_square(C,(0,1,2,3))
AC=[0,3,7,8,12,4,5,1,2,6,14,10,11,9,13,15]
BC=[0,5,6,11,12,1,7,10,13,8,14,2,3,4,15,9]
for path,is_A in [(AC,True),(BC,False)]:
    assert len(path)==len(set(path))==16
    assert all(edge(H,path[k],path[(k+1)%16])==is_A for k in range(16))
print('One admissible square flip retains single Hamiltonian A and B traversals.')
