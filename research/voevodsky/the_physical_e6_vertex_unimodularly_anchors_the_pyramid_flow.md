# The physical e6 vertex unimodularly anchors the pyramid flow

## Question

Does the established physical \(e_6\) component-difference class supply the absolute anchor required by the oriented edge cocycle?

## Claim boundary

This packet proves the integral lattice statement after choosing the adapted marking in which the physical infinity component difference is \(d_1\). It does not identify the two remaining primitive coordinates with specific de Rham generators.

## Physical vertex

The global infinity split fiber has oriented component difference

\[
d_\infty=C_--C_+
=3H-E_1-\cdots-E_6-3E_7.
\]

The physical corner interval is the primitive dual detector of this same global class, up to the established overall orientation convention. Choose the four-vertex marking so that

\[
d_1=d_\infty.
\]

Thus the physical \(e_6\) channel anchors an actual vertex, not merely a half-sum edge.

## Unimodular reconstruction

In the established primitive \(A_1^3\) frame,

\[
d_1=(1,1,1),
\]

and the two oriented edge flows

\[
\beta_{12}=\frac{d_2-d_1}{2}=(0,-1,-1),
\qquad
\beta_{13}=\frac{d_3-d_1}{2}=(-1,0,-1).
\]

The matrix with columns \((d_1,\beta_{12},\beta_{13})\) has determinant one. Therefore

\[
A_1^3
=
\mathbb Z d_1
\oplus_{m lattice}
\mathbb Z\beta_{12}
\oplus_{m lattice}
\mathbb Z\beta_{13}.
\]

No index-two ambiguity remains once the physical vertex itself is retained. The earlier index-two statement concerned the lattice generated only by relative edge flows.

The fourth vertex and every other edge are reconstructed by coherence:

\[
d_2=d_1+2\beta_{12},
\qquad
d_3=d_1+2\beta_{13},
\qquad
d_4=-d_1-d_2-d_3.
\]

## Information flow

The integral flow should therefore be organized as

\[
\text{physical }e_6\text{ vertex }d_1
\longrightarrow
(\beta_{12},\beta_{13})
\longrightarrow
(d_2,d_3,d_4)
\longrightarrow
\text{complementary period coordinates}.
\]

The role of the missing comparison is no longer to construct or saturate the lattice. It must transport the two relative edge generators into the two-dimensional de Rham complement to the anchored \(e_6\) line and identify which linear functional is \(v_{\rm alg}\).

## Disposition

The physical \(e_6\) channel supplies a unimodular anchor for the complete primitive pyramid lattice. The remaining problem is a rank-two edge-to-de-Rham comparison, not an index correction or a four-vertex reconstruction problem.

Verification:

- `research/voevodsky/checkers/check_physical_e6_vertex_anchor.py`
- `research/voevodsky/results/physical_e6_vertex_anchor.json`
