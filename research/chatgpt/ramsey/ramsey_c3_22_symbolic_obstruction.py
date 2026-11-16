"""Independent elementary finite certificate for the C3 axial-vertex obstruction.

The theorem: no triangle-free graph on 15 vertices, partitioned into five
orbits of length 3 under a color-preserving C3 automorphism, has alpha<=5.
Consequently no (3,7)-Ramsey graph on 22 vertices admits a C3 action with
seven length-3 orbits and one fixed vertex.

Proof reduction: 5 C3-orbits are internally independent; each pair must
have at least one A matching to avoid B6. Select one matching from each pair,
normalize the gains on the four spokes at vertex 0, and the remaining signs
form an acyclic tournament on four vertices. Relabel to the canonical graph.
All additional A-orbits (matchings) preserving triangle-freeness form the
five edges of a C5. Since every vertex initially has A-degree 4, no base
orbit can touch two additions without creating an independent B6 in its
A-neighborhood; hence additions are a matching of C5 (0, 1 or 2 edges).
A displayed automorphism acts cyclically on the five possible additions.
The 3 canonical cases have explicit independent B6 witnesses.
"""
from itertools import combinations

K=5
N=3*K
D={(i,j):(0 if i==0 else 1) for i,j in combinations(range(K),2)}
# extra A-matchings ordered as the C5 (0-1-2-3-4-0)
E=[(0,1,1),(1,2,2),(2,3,2),(3,4,2),(0,4,2)]

def connections(additions=()):
    A=[0]*N
    for (i,j),d in D.items():
        shifts=[d]+[dd for x,y,dd in additions if (x,y)==(i,j)]
        for shift in shifts:
            for a in range(3):
                u=3*i+a
                v=3*j+(a+shift)%3
                A[u] |=1<<v
                A[v] |=1<<u
    return A

def is_independent(A, vertices):
    return all(not(A[u]>>v&1) for u,v in combinations(vertices,2))

def is_triangle_free(A):
    return all(not (A[i]&A[j]) for i,j in combinations(range(N),2) if (A[i]>>j)&1)

base=connections()
assert is_triangle_free(base)
assert {z.bit_count() for z in base}=={4}

# The canonical gain system has only five possible individual extra
# rotational matchings that preserve triangle-freeness.
extras=[]
for (i,j),d in D.items():
    for other in set(range(3))-{d}:
        ext=(i,j,other)
        if is_triangle_free(connections((ext,))):
            extras.append(ext)
assert set(extras)==set(E)

# Explicit cyclic automorphism of the canonical base and the 5 extras.
p=[3,4,5,7,8,6,10,11,9,13,14,12,0,1,2]
assert sorted(p)==list(range(N))

def image_of_edges(A):
    B=[0]*N
    for u,v in combinations(range(N),2):
        if A[u]>>v&1:
            B[p[u]] |=1<<p[v]
            B[p[v]] |=1<<p[u]
    return B

assert image_of_edges(base)==base
for k in range(5):
    assert image_of_edges(connections([E[k]])) == connections([E[(k+1)%5]])

# By rotational symmetry, all matchings of the C5 reduce to these 3 cases.
representatives=[(),(E[0],),(E[0],E[2])]
witnesses=[(0,1,5,8,11,14),
           (0,5,7,8,10,13),
           (0,5,8,11,13,14)]
for additions,witness in zip(representatives,witnesses):
    A=connections(additions)
    assert is_triangle_free(A)
    assert is_independent(A,witness)
    print('Added matchings:',additions,'-> B6 witness:',witness)

admissible_extra_sets=[]
for r in range(3):
    for choices in combinations(range(5),r):
        if any((i-j)%5 in (1,4) for i,j in combinations(choices,2)):
            continue
        additions=tuple(E[i] for i in choices)
        A=connections(additions)
        assert is_triangle_free(A)
        admissible_extra_sets.append(choices)
        assert any(is_independent(A,tuple(pw))
                   for pw in combinations(range(N),6))
assert len(admissible_extra_sets)==11
print('11/11 admissible extra-matching patterns retain B6.')
print('THEOREM: A C3-free 15-node triangle-free graph has an independent six-set.')
print('COROLLARY: A fixed axial connector cannot extend 7 rotational triples to 22 Ramsey(3,7) nodes.')
