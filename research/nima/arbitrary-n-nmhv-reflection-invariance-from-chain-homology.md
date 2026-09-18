# Arbitrary-n NMHV reflection invariance from chain homology

## Setup

Let

$$
T_n
=
\sum_{2\le i\le n-2\atop i+2\le j\le n-1}
[n,i-1,i,j-1,j]
$$

be the oriented NMHV BCFW four-chain. Let `sigma` be a reflection of the cyclic labels, for example

$$
\sigma(a)=n+1-a
$$

with labels understood cyclically.

The canonical physical boundary is

$$
P_n
=
\sum_{\{(a,a+1),(b,b+1)\}}
[a,a+1,b,b+1],
$$

where the sum runs over unordered pairs of disjoint cyclic edges and each tetrahedron receives the orientation induced by cyclic order.

## Reflection of the physical boundary

Reflection sends each cyclic edge to the same edge with its two endpoints reversed. On a physical tetrahedron it reverses both edge pairs:

$$
[a,a+1,b,b+1]
\longmapsto
[\sigma(a),\sigma(a+1),\sigma(b),\sigma(b+1)].
$$

Returning each reflected edge to the canonical cyclic orientation uses two transpositions, one in each edge. Exchanging the two edge blocks, when required to restore their cyclic order, is a permutation of two blocks of size two and contributes four transpositions. The total parity is even. Hence every reflected physical tetrahedron has the canonical orientation of its image.

Reflection permutes unordered disjoint edge pairs bijectively, so

$$
\sigma P_n=P_n.
$$

Since the facet-involution theorem gives `partial T_n=P_n`, one has

$$
\partial(\sigma T_n-T_n)=0.
$$

## Simplicial filling

The full simplex on the `n` labels is contractible, so the four-cycle

$$
Z_n^{\rm refl}=\sigma T_n-T_n
$$

is a boundary. Using the standard cone contraction, there exists an explicit five-chain `H_n^refl` with

$$
Z_n^{\rm refl}=\partial H_n^{\rm refl}.
$$

Map oriented four-simplices to momentum-supertwistor five-brackets. The six-term identity says that this map annihilates the boundary of every oriented five-simplex. Therefore

$$
R(\sigma T_n)-R(T_n)
=R(\partial H_n^{\rm refl})
=0.
$$

Thus

$$
\sigma\mathcal A_n^{\rm NMHV}
=
\mathcal A_n^{\rm NMHV}
$$

for every `n>=6`.

## Dihedral consequence

Cyclic rotation and one reflection generate the dihedral group. Combining this theorem with arbitrary-n cyclic invariance proves full dihedral invariance of the standard NMHV BCFW superamplitude at every multiplicity.

## Relation to executable evidence

Exact finite checks verify reflection invariance at rational kinematics through ten points and coefficient-level BCFW reflection invariance through twelve points. They serve as convention regression tests; the arbitrary-n result follows from reflection invariance of `P_n`, simplicial contractibility, and the six-term identity.

## Claim boundary

This proves tree-level dihedral invariance for the NMHV BCFW superamplitude. It does not prove parity symmetry between different helicity sectors, loop-level reflection properties, or a corresponding chain theorem for general `N^kMHV` amplitudes.
