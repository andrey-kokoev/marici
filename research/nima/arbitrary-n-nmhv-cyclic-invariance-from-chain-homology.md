# Arbitrary-n NMHV cyclic invariance from chain homology

## Setup

Let `C_4([n])` be the oriented simplicial four-chain group on the `n` cyclically labelled vertices. Define the BCFW chain

$$
T_n
=
\sum_{2\le i\le n-2\atop i+2\le j\le n-1}
[n,i-1,i,j-1,j].
$$

Let `rho` be the cyclic relabelling `a -> a+1 mod n`.

Define the canonical physical boundary chain `P_n` by summing the oriented tetrahedra

$$
[a,a+1,b,b+1]
$$

over unordered pairs of disjoint cyclic edges, with the orientation induced by their cyclic order. There are

$$
\frac{n(n-3)}2
$$

such pairs.

## Boundary identification

The explicit arbitrary-n facet involution cancels every internal facet of `T_n`. Its unpaired facets are exactly the tetrahedra formed by two disjoint cyclic edges:

- `F_0(i,j)` gives the pairs `(i-1,i)` and `(j-1,j)` away from the anchor edge;
- `F_2(2,j)` and `F_4(2,4)` supply pairs involving `(n,1)` on one side;
- `F_3(i,n-1)` and `F_1(n-3,n-1)` supply the remaining pairs involving `(n-1,n)`.

The induced signs agree with cyclic ordering in each case. Hence

$$
\partial T_n=P_n.
$$

The definition of `P_n` is cyclic, so

$$
\partial(\rho T_n)
=\rho P_n
=P_n.
$$

Therefore

$$
Z_n:=\rho T_n-T_n
$$

is a simplicial four-cycle.

## Filling the cycle

The full simplex on `n` vertices is contractible. Its simplicial chain complex has zero homology in degree four. Consequently there exists a five-chain `H_n` such that

$$
Z_n=\partial H_n.
$$

This existence is purely finite for each supplied `n`, but the contracting homotopy is uniform: choosing any fixed cone vertex `v`, the standard cone operator satisfies

$$
\partial h_v+h_v\partial=I
$$

on positive-degree chains. Since `partial Z_n=0`, one may take

$$
H_n=h_vZ_n.
$$

Thus no finite-range enumeration is used.

## Five-bracket cocycle

Map an oriented four-simplex to its momentum-supertwistor five-bracket:

$$
R([a,b,c,d,e])=[a,b,c,d,e].
$$

For every oriented five-simplex, the six-term identity is exactly

$$
R(\partial[a,b,c,d,e,f])=0.
$$

By linearity, `R` annihilates every simplicial five-boundary. Therefore

$$
R(\rho T_n)-R(T_n)
=R(\partial H_n)
=0.
$$

Since `R(T_n)=A_n^NMHV`, this proves

$$
\rho\mathcal A_n^{\rm NMHV}
=\mathcal A_n^{\rm NMHV}
$$

for every `n>=6`.

## What supplies the proof

Three independently checked ingredients enter:

1. the arbitrary-n facet involution proving `partial T_n=P_n`;
2. the standard simplicial cone contraction;
3. the six-term five-bracket identity.

The finite cyclic-invariance checks through twelve points are regression tests for conventions, not the logical basis of the universal theorem.

## Claim boundary

This proves cyclic invariance of the standard tree-level NMHV BCFW superamplitude. It does not establish reflection invariance, equality under arbitrary non-simplicial decompositions, loop-level cyclicity, or corresponding theorems for general `N^kMHV` sectors.
