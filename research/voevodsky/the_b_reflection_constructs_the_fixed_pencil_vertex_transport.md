# The b-reflection constructs the fixed-pencil vertex transport

## Question

Is there already a global automorphism that acts inside the fixed reflection-adapted pencil and transports its four split-fiber vertices integrally?

## Claim boundary

This packet constructs the permutation action of the global \(b\)-reflection on the abstract component-difference lattice. It does not identify its odd eigenspace with \(v_{\rm alg}\).

## Global automorphism

The homogeneous Cayley–Menger branch polynomial is even in \(b\). Hence

\[
r_b:[a:b:h:W]\longmapsto[a:-b:h:W]
\]

is a global automorphism of the degree-two del Pezzo surface.

For the reflection-adapted pencil coordinate

\[
q=b/h,
\]

it acts internally by

\[
q\longmapsto-q.
\]

The four split fibers occur at

\[
q=\pm(y+z),
\qquad
q=\pm(2x+y+z).
\]

Label their oriented component differences so that \((d_1,d_2)\) belong to the first sign pair and \((d_3,d_4)\) to the second. Because \(r_b\) leaves \(W\) unchanged and the two signs in each base pair have the same square polynomial, it preserves the \(W=+Q\) and \(W=-Q\) component labels. Therefore

\[
r_b:(d_1,d_2,d_3,d_4)
\longmapsto
(d_2,d_1,d_4,d_3).
\]

This is a source-derived fixed-pencil transport, unlike the earlier unsupported import of site exchange from the total-energy diagram.

## Action on the primitive edge frame

For

\[
\alpha_{12}=\frac{d_1+d_2}{2},
\quad
\alpha_{13}=\frac{d_1+d_3}{2},
\quad
\alpha_{14}=\frac{d_1+d_4}{2},
\]

the action is

\[
r_b(\alpha_{12})=\alpha_{12},
\qquad
r_b(\alpha_{13})=-\alpha_{13},
\qquad
r_b(\alpha_{14})=-\alpha_{14}.
\]

Thus the fixed-pencil primitive lattice splits integrally as

\[
A_1^3
=
\mathbb Z\alpha_{12}
\oplus
\mathbb Z\alpha_{13}
\oplus
\mathbb Z\alpha_{14},
\]

with reflection characters \((+,-,-)\).

## Role in the flow

The flow between opposite-sign vertices is now genuine:

\[
d_1\leftrightarrow d_2,
\qquad
d_3\leftrightarrow d_4.
\]

Its invariant information is carried by the paired half-sum \(\alpha_{12}\); its two-dimensional variation is carried by \(\alpha_{13},\alpha_{14}\). Therefore any complementary detector odd under \(r_b\) must live in the latter plane.

This does not by itself select a unique line: the odd eigenspace has rank two. A second commuting character or one period column is still needed to distinguish \(v_{\rm alg}\) within it.

## Disposition

The fixed-pencil transport exists and is supplied by \(r_b\). It reduces the edge-to-de-Rham comparison from three primitive directions to one invariant line plus a rank-two odd plane. The remaining role of the missing comparison is to identify the source response coordinates within that character decomposition.

Verification:

- `research/voevodsky/checkers/check_b_reflection_fixed_pencil_transport.py`
- `research/voevodsky/results/b_reflection_fixed_pencil_transport.json`
