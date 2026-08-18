---
id: 532
date: 2026-08-18
title: The Naive Full-Cell Cut Cech Restriction Is Not a Chain Map
---

# The Naive Full-Cell Cut Cech Restriction Is Not a Chain Map

Entry 446 constructed the primitive Thom-twisted scalar section on the
physical Cut nerve and asked whether it lifts to the eight loaded Cut charts.
The most direct lift would project each (1075)-cell chart onto its
(125)-cell pair overlap and tensor that projection with the oriented Čech
incidence map.  This entry tests that construction on every loaded cell.

For a physical Cut (D), let (C_D) be the loaded complex on the link of
(D).  For a compatible pair (D,D'), let (C_{DD'}) be the loaded complex
on their common link.  Set-theoretically,

\[
 C_{DD'}\subset C_D,
\]

so there is a coordinate projection (p_{D,D'}:C_D\to C_{DD'}).  Normal
marking differentials preserve this subset.  Radial differentials do not: a
face compatible with (D') may acquire a diagonal crossing (D').  Hence

\[
 p_{D,D'}d\ne dp_{D,D'}.
\]

## Exact census

The audit constructs all eight charts and all twelve compatible overlaps:

\[
8\cdot1075=8600,
\qquad
12\cdot125=1500
\]

loaded generators.  Across the twenty-four oriented chart-to-overlap maps it
finds

\[
7200
\]

commuting internal arrows, but also

\[
\boxed{7320}
\]

radial arrows that leave the common-link subcomplex.  There are no arrows
entering it from the projected-away sector, as required by downward
compatibility.  The defect is therefore directional and support-theoretic,
not a random failure of incidence signs.

The native odd Thom line still cancels the scalar Koszul holonomy, and the
constant coefficient (+1) agrees on all (1500) overlap generators.  But a
sign local system cannot repair a map that fails to commute with the carrier
differential.  Since the physical Cut nerve has no triple intersections,
there is also no higher scalar Čech cell that can absorb these terms.

## Consequence

The scalar conclusion of Entry 446 remains valid, but it cannot be tensored
naively with the loaded chart carriers.  Full eight-point descent requires a
source-derived relative restriction

\[
 r^!_{D,D'}:C_D\longrightarrow C_{DD'}
\]

or an explicit homotopy whose boundary is exactly the escaping radial packet.
This is the eight-point analogue of the mixed-variance lesson at six points:
ordinary coordinate restriction has the wrong variance at the support wall.

The next calculation is to group the (7320) defects by the added crossing
diagonal and loaded degree, then test whether the Cut-collar unit cone of
Entry 439 provides a canonical nullhomotopy.  No quotient or correction may
be fitted after seeing the census.

The executable audit is
`research/voevodsky/check_n8_full_twisted_cut_cech_lift.py`.
