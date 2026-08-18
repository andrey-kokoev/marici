---
authors:
  - marici.Nima
date: 2026-08-18
---
# 840 — The Triangle–Soft Beck–Chevalley Square Generates Both Labelled Polar Lines

## Canonical square

The triangle equation \(\Lambda\) is independent of the total-energy
coordinate \(E\). Away from their deeper intersections, \((\Lambda,E)\)
is a regular Cartier sequence. Hence the comparison

\[
\psi_E\psi_\Lambda\mathcal P_{\rm pol}
\longrightarrow
\psi_\Lambda\psi_E\mathcal P_{\rm pol}
\]

is the canonical Beck–Chevalley map; no horizontal splitting is involved.

## Labelled fold pair

Entry 838 gives

\[
Q_\pm
=
E^2(a^2-b^2)-P_1^2a^2+P_2^2b^2
\pm2EP_3ab.
\]

At \(E=0\), both factors restrict to the common line

\[
L_0=-P_1^2a^2+P_2^2b^2.
\]

Their first soft-normal derivatives are opposite:

\[
\boxed{
\left(
\partial_EQ_+,\partial_EQ_-
\right)_{E=0}
=
2P_3ab(1,-1).
}
\]

Thus the ordinary restriction supplies the diagonal vector \((1,1)\),
while the existing soft nearby-cycle normal supplies the anti-diagonal
vector \((1,-1)\). Their determinant is

\[
\boxed{-4P_3ab.}
\]

It is a unit at a generic point of the triangle–soft stratum.

## Consequence

\[
\boxed{
\operatorname{Cone}\!\left(
\text{triangle restriction}\oplus\text{soft normal}
\longrightarrow
\langle Q_+,Q_-\rangle
\right)
\simeq0
}
\]

generically away from \(P_3ab=0\). Therefore the existing triangle Gysin
and soft nearby-cycle maps generate both labelled polar fold lines. The
ordinary node of Entry 839 has no residual coefficient excess.

The failure locus

\[
P_3ab=0
\]

is exactly the union of already labelled soft and coordinate-boundary
supports. It must be handled by their iterated localization squares, not by
adding a polar carrier.

## Verification

- checker: research/nima/audit_triangle_soft_polar_beck_chevalley.py;
- packet: research/nima/triangle-soft-polar-beck-chevalley.json;
- allocator claim: seqclaim-07c1b00be3a4b15f4339fef8.
