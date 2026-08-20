# 1083 — The Physical Hexagon Activates Only After Double Leray Continuation

## Problem

Entry 1082 showed that the six ordered residue terms of the three-site
integrand generate the nonzero fundamental class of the physical normal link

\[
\operatorname{Lk}_{\rm phys}=C_6.
\]

The remaining question was whether the Bunch--Davies integration chain
physically selects this class.

Two notions of restriction must be kept separate:

1. ordinary intersection with the literal positive Cayley--Menger chain;
2. Leray specialization of its negative-imaginary boundary value after
   analytic continuation to a factorization sheet.

## Literal positive-chain restriction

The frozen three-cut certificate writes the positive chain as

\[
a,b,c\ge0,
\qquad
x,y,z>0,
\]

with the positive Cayley--Menger square-root sheet and all required signed
minor inequalities. On this chain,

\[
q_{\mathcal G_{12}}=E+c>E,
\qquad
q_{\mathcal G_{23}}=E+a>E,
\qquad
q_{\mathcal G_{31}}=E+b>E.
\]

For physical \(E>0\), neither the interior nor the boundary of the chain meets
the marked cut union. Therefore the six literal incidence pairings are

\[
\boxed{(0,0,0,0,0,0).}
\]

This vanishing is an ordinary-support statement. It does not determine the
continued boundary value.

## Boundary-value Leray specialization

Entry 180 froze the relevant primary-source data:

- arXiv:2305.19686v2, equations (4.18)--(4.20), puts every external and
  internal energy in the negative-imaginary tube;
- arXiv:2402.06558 fixes the oriented positive Cayley--Menger chain and its
  signed-minor boundary;
- arXiv:2408.16386v2 fixes the labelled polar coordinates and unit residue
  Jacobians.

The negative-imaginary tube is convex. Hence the continued positive
Cayley--Menger chain has a unique local Leray germ at every generic transverse
marked pole. Its sheet, orientation, Jacobian, and multiplicity are fixed, and
the multiplicity is one.

For a compatible pair in equation (51), applying this construction
successively gives a unique double-Leray germ. Antisymmetry under reversing the
two residue normals is exactly the sign used in Entry 1082. Consequently the
six continued germs have oriented coefficients

\[
(-1,-1,-1,-1,-1,-1).
\]

They therefore represent the nonzero generator

\[
\boxed{
[\Gamma^{(2)}_{\rm BD}]
=
\pm[C_6]
\ne0
\quad\text{in }H_1(C_6;\mathbb Q),
}
\]

where the overall sign depends only on the already frozen global orientation
convention.

## Narrow theorem

\[
\boxed{
\begin{aligned}
\text{literal positive-chain restriction}&=0,\\
\text{Bunch--Davies double-Leray specialization}&\ne0.
\end{aligned}
}
\]

Thus the physical hexagon is activated as analytic-continuation/nearby-cycle
data, not as a boundary component of the starting real chamber.

This is the precise mechanism that was unavailable for the two-site spurious
corner: here both the support complex and the continued residue germ are
source-defined.

## Architectural consequence

No new carrier datum is required. The result uses

\[
\text{connected-subgraph incidence}
+
\text{Cayley--Menger relative chain}
+
\text{Leray/nearby specialization}
+
\text{ordered residue signs}.
\]

This is direct evidence for H2's shared support-sensitive calculus with a
cosmological relative-chain coefficient object.

## Scope boundary

The theorem is local on generic transverse factorization patches. It does not
assert an additional independent integrated period, nor determine global
monodromy when the six strata meet the elliptic or algebraic discriminants.

## Next falsifier

Transport the double-Leray generator around the cyclic atlas and toward the
total-energy degeneration. Test whether it maps to an existing Cut flag/Tate
nearby-cycle class or leaves a residual extension into the elliptic
coefficient block. This comparison must retain occurrence labels and cannot be
inferred from the rank-one result alone.

## Durable packet

- `research/benincasa/three-site-double-leray-activation.json`
- `research/benincasa/three-cut-relative-chain-pairing-certificate.json`
- `research/benincasa/check_three_site_physical_residue_link.rs`

