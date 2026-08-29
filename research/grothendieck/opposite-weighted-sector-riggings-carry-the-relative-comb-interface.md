# Opposite Weighted Sector Riggings Carry the Relative Comb Interface

## Sector spaces

Fix \(\varepsilon>0\). Define

\[
\mathcal H_{+,\varepsilon}
=
H^1\left(
\mathbb R,
e^{(1+\varepsilon)q}\,dq
\right)
\]

and

\[
\mathcal H_{-,\varepsilon}
=
H^1\left(
\mathbb R,
e^{-(1+\varepsilon)q}\,dq
\right).
\]

These are opposite rather than competing completions.

## Matching source vacua

The logarithmic Gaussian vacua are

\[
\psi_+(q)
=
e^{q/2}e^{-\pi e^{2q}},
\qquad
\psi_-(q)=\psi_+(-q).
\]

At negative infinity,

\[
|\psi_+(q)|^2\sim e^q,
\]

so its positive-sector weighted density behaves like

\[
e^{(2+\varepsilon)q},
\]

which is integrable. At positive infinity it decays superexponentially.
Therefore

\[
\psi_+\in\mathcal H_{+,\varepsilon}.
\]

By reflection,

\[
\psi_-\in\mathcal H_{-,\varepsilon}.
\]

## Matching comb traces

Define

\[
B_+f
=
\sum_{n\geq1}n^{-1/2}f(\log n),
\]

and

\[
B_-g
=
\sum_{n\geq1}n^{-1/2}g(-\log n).
\]

Partition the positive logarithmic ray into Voronoi cells around \(\log n\).
Their lengths are comparable to \(1/n\). The one-dimensional Sobolev trace
estimate on the \(n\)-th cell, combined with the weight
\(e^{(1+\varepsilon)q}\asymp n^{1+\varepsilon}\), gives

\[
|f(\log n)|^2
\leq
C_\varepsilon n^{-\varepsilon}E_n(f),
\]

where the nonnegative cell energies satisfy

\[
\sum_nE_n(f)
\leq
\lVert f\rVert_{\mathcal H_{+,\varepsilon}}^2.
\]

Consequently,

\[
|B_+f|
\leq
C_\varepsilon
\left(
\sum_{n\geq1}n^{-1-\varepsilon}
\right)^{1/2}
\lVert f\rVert_{\mathcal H_{+,\varepsilon}}.
\]

Thus \(B_+\) is continuous on \(\mathcal H_{+,\varepsilon}\). Reflection gives
continuity of \(B_-\) on \(\mathcal H_{-,\varepsilon}\).

The strict inequality \(\varepsilon>0\) is essential: at \(\varepsilon=0\),
the controlling series is harmonic.

## Continuous relative pairing

The two sectors pair through

\[
\langle f,g\rangle_{\mathrm{rel}}
=
\int_{\mathbb R}
f(q)\overline{g(q)}\,dq.
\]

Cauchy–Schwarz with opposite weights gives

\[
|\langle f,g\rangle_{\mathrm{rel}}|
\leq
\lVert f\rVert_{\mathcal H_{+,\varepsilon}}
\lVert g\rVert_{\mathcal H_{-,\varepsilon}}.
\]

In particular, the vacuum interface is finite:

\[
\psi_+(q)\psi_-(q)
=
e^{-\pi(e^{2q}+e^{-2q})}.
\]

## Crossed traces remain forbidden

The incorrectly crossed incidence diverges:

\[
B_+\psi_-
=
\sum_{n\geq1}
\frac1n
e^{-\pi/n^2}
=
\infty.
\]

Likewise,

\[
B_-\psi_+=\infty.
\]

Thus the typing is intrinsic:

- \(B_+\) acts on the positive sector and \(\psi_+\);
- \(B_-\) acts on the negative sector and \(\psi_-\);
- the two sectors communicate through the relative pairing;
- neither comb may be applied to the opposite vacuum.

## Critical projective boundary

The family indexed by \(\varepsilon>0\) approaches the critical exponent where
comb continuity fails. The natural completed object is therefore a
projective or rigged family of sector spaces, with the seam encoded by the
limit \(\varepsilon\downarrow0\).

This constructs the first nontrivial functional-analytic form of the
two-sector interface demanded by the carrier/comb no-go.

## Scope boundary

The relative pairing and typed traces are now continuous, but no determinant
or zero-to-kernel bridge has yet been derived from them.

## Falsifier

The construction fails if a matching trace is discontinuous, a matching vacuum
has infinite norm, or a crossed trace converges. The cell estimate, endpoint
asymptotics, and harmonic divergence decide these three tests.
