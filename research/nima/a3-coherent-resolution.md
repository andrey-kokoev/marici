# The finite A3 Coherent Resolution

## Question

What source-supported resolution can be constructed from the established type-A cluster carrier without importing physical coefficients or radiative data?

## Construction

Triangulations of a hexagon form the vertices of the type-A3 associahedron. Diagonal flips form its edges. Fixing one diagonal gives a face: three are squares and six are pentagons. With orientations fixed algorithmically, let

\[
C_0=\mathbb Z^{14},\qquad
C_1=\mathbb Z^{21},\qquad
C_2=\mathbb Z^9,\qquad
C_3=\mathbb Z.
\]

The differential from `C1` to `C0` is signed edge incidence. The differential from `C2` to `C1` is the oriented boundary of each square or pentagon. The differential from `C3` to `C2` is the unique primitive integral orientation of the polytope boundary. Augmentation sends every cluster vertex to `1`.

The resulting augmented complex is

\[
0\longrightarrow\mathbb Z
\longrightarrow\mathbb Z^9
\longrightarrow\mathbb Z^{21}
\longrightarrow\mathbb Z^{14}
\longrightarrow\mathbb Z
\longrightarrow0.
\]

## Exact checks

The computed ranks are

\[
\operatorname{rank}d_1=13,\qquad
\operatorname{rank}d_2=8,\qquad
\operatorname{rank}d_3=1.
\]

The checker verifies

\[
d_1d_2=0,\qquad d_2d_3=0,\qquad \varepsilon d_1=0,
\]

and vanishing augmented homology in every degree. The top boundary coefficients are all units, so the construction is integral and does not require fitted weights.

## Relation to the Coherent Construction Law

This supplies a resolution of the finite A3 cluster-label carrier that was previously only described by vertices, flips, squares, and pentagons. It provides the chain-level location where a mutation-edge coefficient system and its face coboundary can be defined.

It does not yet resolve the physical NNMHV construction. A physical comparison requires three additional maps:

1. a labelled map from certified history or positroid cells to cluster vertices;
2. a source-derived coefficient transport on every mutation edge;
3. proof that the resulting weighted map commutes with the displayed differentials.

The single known negative exchange residual does not determine item 2.

## Claim boundary

This is a finite exact theorem for the A3 combinatorial carrier. It does not construct an arbitrary-cutoff resolution, a resolution of canonical forms, a radiative comparison map, or a physical-time object.

## Disposition

The premise failure identified by `marici.Strominger` and `marici.Benincasa` is partially repaired: a complete signed resolution now exists for the finite A3 cluster-label carrier. Their physical and arbitrary-cutoff tasks remain blocked at the three comparison maps above.

Verification:

- `research/nima/checkers/check_a3_coherent_resolution.py`
- `research/nima/results/a3-coherent-resolution.json`
