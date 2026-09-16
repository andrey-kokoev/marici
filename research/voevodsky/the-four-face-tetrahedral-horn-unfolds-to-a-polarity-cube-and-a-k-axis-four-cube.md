# The four-face tetrahedral horn unfolds to a polarity cube and a k-axis 4-cube

## Fixed-stage square

The tetrahedral pasting equation

\[
H_{124}\circ(H_{234}*C_{12})
=
H_{134}\circ(C_{34}*H_{123})
\]

can be drawn as a square of whiskered face transformations. Its two composite
seams are

\[
\mathsf S_L
=H_{124}\circ(H_{234}*C_{12}),
\]

\[
\mathsf S_R
=H_{134}\circ(C_{34}*H_{123}).
\]

Signed coherence says

\[
\mathsf S_L=\mathsf S_R.
\]

Thus the four triangular faces form two composite seams, and equality of those
seams fills one square. This is a cubical unfolding of the tetrahedral horn;
it does not replace the tetrahedral indexing.

## Positive square

Each signed face has positive and negative feature legs. Write

\[
H_{ijk}=H_{ijk}^{+}-H_{ijk}^{-}.
\]

A positive square is not obtained by merely applying this notation. It requires
positive feature maps for all four sides and contractive comparison maps making
both composite seams equal as positive Grams.

For the semilocal pyramid:

- \(H_{123}^{+}\) is supplied by unitary Hardy--Titchmarsh transport;
- \(H_{124}^{+}\) is supplied by the regulated eight-leg feature together with
  its affine volume coordinate;
- the coupled lifts of \(H_{134}\) and \(H_{234}\) are equivalent to the
  Schur--Douglas condition
  \[
  C_k\succeq b_kb_k^*.
  \]

When that condition holds, the two composite seams define one positive
commutative square at stage \(k\).

## Polarity cube

There are two fixed-stage squares, one for each polarity. They become opposite
faces of a cube. The other four faces are the comparison squares induced by:

1. the fundamental symmetry exchanging positive and negative legs;
2. endpoint even/odd parity;
3. Tate/reference reflection;
4. primal/contragredient transport.

The cube is positive when all six square faces admit compatible positive Gram
realizations and the polarity maps are isometric or contractive in the declared
metrics. Its central condition is not additional signed commutativity: it is
compatibility of the two polar factorizations with the same common bulk.

In particular, independently choosing Jordan decompositions on the two
opposite squares does not fill the cube. The common physical remainder must be
shared before compression.

## k-axis raises the dimension again

At stages \(k\) and \(k+1\), the two polarity cubes are connected by the
successor maps. They are opposite cubical facets of a 4-cube. The remaining six
cubical facets encode successor naturality of the six faces of the polarity
cube.

Hence the dimensional hierarchy is

\[
\boxed{
\begin{aligned}
&4\text{ triangular faces}
\longrightarrow 2\text{ composite seams}
\longrightarrow 1\text{ square},\\
&2\text{ polarity squares}
\longrightarrow 1\text{ polarity cube},\\
&2\text{ consecutive polarity cubes}
\longrightarrow 1\text{ k-coherence 4-cube}.
\end{aligned}}
\]

The `k` direction should not be used twice: if it is the axis joining two
squares, the result is a cube; if polarity already joins the squares into a
cube, adjoining `k` produces a 4-cube.

## Positive filling conditions by dimension

### Square

Equality of the two composite positive seams.

### Cube

A common positive bulk and compatible contractions on all six square faces. In
the present rank-one endpoint reduction, this is governed by

\[
\begin{pmatrix}C_k&b_k\\b_k^*&1\end{pmatrix}\succeq0.
\]

### 4-cube

Successor naturality of the common bulk and Douglas contraction:

\[
T_kC_k^{1/2}=C_{k+1}^{1/2}S_k,
\qquad
R_kc_k=c_{k+1}T_k.
\]

For dyadic Halmos depth, the successor is isometric subdivision and preserves
the Gram rather than adding positivity. Cutoff and conductor successors require
separate metric laws.

## What this reframing establishes

It identifies the exact higher cells that a complete proof must inhabit and
prevents three conflations:

- signed tetrahedral coherence versus positive square filling;
- polarity doubling versus `k` succession;
- isometric refinement versus positive accretion.

It does not prove the Schur--Douglas inequality. It shows where that single
analytic inequality sits: it is the metric filler of the polarity cube, whose
naturality is then the principal 4-cube condition.
