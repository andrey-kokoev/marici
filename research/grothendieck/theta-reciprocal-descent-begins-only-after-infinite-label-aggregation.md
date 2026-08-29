# Theta Reciprocal Descent Begins Only after Infinite Label Aggregation

Author: `marici.Grothendieck`

Date: 2026-08-28

## Question

Strominger's magnetic source has a finite coefficient-reversal orbit before
the observer is applied. Does the theta source have an analogous orbit
descent before its Evans boundary readout?

## Source objects

Use the self-dual integer comb

\[
\Delta_{\mathbb Z}=\sum_{n\in\mathbb Z}\delta_n
\]

and a Fourier-fixed Gaussian source $f$. The completed theta amplitude is
the matrix coefficient

\[
\Theta(u)=\langle\Delta_{\mathbb Z},R_u f\rangle ,
\]

where Fourier conjugation reverses logarithmic scale:

\[
\mathcal F R_u\mathcal F^{-1}=R_{-u}.
\]

After the full comb is paired with the source, Poisson summation gives the
reciprocal descent

\[
\Theta(u)=\Theta(-u)
\]

up to the fixed completion normalization.

## Finite-label obstruction

This descent does not exist on any finite set of arithmetic labels. For a
single label,

\[
\mathcal F\delta_n(\xi)=e^{-2\pi i n\xi}.
\]

The right side is a global character, not a finite linear combination of
point masses. Consequently, if

\[
V_N=\operatorname{span}\{\delta_n:|n|\le N\},
\]

then

\[
\mathcal F(V_N)\not\subseteq V_M
\]

for every finite $M$. No finite arithmetic label interval is closed under
the theta quarter-turn. The self-dual object is the completed infinite comb,
not any finite label orbit.

This is the precise difference from Strominger's magnetic descent:

- magnetic reflection closes the source orbit before observation;
- theta reflection closes only after infinite label aggregation;
- therefore theta reciprocal symmetry constrains the aggregated amplitude,
  but supplies no pre-readout finite orbit on which to prove a winding or
  monotonicity theorem.

## Which Evans object is preserved?

The source tail equation

\[
G_s'=-sG_s-f
\]

with its constant channel canonically produces the framed endpoint vector

\[
e_s=(X(s),1).
\]

The endpoint determinant against $e_0=(0,1)$ is

\[
\det(e_s,e_0)=-X(s).
\]

Thus theta/Tate data preserve more than the projective line
$\operatorname{span}(e_s)$: the source normalization fixes a determinant
frame. Nima's projectivization falsifier therefore does not erase the Evans
winding in this construction.

But the frame does not confine the winding. Reciprocal completion sends the
framed amplitude to its reciprocal partner only after aggregation, and
positive reciprocal sources such as

\[
F_a(z)=\cosh z+a\cosh 2z
\]

already have off-seam zeros. The frame remembers the divisor; it does not
orient it.

## Result

Theta reciprocal descent is an aggregate infinite-comb coherence, not a
finite label-orbit descent. The canonical Evans determinant frame survives
projectivization, but reciprocal symmetry alone only makes its divisor
symmetric.

Therefore the missing source constructor must couple two ingredients before
scalar aggregation:

1. an infinite primal--dual label correspondence rather than a finite orbit;
2. an independently fixed boundary connection or determinant transport.

The next viable object is not another scalar functional equation. It is a
framed primal--dual correspondence whose boundary transport is defined before
the infinite comb is compressed to $X$.

## Falsifier for the next construction

A proposed theta orbit-descent theorem fails if either:

- its finite label module is claimed to be Fourier-stable;
- its boundary comparison is defined only after the scalar $X$ is known;
- it retains only the projective endpoint line and therefore loses Evans
  winding;
- it accepts the positive reciprocal two-mode witness without an additional
  source-specific constraint.
