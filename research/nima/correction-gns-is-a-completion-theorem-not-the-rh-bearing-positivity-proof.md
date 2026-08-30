# Correction: GNS is a completion theorem, not the RH-bearing positivity proof

The GNS reduction is structurally correct but must not be counted as progress on
the hard inequality by itself.

For the completed Xi response, positivity of the full Loewner kernel

\[
K_F(x,y)=\frac{F(y)-F(x)}{y-x}
\]

is already RH-equivalent once the meromorphic pole identification is fixed.
Likewise, an order-two Stieltjes representation

\[
F'(x)=\int_0^\infty\frac{d\rho(\lambda)}{(x+\lambda)^2},
\qquad d\rho\ge0,
\]

would place the spectral poles on the required real source axis. Deriving this
representation from the zero divisor would therefore be circular.

GNS only says:

\[
K_F\ge0
\quad\Longrightarrow\quad
K_F(x,y)=\langle R(x),R(y)\rangle
\]

for some canonical minimal carrier. It does not explain why \(K_F\ge0\).

The explanatory theorem must supply \(R(x)\) before scalar Xi reconstruction,
from the undecomposed prime--theta source and its Green correspondence, and
then prove

\[
K_F(x,y)=R(x)^*R(y).
\]

That equality has two logically separate halves:

1. source positivity: \(R(x)^*R(y)\) is positive by construction;
2. spectral identification: its scalar compression equals the Xi Loewner
   kernel.

Only the first half may be used to prove the second. Defining \(R\) as a
Kolmogorov factor of the already-known \(K_F\) reverses the authority arrow.

The positive-even theta measure does not suffice. A symmetric four-atom
positive measure violates the first coupled Loewner curvature inequality.
Hence any valid \(R\) must use more than positivity and reciprocal symmetry:
it must retain the special arithmetic/Poisson coupling and the exterior
boundary incidence.

This yields a sharper finite attack. Before seeking all-rank Loewner
positivity, construct a two-parameter source vector \(R_2(x)\) whose Gram
reproduces the first nontrivial \(2\times2\) mixed Bezoutian. Verify that its
construction:

- is defined before Xi zeros or logarithmic derivatives;
- uses the full theta source before Euler projection;
- retains the external five-cell ports;
- is Poisson-covariant;
- and reproduces the scalar kernel by a Green identity, not by fitted
  Cholesky factorization.

The minimal circular hostile takes a numerically positive finite Loewner
matrix and declares its Cholesky factors to be source states. It passes every
finite positivity test but has no constructor provenance and cannot explain
completion.

Thus the hierarchy is

\[
\text{source-derived Gram factor}
\Longrightarrow
\text{Loewner positivity}
\Longrightarrow
\text{GNS completion}
\Longrightarrow
\text{self-adjoint resolvent}.
\]

GNS closes the last representation step. The earliest missing arrow remains
the source-derived Gram factor, beginning at rank two.
