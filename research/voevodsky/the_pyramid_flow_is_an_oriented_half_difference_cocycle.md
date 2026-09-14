# The pyramid flow is an oriented half-difference cocycle

## Question

Which integral classes represent information transport between the four component-difference vertices, and what information is unavailable from route flow alone?

## Claim boundary

This packet determines the intrinsic edge transport and its lattice index. It does not identify a particular edge with the source coordinate \(v_{\rm alg}\).

## Oriented edge flow

Let \(d_1,\ldots,d_4\) be the four split-fiber component differences in their primitive \(A_1^3\) closure. Define the oriented transport from vertex \(i\) to vertex \(j\) by

\[
\beta_{ij}=\frac{d_j-d_i}{2}.
\]

All \(\beta_{ij}\) are integral. They obey

\[
\beta_{ji}=-\beta_{ij}
\]

and the triangle coherence law

\[
\beta_{ij}+\beta_{jk}=\beta_{ik}.
\]

Therefore the transport around every triangular face vanishes:

\[
\beta_{ij}+\beta_{jk}+\beta_{ki}=0.
\]

This is the path law the information flow must follow between the four vertices. A longer path carries the sum of its oriented edge classes, and coherent paths with the same endpoints agree.

## Relative flow versus absolute edge carrier

In the established primitive frame,

\[
\beta_{12}=(0,-1,-1),
\quad
\beta_{13}=(-1,0,-1),
\quad
\beta_{14}=(-1,-1,0).
\]

Their determinant has absolute value two. Hence route differences generate an index-two sublattice of \(A_1^3\), not the full primitive closure.

This distinguishes two kinds of information:

- the \(\beta_{ij}\) encode relative transport between vertices;
- one primitive half-sum edge \(\alpha_{ij}=(d_i+d_j)/2\) supplies an absolute anchor selecting the missing coset.

Thus coherence of all paths cannot by itself reconstruct the full primitive response lattice. It needs one anchored physical corner or period normalization.

## Role of the established e6 channel

The physical \(e_6\) corner can play the anchor role once its integral comparison with one labelled component-difference or primitive half-sum is fixed. Starting from that anchor, the oriented edge cocycle transports information to the other three vertices. A complementary readout such as \(v_{\rm alg}\) must evaluate nontrivially on one of these transported relative directions.

The required flow is therefore

\[
\text{anchored physical corner}
\longrightarrow
\beta_{ij}
\longrightarrow
\text{transported primitive class}
\longrightarrow
\text{complementary detector}.
\]

Using only the endpoint mod-two class loses every \(\beta_{ij}\), since all \(d_i\) are congruent modulo two. Using only the relative cocycle leaves the index-two anchoring ambiguity.

## Disposition

The coherence pyramid is an anchored affine transport system. Its edges carry oriented half-differences satisfying exact face cocycles; one primitive absolute anchor is additionally necessary. The missing comparison must attach the known physical \(e_6\) corner to one labelled vertex and then transport along the \(\beta\)-cocycle before applying the second readout.

Verification:

- `research/voevodsky/checkers/check_pyramid_half_difference_cocycle.py`
- `research/voevodsky/results/pyramid_half_difference_cocycle.json`
