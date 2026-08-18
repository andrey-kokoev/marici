---
authors:
  - marici.Nima
date: 2026-08-18
---
# 858 — The Wall Quotient Is Regular at the Generic Källén Quartic

## Coordinate identification

The marked-relative reduction engine does not use abstract \((u,v)\)
coordinates.  Its source code fixes

\[
x=1,
\qquad
y=\frac{u+v}{2}-1,
\qquad
z=\frac{u-v}{2}.
\]

Consequently

\[
E=x+y+z=u.
\]

This identifies the source quartic in exactly the coordinates used by the
rank-three and forthcoming rank-twelve connections.

## Normalized quartic

Substitution into

\[
\mathcal Q
=-16x^2y^2-8xyE^2+8(x+y)E^3-5E^4
\]

gives

\[
\boxed{
\begin{aligned}
\mathcal Q_{uv}={}&-u^4+4u^3v-4u^3-4u^2v+4u^2\\
&-8uv-4v^2+16u+16v-16.
\end{aligned}
}
\]

The standard-library checker reconstructs this polynomial coefficientwise
from the source formula.

Entry 178 proves irreducibility of the homogeneous source quartic.  The
displayed change of homogeneous variables is invertible, and the chart
\(x=1\) is a dehomogenization not contained in the quartic.  Therefore
\(\mathcal Q_{uv}\) remains irreducible of degree four over \(\mathbb Q\).

## Comparison with the quotient connection

Entry 855's exact rank-three connection has denominator factors

\[
u,quad u-2,quad v-2,quad u+v-2,quad D,quad H,
\]

where

\[
D=-4+12u-6uv+4v-9u^2+4u^2v-v^2
\]

and

\[
H=-2-3u+2uv+v-u^2v+u^3.
\]

The four linear factors have degree one and \(D,H\) have degree three.
Since the irreducible quartic \(\mathcal Q_{uv}\) cannot divide any of
them,

\[
\boxed{
\gcd\!\left(\mathcal Q_{uv},\operatorname{den}A_3\right)=1.
}
\]

Thus \(A_3\) is regular at the generic point of
\(\mathcal Q_{uv}=0\).

## Consequence for the extension test

Together with the established generic \(\mathcal Q\)-regularity of the
absolute rank-nine system, this discharges Entry 856's diagonal
prerequisite.  Any future logarithmic \(\mathcal Q_{uv}\)-pole in
\(B_u,B_v\) cannot be inherited from either diagonal block.  Its residue is
therefore genuinely off-diagonal and invariant under triangular gauges
regular on the quartic.

No claim about the existence or nonvanishing of that residue is made before
the characteristic-zero extension block is derived.

## Durable verification

- packet: `research/nima/normalized-q-a3-regularity.json`;
- checker: `research/nima/check_normalized_q_a3_regularity.py`;
- allocator claim: `seqclaim-365b65469b40584faea07172`.
